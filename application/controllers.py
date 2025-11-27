from application.models import *
from app import app
from flask import Flask, render_template, request, redirect, url_for, session
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from sqlalchemy import and_, or_, distinct, desc
import datetime
from dateutil.relativedelta import relativedelta
import re 
from pyisemail import is_email

login_manager = LoginManager()
login_manager.init_app(app)  

date_today = date.today()

# Validation functions
def validate_username(username):
    return re.fullmatch(r"[\w@#$&.\-]{1,32}", username)
def validate_password(password):
    return re.fullmatch(r"[\w@#$&.\-]{5,32}", password)
def validate_email(email):
    return is_email(email)
def validate_contact_number(number):
    return re.fullmatch(r"[\d]{10}", number)
def validate_name(name):
    return re.fullmatch(r"[a-zA-Z ]{,64}", name)
def validate_only_text_fields(number):
    return number.isdigit()
def validate_description(description):
    return re.fullmatch(r"[\w,.\'\/\- ]{1,}", description)
def validate_treatment_details(input_string):
    return re.fullmatch(r"[\w@#!$&+*'\/ \-]{1,}", input_string)

@login_manager.user_loader  
def load_user(user_id): 
    return User.query.get(int(user_id))

@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('login_page.html', flag1 = False, flag2 = False)
    else:
        user_name = request.form['u_name']
        user_password = request.form['u_password']
        
        if validate_username(user_name) == None:
            return render_template('login_page.html')

        if validate_password(user_password) == None:
            return render_template('login_page.html')
        
        user = User.query.filter(User.user_name == user_name).first()
        if user == None:
            return render_template('login_page.html', flag2 = True) # user is not registered

        user_id = user.user_id
        session['user_id'] = user.user_id

        if user_password == user.user_password and user.user_role == 'Admin': #user is admin
            login_user(user)
            return redirect('/admin')
        
        elif user_password == user.user_password and user.user_role == 'Doctor': #user is a doctor
            # check if the user is blacklisted
            if (not user.doctor_relationship.doctor_blacklisted) and (user.doctor_relationship.status == None):
                login_user(user)
                d_id = Doctor.query.filter(Doctor.doctor_user_id == user_id).first()
                dietetics_dept = Department.query.filter(Department.department_name == 'Dietetics').first()
            else:
                message = 'You have been blacklisted by the admin'
                return render_template('error.html', message = message)

            if d_id.department_id != dietetics_dept.department_id:
                return redirect(f'/doctor/{d_id.doctor_id}')
            else:
                return redirect(f'/dietetics/doctor/{d_id.doctor_id}')
            
        elif user_password == user.user_password and user.user_role == 'Patient': #user is a patient
            # check if the user is blacklisted
            if (not user.patient_relationship.patient_blacklisted) and (user.patient_relationship.status == None):
                login_user(user)
                p_id = Patient.query.filter(Patient.patient_user_id == user_id).first()
                return redirect(f'/patient/{p_id.patient_id}')
            else:
                message = 'You have been blacklisted by the admin'
                return render_template('error.html', message = message)
            
        return render_template('login_page.html', flag1 = True) # Invalid username or password

@app.route('/logout')
@login_required
def logout():
    if session['user_id']:
        session.pop('user_id', None)
        return redirect('/')

# Find Admin

@app.route('/admin', methods = ['GET'])
@login_required
def admin_dashboard():
    if session['user_id']:
        if current_user.user_role != 'Admin':
            return 'You are not authorized'
        
        doctors = Doctor.query.filter(Doctor.status == None).all()
        patients = Patient.query.filter(Patient.status == None).all()
        appointments = Appointment.query.all()
        departments = Department.query.filter(Department.status == None).all()

        doctors_first_five = Doctor.query.filter(Doctor.status == None).limit(5).all()
        patients_first_five = Patient.query.filter(Patient.status == None).limit(5).all()
        appointments_first_five = Appointment.query.limit(5).all()
        departments_first_four = Department.query.filter(Department.status == None).limit(4).all()
        appointments = Appointment.query.all()
        admin_name = Admin.query.first()

        return render_template('admin/admin-dashboard.html', doctors = doctors, patients = patients, appointments = appointments, departments = departments,
                               doctors_first_five = doctors_first_five, patients_first_five = patients_first_five, appointments_first_five = appointments_first_five, departments_first_four = departments_first_four, admin_name = admin_name)
    else:
        return redirect('/')

@app.route('/admin/appointment/<int:pid>/<int:did>/<int:aid>', methods = ['GET'])
@login_required
def view_appointment_patient_doctor(pid, did, aid):
    if session['user_id']:
        if current_user.user_role != 'Admin':
            return 'You are not authorized'
        global date_today 
        patient = Patient.query.filter(Patient.patient_id == pid).first()
        age = relativedelta(date_today, patient.patient_dob)
        doctor = Doctor.query.filter(Doctor.doctor_id == did).first()
        this_appointment = Appointment.query.filter(Appointment.appointment_id == aid).first()
        past_appointments = Appointment.query.filter(and_(Appointment.patient_id == pid, Appointment.doctor_id == did, Appointment.date_time <= date_today, Appointment.appointment_id != aid)).all()
        
        booked_appointments = []
        for a in past_appointments:
            if a.t.status != 'Booked':
                booked_appointments += [a]

        upcoming_appointments = Appointment.query.filter(and_(Appointment.patient_id == pid, Appointment.doctor_id == did, Appointment.date_time >= date_today, Appointment.appointment_id != aid)).all()
        return render_template('admin/view-appointment-p-d.html', past_appointments = past_appointments, doctor = doctor, patient = patient, pid = pid, did = did, 
                               upcoming_appointments = upcoming_appointments, age = age, this_appointment = this_appointment, booked_appointments = booked_appointments)
    else:
        return redirect('/')

@app.route('/admin/view-all-appointments', methods = ['GET'])
@login_required    
def view_all_appointments():
    if session['user_id']:
        if current_user.user_role != 'Admin':
            return 'You are not authorized'
        appointments = Appointment.query.all()
        global date_today 
        past_appointments = Appointment.query.filter(Appointment.date_time <= date_today).all()
        upcoming_appointments = Appointment.query.filter(Appointment.date_time >= date_today).all()
        return render_template('admin/view-all-appointments.html', appointments = appointments, past_appointments = past_appointments, upcoming_appointments = upcoming_appointments)
    else:
        return redirect('/')

@app.route('/admin/select-patient', methods = ['GET', 'POST'])
@login_required
def admin_select_patient():
    if session['user_id']:
        if current_user.user_role != 'Admin':
            return 'You are not authorized'
        if request.method == 'GET':
            patients = Patient.query.all()
            return render_template('/admin/select_patient.html', patients = patients)
        else:
            patient_id = request.form['patients_name']
            patient = db.get_or_404(Patient, patient_id)
            return redirect(f'/admin/book-appointment/{ patient.patient_id }')
    else:
        return redirect('/')
    
@app.route('/admin/book-appointment/<int:pid>', methods = ['GET', 'POST'])
@login_required
def admin_book_appointment(pid):
    if session['user_id']:
        if current_user.user_role != 'Admin':
            return 'You are not authorized'
        patient = db.get_or_404(Patient, pid)
        if request.method == 'GET':
            global date_today 
            departments = Department.query.filter(Department.department_name != 'Dietetics').all()
            doctors = Doctor.query.all()
            appointment_dict = {i:0  for i in doctors}

            for i in doctors:
                doctor_availability_list = []
                helper_list = []
                doctor_availability = SlotSchedules.query.filter(and_(SlotSchedules.slot_doctor_id == i.doctor_id, SlotSchedules.date >= date_today)).order_by(SlotSchedules.date, SlotSchedules.schedule_slot_id).all()

                for a in doctor_availability:
                    if [a.date, a.s_sch.slot_name] not in helper_list:
                        helper_list += [[a.date, a.s_sch.slot_name]]
                        doctor_availability_list += [a]
                        appointment_dict[i] = doctor_availability_list
            return render_template('admin/book-appointment.html', departments = departments, doctors = doctors, appointment_dict = appointment_dict, patient = patient)
        else:
            return redirect('/')
    
@app.route('/admin/confirm-appointment/<int:pid>/<int:did>', methods = ['GET', 'POST'])
@login_required
def admin_confirm_appointment(pid, did):
    if session['user_id']:
        if current_user.user_role != 'Admin':
            return 'You are not authorized'        
        # global date_today 
        # da_dict = {}
        # doctor = db.get_or_404(Doctor, did)
        # doctor_slots = SlotSchedules.query.filter(and_(SlotSchedules.slot_doctor_id == doctor.doctor_id, SlotSchedules.date >= date_today)).order_by(SlotSchedules.date, SlotSchedules.schedule_slot_id).all()
        # list_of_next_7_dates = [(date_today + timedelta(days = i)) for i in range(8)]
        # flag1 = False #check for double booking
        # slots = Slot.query.all()
        # selected_slot = None
        patients = Patient.query.order_by(Patient.patient_name).all()
        # for d in list_of_next_7_dates:
        #     da_dict[d] = {}
        #     for s in slots:
        #         query = SlotSchedules.query.filter(SlotSchedules.date == d, SlotSchedules.schedule_slot_id == s.slot_id, SlotSchedules.slot_doctor_id == doctor.doctor_id).first()
        #         da_dict[d][s] = query

        # if request.method == 'GET':
        #     return render_template('admin/confirm-appointment.html', doctor = doctor, doctor_slots = doctor_slots, flag1 = False, list_of_next_7_dates = list_of_next_7_dates, slots = slots, da_dict = da_dict, selected_slot = selected_slot, patients = patients)
        # else: 
            # patient_id = request.form['patients_name']
            # patient = db.get_or_404(Patient, patient_id)
        #     form_content = request.form 
        #     form_content_to_dict = form_content.to_dict(flat = False)
        #     list_of_next_7_dates = [(date_today + timedelta(days = i)) for i in range(8)]

        #     input_slot = request.form['time_slot']
        #     selected_slot = db.get_or_404(SlotSchedules, int(input_slot))
            
        #     sister_slots = SlotSchedules.query.filter(SlotSchedules.schedule_slot_id == selected_slot.schedule_slot_id, 
        #                                               SlotSchedules.date == selected_slot.date, SlotSchedules.slot_patient_id != None).all()
            
        #     if selected_slot.slot_patient_id == None:
        #         selected_slot.slot_patient_id = patient.patient_id 
        #         selected_slot.slot_sch_appointment_rel = Appointment(date_time = selected_slot.date, doctor_id = doctor.doctor_id, patient_id = patient.patient_id)
        #         selected_slot.slot_sch_appointment_rel.t = Treatment(status = 'Booked')
                
        #         # notify patient
        #         notification = PatientDoctorNotifications(role = 'Doctor', message_type = 'Appointment Booking Confirmation', 
        #                                                   message_content = f'Hello, { patient.patient_name }! Your appointment with doctor { doctor.doctor_name } is on { selected_slot.date } ({ selected_slot.s_sch.slot_name })'
        #                                                   ,m_doctor_id = doctor.doctor_id, m_patient_id = patient.patient_id)
        #         db.session.add(notification)
                
        #     if sister_slots != []:
        #         for s in sister_slots:
        #             if s.slot_patient_id == patient.patient_id:
        #                 return render_template('admin/confirm-appointment.html', doctor = doctor, doctor_slots = doctor_slots, flag1 = True, list_of_next_7_dates = list_of_next_7_dates, 
        #                                        slots = slots, da_dict = da_dict, selected_slot = selected_slot, patients = patients, patient = patient)
                    
        #         new_entry = SlotSchedules(date = selected_slot.date, slot_doctor_id = selected_slot.slot_doctor_id, slot_patient_id = patient.patient_id, schedule_slot_id = selected_slot.schedule_slot_id)
        #         new_entry.slot_sch_appointment_rel = Appointment(date_time = selected_slot.date, doctor_id = doctor.doctor_id, patient_id = patient.patient_id)
        #         new_entry.slot_sch_appointment_rel.t = Treatment(status = 'Booked')
        #         db.session.add(new_entry)
        #         db.session.commit()

        #         notification = PatientDoctorNotifications(role = 'Doctor', message_type = 'Appointment Booking Confirmation', 
        #                                                   message_content = f'Hello, { patient.patient_name }! Your appointment with Dr. { doctor.doctor_name } is on { new_entry.date } ({ new_entry.s_sch.slot_name })'
        #                                                   ,m_doctor_id = doctor.doctor_id, m_patient_id = patient.patient_id)
        #         db.session.add(notification)
        #     db.session.commit()

        #     return redirect('/admin')

        global date_today 
        patient = db.get_or_404(Patient, pid)
        doctor = db.get_or_404(Doctor, did)
        list_of_next_7_dates = [(date_today + timedelta(days = i)) for i in range(8)]
        slots = {}
        all_slots = Slot.query.all()
        patients = Patient.query.order_by(Patient.patient_name).all()
        for d in list_of_next_7_dates:
            slots[d] = {}
            for s in all_slots:
                # doctor is not available for this date and this slot
                doctor_unavailable = SlotSchedules.query.filter(SlotSchedules.date == d, SlotSchedules.schedule_slot_id == s.slot_id, SlotSchedules.slot_doctor_id == doctor.doctor_id).all()
                if doctor_unavailable == []:
                    slots[d][s] = -1            
                else:
                    # patient has already has a booking on this date with this doctor
                    booked_slot = SlotSchedules.query.filter(SlotSchedules.date == d, SlotSchedules.schedule_slot_id == s.slot_id, SlotSchedules.slot_doctor_id == doctor.doctor_id, SlotSchedules.slot_patient_id == patient.patient_id).first()
                    # patient has already has a booking on this date with other doctors
                    other_booked_slot = SlotSchedules.query.filter(SlotSchedules.date == d, SlotSchedules.schedule_slot_id == s.slot_id, SlotSchedules.slot_doctor_id != doctor.doctor_id, SlotSchedules.slot_patient_id == patient.patient_id).first()
                    if booked_slot != None:
                        slots[d][s] = [1, booked_slot]
                    if other_booked_slot != None:
                        slots[d][s] = [2, other_booked_slot]
                    if (other_booked_slot == None) and (booked_slot == None):
                        unbooked_slot = SlotSchedules.query.filter(SlotSchedules.date == d, SlotSchedules.schedule_slot_id == s.slot_id, SlotSchedules.slot_doctor_id == doctor.doctor_id).first()
                        slots[d][s] = [0, unbooked_slot]

        if request.method == 'GET':
            return render_template('admin/confirm-appointment.html', doctor = doctor, patient = patient, list_of_next_7_dates = list_of_next_7_dates, slots = slots, 
                                   all_slots = all_slots)
        else:
            form_content = request.form 
            form_content_to_dict = form_content.to_dict(flat = False)
            list_of_next_7_dates = [(date_today + timedelta(days = i)) for i in range(8)]

            input_slot = request.form['time_slot']
            selected_slot = db.get_or_404(SlotSchedules, int(input_slot))
            if selected_slot.slot_patient_id == None:
                selected_slot.slot_patient_id = patient.patient_id 
                selected_slot.slot_sch_appointment_rel = Appointment(date_time = selected_slot.date, doctor_id = doctor.doctor_id, patient_id = pid)
                selected_slot.slot_sch_appointment_rel.t = Treatment(status = 'Booked')
                
                # notify patient
                notification = PatientDoctorNotifications(role = 'Doctor', message_type = 'Appointment Booking Confirmation', 
                                                          message_content = f'Hello, { patient.patient_name }! Your appointment with doctor { doctor.doctor_name } is on { selected_slot.date } ({ selected_slot.s_sch.slot_name })'
                                                          ,m_doctor_id = doctor.doctor_id, m_patient_id = pid)
                db.session.add(notification)
                db.session.commit()
                return redirect('/admin')
            
            else:
                # patient_id = request.form['patients_name']
                patient = db.get_or_404(Patient, pid)
                new_entry = SlotSchedules(date = selected_slot.date, slot_doctor_id = selected_slot.slot_doctor_id, slot_patient_id = pid, schedule_slot_id = selected_slot.schedule_slot_id)
                new_entry.slot_sch_appointment_rel = Appointment(date_time = selected_slot.date, doctor_id = doctor.doctor_id, patient_id = pid)
                new_entry.slot_sch_appointment_rel.t = Treatment(status = 'Booked')
                db.session.add(new_entry)
                db.session.commit()

                # notify patient
                notification = PatientDoctorNotifications(role = 'Doctor', message_type = 'Appointment Booking Confirmation', 
                                                          message_content = f'Hello, { patient.patient_name }! Your appointment with Dr. { doctor.doctor_name } is on { new_entry.date } ({ new_entry.s_sch.slot_name })'
                                                          ,m_doctor_id = doctor.doctor_id, m_patient_id = pid)
                db.session.add(notification)
                db.session.commit()
                return redirect('/admin')

    else:
        return redirect('/')


# admin - department: view - view_all - add - update - delete

@app.route('/department/<int:dept_id>', methods = ['GET'])
@login_required
def view_department(dept_id):
    if session['user_id']:
        if current_user.user_role != 'Admin':
            return 'You are not authorized'
        global date_today
        department = Department.query.filter(Department.department_id == dept_id).first()

        dept_doctors = department.doctors
        upcoming_dept_appointments = []
        for doc in dept_doctors:
            upcoming_dept_appointments += Appointment.query.filter(and_(Appointment.doctor_id == doc.doctor_id, Appointment.date_time >= date_today)).all()

        past_dept_appointments = []
        for doc in dept_doctors:
            past_dept_appointments += Appointment.query.filter(and_(Appointment.doctor_id == doc.doctor_id, Appointment.date_time <= date_today)).all()
        return render_template('admin/view_department.html', department = department, upcoming_dept_appointments = upcoming_dept_appointments, past_dept_appointments = past_dept_appointments, flag = True)
    else:
        return redirect('/')

@app.route('/all-dept', methods = ['GET'])
@login_required    
def view_all_departments():
    if session['user_id']:
        if current_user.user_role != 'Admin':
            return 'You are not authorized'
        departments = Department.query.filter(Department.status == None).all()
        deleted_departments = Department.query.filter(Department.status != None).all()
        return render_template('admin/view-all-dept.html', departments = departments, deleted_departments = deleted_departments)
    else:
        return redirect('/')

@app.route('/add_dept', methods = ['GET', 'POST'])
@login_required    
def add_department():
    if session['user_id']:
        if current_user.user_role != 'Admin':
            return 'You are not authorized'
        
        if request.method == 'GET':
            return render_template('admin/add_department.html')
        else:
            # validating name
            department_name = request.form['d_name']
            if validate_name(department_name) == None:
                return render_template('admin/add_department.html')

            if Department.query.filter(Department.department_name == department_name).first():
                return render_template('exists.html')

            # validating desc  
            department_description = request.form['d_desc']
            if validate_description(department_description) == None:
                return render_template('admin/add_department.html')
            
            # adding into db
            dept = Department(department_name = department_name, department_description = department_description, department_profile_picture = 'DefaultDepartment')
            db.session.add(dept)
            db.session.commit()
            return redirect('/admin')
    else:
        return redirect('/')

@app.route('/admin/department/update/<int:dept_id>', methods = ['GET', 'POST'])
@login_required    
def update_dept(dept_id):
    if session['user_id']:
        if current_user.user_role != 'Admin':
            return 'You are not authorized'
        if request.method == 'GET':
            department = db.get_or_404(Department, dept_id)
            return render_template('admin/update-department.html', department = department)
        else:
            department = db.get_or_404(Department, dept_id)
            department_name = request.form['dept_name']
            department_description = request.form['dept_description']

            # validation
            if validate_name(department_name) == None:
                return render_template('admin/add_department.html')
            
            if validate_description(department_description) == None:
                return render_template('admin/add_department.html')

            department.department_name = request.form['dept_name']
            department.department_description = request.form['dept_description']
            db.session.commit()
            return redirect('/admin')
    else:
        return redirect('/')

@app.route('/admin/department/delete/<int:dept_id>')
@login_required    
def delete_dept(dept_id):
    if session['user_id']:
        if current_user.user_role != 'Admin':
            return 'You are not authorized'
        department = db.get_or_404(Department, dept_id)
        department.status = 'Deleted by Admin'
        doctors = department.doctors
        for doctor in doctors:
            doctor = db.get_or_404(Doctor, doctor.doctor_id)
            doctor.status = 'Deleted by Admin'
        db.session.commit()
        return redirect('/admin')
    else:
        return redirect('/')
    
@app.route('/admin/department/undo-delete/<int:dept_id>')
@login_required    
def undo_delete_dept(dept_id):
    if session['user_id']:
        if current_user.user_role != 'Admin':
            return 'You are not authorized'
        department = db.get_or_404(Department, dept_id)
        department.status = None
        doctors = department.doctors
        for doctor in doctors:
            doctor = db.get_or_404(Doctor, doctor.doctor_id)
            doctor.status = None
        db.session.commit()
        return redirect('/admin')
    else:
        return redirect('/')
    
# admin - doctor: view - add - update - delete

@app.route('/admin/doctor/<int:did>', methods = ['GET'])
@login_required
def view_doctor(did):
    if session['user_id']:
        if current_user.user_role != 'Admin':
            return 'You are not authorized'
        doctor = db.get_or_404(Doctor, did)
        global date_today 
        past_appointments = Appointment.query.filter(and_(Appointment.date_time <= date_today, Appointment.doctor_id == doctor.doctor_id)).all()
        upcoming_appointments = Appointment.query.filter(and_(Appointment.date_time >= date_today, Appointment.doctor_id == doctor.doctor_id, Appointment.patient_id != None)).all()
        available_slots = SlotSchedules.query.filter(and_(SlotSchedules.date >= date_today, SlotSchedules.slot_doctor_id == doctor.doctor_id)).all()
        
        doctor_availability_list = []
        helper_list = []
        doctor_availability = SlotSchedules.query.filter(and_(SlotSchedules.slot_doctor_id == doctor.doctor_id, SlotSchedules.date >= date_today)).order_by(SlotSchedules.date, SlotSchedules.schedule_slot_id).all()
        for a in doctor_availability:
            if [a.date, a.s_sch.slot_name] not in helper_list:
                helper_list += [[a.date, a.s_sch.slot_name]]
                doctor_availability_list += [a]
        
        return render_template('admin/view_doctor.html', doctor = doctor,upcoming_appointments = upcoming_appointments, past_appointments = past_appointments, available_slots = available_slots
                               , doctor_availability_list = doctor_availability_list)
    else:
        return redirect('/')

@app.route('/admin/view-all-doctors', methods = ['GET'])
@login_required    
def view_all_doctors():
    if session['user_id']:
        if current_user.user_role != 'Admin':
            return 'You are not authorized'
        doctors = Doctor.query.filter(Doctor.status == None).all()
        deleted_doctors = Doctor.query.filter(Doctor.status != None).all()
        return render_template('admin/view-all-doctors.html', doctors = doctors, deleted_doctors = deleted_doctors)
    else:
        return redirect('/')

@app.route('/admin/doctor/add', methods = ['GET', 'POST'])
@login_required    
def add_doctor():
    if session['user_id']:
        if current_user.user_role != 'Admin':
            return 'You are not authorized'
        
        departments = Department.query.all()
        if request.method == 'GET':
            return render_template('admin/add_doctor.html', departments = departments)
        else:
            doctor_name = request.form['d_name']
            if validate_name(doctor_name) == None:
                return render_template('admin/add_doctor.html', departments = departments)

            if Doctor.query.filter(Doctor.doctor_name == doctor_name).first():
                return render_template('exists.html')

            # add as a user
            user_name = request.form['u_name']
            user_password = request.form['u_password']

            if validate_username(user_name) == None:
                return render_template('admin/add_doctor.html', departments = departments)
            if validate_password(user_password) == None:
                return render_template('admin/add_doctor.html', departments = departments)

            user = User(user_name = user_name, user_password = user_password, user_role = 'Doctor')
            db.session.add(user)

            # add as a doctor
            dept = request.form['dept']
            d = Department.query.filter(Department.department_name == dept).first()

            doctor_contact_number = request.form['contact_info']
            doctor_email = request.form['email']
            doctor_desc = request.form['desc']
            doctor_dob = request.form['d_dob']
            doctor_gender = request.form['gender']

            if validate_contact_number(doctor_contact_number) == None:
                return render_template('admin/add_doctor.html', departments = departments)
            if validate_email(doctor_email) == None:
                return render_template('admin/add_doctor.html', departments = departments)
            if validate_description(doctor_desc) == None:
                return render_template('admin/add_doctor.html', departments = departments)

            doctor_user_id = User.query.filter(User.user_name == user_name).first()
            
            photo = None
            if doctor_gender == 'Male':
                photo = 'MaleDoctor'
            else:
                photo = 'FemaleDoctor1'

            doctor = Doctor(doctor_name = doctor_name, department_id = d.department_id, doctor_contact_number = doctor_contact_number 
                            , doctor_email = doctor_email, doctor_desc = doctor_desc, doctor_gender = doctor_gender, 
                            doctor_dob = date.fromisoformat(doctor_dob), doctor_user_id = doctor_user_id.user_id,
                            doctor_profile_picture = photo)
            
            db.session.add(doctor)
            db.session.commit()
            return redirect('/admin')
    else:
        return redirect('/')

@app.route('/admin/doctor/update/<int:did>', methods = ['GET', 'POST'])
@login_required    
def update_doctor(did):
    if session['user_id']:
        if current_user.user_role != 'Admin':
            return 'You are not authorized'
        
        if request.method == 'GET':
            old_data = Doctor.query.filter_by(doctor_id = did).first()
            departments = Department.query.all()
            return render_template('admin/update_doctor.html',did = did, old_data = old_data, departments = departments)
        else:
            new_data = Doctor.query.filter_by(doctor_id = did).first()
            doctor_name = request.form['d_name']
            doctor_contact_number = request.form['contact_info']
            doctor_email = request.form['email']
            doctor_dob = request.form['d_dob']
            doctor_gender = request.form['gender']

            if validate_name(request.form['d_name']) == None:
                return render_template('admin/add_doctor.html', departments = departments)
            if validate_contact_number(request.form['contact_info']) == None:
                return render_template('admin/add_doctor.html', departments = departments)
            if validate_email(request.form['email']) == None:
                return render_template('admin/add_doctor.html', departments = departments)
            
            if request.form['d_dob'] != '':
                new_data.doctor_dob = date.fromisoformat(doctor_dob)

            dept = request.form['dept']
            d = Department.query.filter(Department.department_name == dept).first()
            new_data.department_id = d.department_id

            blacklisted = request.form['blacklist']
            if blacklisted == 'True':
                new_data.doctor_blacklisted = True
                notification = AdminDoctorNotifications(message_doctor_id = new_data.doctor_id,admin_doctor_message_type = 'Blacklisted Warning', admin_doctor_message_content = 'You have been temporarily blacklisted.')
                db.session.add(notification)
            else:
                new_data.doctor_blacklisted = False
            db.session.commit()
            return redirect('/admin')
    else:
        return redirect('/')

@app.route('/admin/doctor/delete/<int:did>', methods = ['GET'])
@login_required    
def delete_doctor(did):
    if session['user_id']:
        if current_user.user_role != 'Admin':
            return 'You are not authorized'
        doctor = db.get_or_404(Doctor, did)
        doctor.status = 'DeletedbyAdmin'
        db.session.commit()
        return redirect('/admin')
    else:
        return redirect('/')
    
@app.route('/admin/doctor/undo-delete/<int:did>', methods = ['GET'])
@login_required    
def undo_delete_doctor(did):
    if session['user_id']:
        if current_user.user_role != 'Admin':
            return 'You are not authorized'
        doctor = db.get_or_404(Doctor, did)
        doctor.status = None
        db.session.commit()
        return redirect('/admin')
    else:
        return redirect('/')

@app.route('/admin/doctor/check-availability/<int:did>', methods = ['GET'])
@login_required    
def check_availabilty(did):
    if session['user_id']:
        if current_user.user_role != 'Admin':
            return 'You are not authorized'
        doctor_slots = SlotSchedules.query.filter(and_(SlotSchedules.slot_doctor_id == did, SlotSchedules.date >= date_today)).order_by(SlotSchedules.date).all()
        doctor = db.get_or_404(Doctor, did)
        return render_template('admin/check-availability.html', doctor_slots = doctor_slots, doctor = doctor)
    else:
        return redirect('/')
    
# admin - patient: view - view_all - update - delete

@app.route('/admin/patient/<int:pid>', methods = ['GET'])
@login_required
def view_patient_admin(pid):
    if session['user_id']:
        if current_user.user_role != 'Admin':
            return 'You are not authorized'
        global date_today 
        patient = db.get_or_404(Patient, pid)
        past_appointments = Appointment.query.filter(and_(Appointment.date_time <= date_today, Appointment.patient_id == patient.patient_id)).all()
        age = relativedelta(date_today, patient.patient_dob)
        upcoming_appointments = Appointment.query.filter(and_(Appointment.date_time >= date_today, Appointment.patient_id == patient.patient_id)).all()

        return render_template('admin/view-patient.html', date_today = date_today, age = age, patient = patient, past_appointments = past_appointments, upcoming_appointments = upcoming_appointments)
    else:
        return redirect('/')

@app.route('/admin/patient/<int:pid>/send-message', methods = ['POST'])
@login_required    
def admin_send_patient_message(pid):
    if session['user_id']:
        if current_user.user_role != 'Admin':
            return 'You are not authorized'
        patient = db.get_or_404(Patient, pid)
        message = AdminPatientNotifications(message_patient_id = patient.patient_id, admin_patient_message_type = 'Message from Admin', admin_patient_message_content = request.form['message'])
        db.session.add(message)
        db.session.commit()
        return redirect('/admin')
    else:
        return redirect('/')

@app.route('/admin/view-all-patients', methods = ['GET'])
@login_required    
def view_all_patients():
    if session['user_id']:
        if current_user.user_role != 'Admin':
            return 'You are not authorized'
        patients = Patient.query.filter(Patient.status == None).all()
        deleted_patients = Patient.query.filter(Patient.status != None).all()
        return render_template('admin/view-all-patients.html', patients = patients, deleted_patients = deleted_patients)
    else:
        return redirect('/')

@app.route('/admin/patient/update/<int:pid>', methods = ['GET', 'POST'])
@login_required
def update_patient(pid):
    if session['user_id']:
        if current_user.user_role != 'Admin':
            return 'You are not authorized'
        old_data = db.get_or_404(Patient,pid)
        if request.method == 'GET':
            return render_template('admin/update_patient.html', pid = pid, old_data = old_data)
        else:
            new_data = Patient.query.filter(Patient.patient_id == pid).first()
            new_data.patient_name = request.form['p_name']
            new_data.patient_email = request.form['email']
            new_data.contact_info = request.form['contact_info']
            new_data.patient_gender = request.form['gender']
            patient_dob = request.form['p_dob']

            if validate_name(request.form['p_name']) == None:
                return render_template('admin/update_patient.html', pid = pid, old_data = old_data)
            if validate_contact_number(request.form['contact_info']) == None:
                return render_template('admin/update_patient.html', pid = pid, old_data = old_data)
            if validate_email(request.form['email']) == None:
                return render_template('admin/update_patient.html', pid = pid, old_data = old_data)

            if patient_dob != '':
                new_data.patient_dob = date.fromisoformat(request.form['d_dob'])
                
            blacklisted = request.form['blacklist']
            if blacklisted == 'True':
                new_data.patient_blacklisted = True
                notification = AdminPatientNotifications(message_patient_id = new_data.patient_id, admin_patient_message_type = 'Blacklisted Warning', admin_patient_message_content = 'You have been temporarily blacklisted.')
                db.session.add(notification)
            else:
                new_data.patient_blacklisted = False

            db.session.commit()
        return redirect('/admin')
    else:
        return redirect('/')

@app.route('/admin/patient/delete/<int:pid>', methods = ['GET'])
@login_required    
def delete_patient(pid):
    if session['user_id']:
        if current_user.user_role != 'Admin':
            return 'You are not authorized'
        patient = db.get_or_404(Patient, pid)
        patient.status = 'Deleted by Admin'
        db.session.commit()
        return redirect('/admin')
    else:
        return redirect('/')

@app.route('/admin/patient/undo-delete/<int:pid>', methods = ['GET'])
@login_required    
def undo_delete_patient(pid):
    if session['user_id']:
        if current_user.user_role != 'Admin':
            return 'You are not authorized'
        patient = db.get_or_404(Patient, pid)
        patient.status = None
        db.session.commit()
        return redirect('/admin')
    else:
        return redirect('/')
    
# admin - search 

@app.route('/admin/search', methods = ['POST'])
@login_required
def search():
    if session['user_id']:
        if current_user.user_role != 'Admin':
            return 'You are not authorized'
        if request.method == 'POST':
            input_value = request.form['query']

            if input_value.isnumeric(): # input value is ID
                appointments_by_patient_name = []
                appointments_by_doctor_name = []

                patients = Patient.query.filter(or_(Patient.patient_name.like(f'%{input_value}%'), Patient.contact_info.like(f'%{input_value}%'), Patient.patient_id.like(f'%{input_value}%'))).all()
                for patient in patients:
                    appointments_by_patient_name += Appointment.query.filter(Appointment.patient_id == patient.patient_id).all()

                doctors = Doctor.query.filter(or_(Doctor.doctor_name.like(f'%{input_value}%'), Doctor.doctor_contact_number.like(f'%{input_value}%'), Doctor.doctor_id.like(f'%{input_value}%'))).all()
                for doctor in doctors:
                    appointments_by_doctor_name += Appointment.query.filter(Appointment.doctor_id == doctor.doctor_id).all()

                departments = Department.query.filter(or_(Department.department_id.like(f'%{input_value}%'), Department.department_name.like(f'%{input_value}%'))).all()
                return render_template('admin/search.html', input_value =  input_value, patients = patients, doctors = doctors, departments = departments, 
                                        appointments_by_patient_name = appointments_by_patient_name, appointments_by_doctor_name = appointments_by_doctor_name)

            else:
                patients = []
                doctors = []
                departments = []
                appointments_by_doctor_name = []
                appointments_by_patient_name = []

                patients = Patient.query.filter(Patient.patient_name.like(f'%{input_value}%')).all()
                if patients != []:
                    for patient in patients:
                        appointments_by_patient_name = Appointment.query.filter(Appointment.patient_id == patient.patient_id).all()

                doctors = Doctor.query.filter(Doctor.doctor_name.like(f'%{input_value}%')).all()
                if doctors != []:
                    for doctor in doctors:
                        appointments_by_doctor_name = Appointment.query.filter(Appointment.doctor_id == doctor.doctor_id).all()

                departments = Department.query.filter(Department.department_name.like(f'%{input_value}%')).all()
                if departments != []:
                    for department in departments:
                        doctors = department.doctors
                        appointments_by_doctor_name = []
                        for doc in doctors:
                            appointments_by_doctor_name += Appointment.query.filter(Appointment.doctor_id == f'{doc.doctor_id}').all()

                return render_template('admin/search.html', input_value = input_value, patients = patients, doctors = doctors, departments = departments, 
                                    appointments_by_patient_name = appointments_by_patient_name, appointments_by_doctor_name = appointments_by_doctor_name)   
    else:
        return redirect('/')
        
@app.route('/admin/notification-page', methods = ['GET'])
@login_required
def admin_notification_page():
    if session['user_id']:
        if current_user.user_role != 'Admin':
            return 'You are not authorized'

        unread_patient_notifications  = AdminPatientNotifications.query.filter(AdminPatientNotifications.admin_message_recieved == 0, AdminPatientNotifications.role == 'Patient').all()
        read_patient_notifications = AdminPatientNotifications.query.filter(AdminPatientNotifications.admin_message_recieved == 1, AdminPatientNotifications.role == 'Patient').all()
        unread_doctor_notifications  = AdminDoctorNotifications.query.filter(AdminDoctorNotifications.admin_message_recieved == 0, AdminDoctorNotifications.role == 'Patient').all()
        read_doctor_notifications  = AdminDoctorNotifications.query.filter(AdminDoctorNotifications.admin_message_recieved == 1, AdminDoctorNotifications.role == 'Patient').all()

        # Mark notifications as read
        for n in unread_patient_notifications:
            n.admin_message_recieved = 1

        for n in unread_doctor_notifications:
            n.admin_message_recieved = 1

        db.session.commit()
        return render_template('/admin/notification-page.html', unread_patient_notifications = unread_patient_notifications, read_patient_notifications = read_patient_notifications,
                               unread_doctor_notifications = unread_doctor_notifications, read_doctor_notifications = read_doctor_notifications)

# Find Doctor   

@app.route('/doctor/<int:did>', methods = ['GET'])
@login_required 
def doctor_dashboard(did):
    if session['user_id']:
        if current_user.user_role != 'Doctor':
            return 'You are not authorized'
        if current_user.doctor_relationship.doctor_id != did:
            return 'You can not view this'
        if request.method == 'GET':
            global date_today
            patients_list = []
            show_patients = []
            helper_lst = []
            availabilty_list = []
            appointments_today = []
            appointments_this_week = []
            slot_patients_dict = {}
            
            patients = Appointment.query.filter(Appointment.doctor_id == did).all()
            availabilty = SlotSchedules.query.filter(and_(SlotSchedules.slot_doctor_id == did, SlotSchedules.date >= date_today)).order_by(SlotSchedules.date, SlotSchedules.schedule_slot_id).all()

            # patients who have booked an appointment with doctor atleast once
            for a in patients:
                if a.p_ref.patient_name not in patients_list:
                    patients_list += [a.p_ref.patient_name]
                    show_patients += [a]

            # group slots by date and time, so count of patients can be shown
            for a in availabilty:
                if [a.date, a.s_sch.slot_name] not in helper_lst:
                    helper_lst += [[a.date, a.s_sch.slot_name]]
                    availabilty_list += [a]

            # how many patients are scheduled to see the doctor in a slot
            for a in availabilty:
                if a.date not in slot_patients_dict.keys():
                    slot_patients_dict[a.date] = {1:0, 2:0, 3:0}
                if a.slot_patient_id == None:
                    slot_patients_dict[a.date][a.schedule_slot_id] += 0
                else:
                    slot_patients_dict[a.date][a.schedule_slot_id] += 1

            # appointments scheduled today
            appointments_today = SlotSchedules.query.filter(and_(SlotSchedules.date == date_today, SlotSchedules.slot_doctor_id == did, SlotSchedules.slot_patient_id != None)).all()
            
            # appointments scheduled this week 
            list_of_next_7_dates = [(date_today + timedelta(days = i)) for i in range(1,8)]
            for d in list_of_next_7_dates:
                appointments_this_week += SlotSchedules.query.filter(and_(SlotSchedules.date == d, SlotSchedules.slot_doctor_id == did,  SlotSchedules.slot_patient_id != None)).order_by(SlotSchedules.date, SlotSchedules.schedule_slot_id).all()

            # past appointments
            past_appointments = SlotSchedules.query.filter(and_(SlotSchedules.slot_doctor_id == did, SlotSchedules.date < date_today, SlotSchedules.slot_patient_id != None)).all()

            return render_template('doctor/doctor-dashboard.html', show_patients = show_patients, availabilty_list = availabilty_list, slot_patients_dict = slot_patients_dict, 
                                appointments_today = appointments_today, appointments_this_week = appointments_this_week, past_appointments = past_appointments)
    else:
        return redirect('/')

@app.route('/doctor/<int:did>/doctor-profile', methods = ['GET'])
@login_required 
def view_doctor_profile(did):
    if session['user_id']:
        if current_user.user_role != 'Doctor':
            return 'You are not authorized'
        if current_user.doctor_relationship.doctor_id != did:
            return 'You can not view this'
        return render_template('doctor/profile.html')
    else:
        return redirect('/')

@app.route('/doctor/<int:did>/doctor-profile/update', methods = ['GET', 'POST'])
@login_required 
def update_doctor_profile(did):
    if session['user_id']:
        if current_user.user_role != 'Doctor':
            return 'You are not authorized'
        if current_user.doctor_relationship.doctor_id != did:
            return 'You can not view this'
        
        if request.method == 'GET':
            return render_template('doctor/update_profile.html')
        else:
            user_name = request.form['u_name']
            user_password = request.form['u_password']
            doctor_name = request.form['d_name']
            doctor_desc = request.form['descprition']
            doctor_contact_number = request.form['contact_info']
            user_name = request.form['u_name']
            user_password = request.form['u_password']

            # validation
            if validate_username(user_name) == None:
                return render_template('doctor/update_profile.html')
            if validate_password(user_password) == None:
                return render_template('doctor/update_profile.html')
            if validate_name(doctor_name) == None:
                return render_template('doctor/update_profile.html')
            if validate_description(doctor_desc) == None:
                return render_template('doctor/update_profile.html')
            if validate_contact_number(doctor_contact_number) == None:
                return render_template('doctor/update_profile.html')

            doctor = db.get_or_404(Doctor, current_user.doctor_relationship.doctor_id)
            doctor.d.user_name = request.form['u_name']
            doctor.d.user_password = request.form['u_password']
            doctor.doctor_name = request.form['d_name']
            doctor.doctor_desc = request.form['descprition']
            doctor.doctor_email = request.form['email']
            doctor.doctor_contact_number = request.form['contact_info']
            db.session.commit()
            return redirect(f'/doctor/{did}')
    else:
        return redirect('/')

@app.route('/doctor/<int:did>/send-message-to-admin', methods = ['GET', 'POST'])
@login_required
def doctor_send_admin_messages(did):
    if session['user_id']:
        if current_user.user_role != 'Doctor':
            return 'You are not authorized'
        if current_user.doctor_relationship.doctor_id != did:
            return 'You can not view this'
        global date_today
        if request.method == 'GET':
            return render_template('doctor/admin_notify_profile_change.html', date_today = date_today)
        else:
            message_content = request.form['message']
            message = AdminDoctorNotifications(admin_doctor_message_type = f'From Dr. {current_user.doctor_relationship.doctor_name}', admin_doctor_message_content = message_content)
            db.session.add(message)
            db.session.commit()
            return redirect(f'/doctor/{did}')


@app.route('/doctor/view-patient/<int:pid>/<int:did>', methods = ['GET'])
@login_required 
def view_patient_doctor(pid, did):
    if session['user_id']:
        if current_user.user_role != 'Doctor':
            return 'You are not authorized'
        if current_user.doctor_relationship.doctor_id != did:
            return 'You can not view this'
        global date_today

        patient = Appointment.query.filter(and_(Appointment.doctor_id == did, Appointment.patient_id == pid)).first()
        past_appointments = Appointment.query.filter(and_(Appointment.doctor_id == did, Appointment.patient_id == pid, Appointment.date_time < date_today)).order_by(Appointment.date_time).all()
        all_past_appointments = Appointment.query.filter(and_(Appointment.patient_id == pid, Appointment.date_time < date_today)).order_by(Appointment.date_time).all()
        upcoming_appointments = Appointment.query.filter(and_(Appointment.doctor_id == did, Appointment.patient_id == pid, Appointment.date_time >= date_today)).all()
        age = relativedelta(date_today, patient.p_ref.patient_dob)
        
        if past_appointments == []:
            last_visit = '--'
        elif len(past_appointments) == 1:
            last_visit = past_appointments[0].date_time
        else:
            last_visit = past_appointments[-1].date_time
        print(last_visit)

        return render_template('doctor/view-patient.html', patient = patient, past_appointments = past_appointments, last_visit = last_visit, upcoming_appointments = upcoming_appointments, all_past_appointments = all_past_appointments, age = age, date_today = date_today)
    else:
        return redirect('/')

@app.route('/doctor/<int:did>/patient/<int:pid>/send-message', methods = ['POST'])
@login_required    
def doctor_send_patient_message(did, pid):
    if session['user_id']:
        if current_user.user_role != 'Doctor':
            return 'You are not authorized'
        if current_user.doctor_relationship.doctor_id != did:
            return 'You can not view this'
        
        patient = db.get_or_404(Patient, pid)
        message = PatientDoctorNotifications(m_patient_id = patient.patient_id, m_doctor_id = current_user.doctor_relationship.doctor_id, message_type = f'Message from Dr. { current_user.doctor_relationship.doctor_name }', 
                                             message_content = request.form['message'], role = 'Doctor')
        db.session.add(message)
        db.session.commit()
        return redirect(f'/doctor/{did}')
    else:
        return redirect('/')

@app.route('/doctor/patients-by-slot/<int:did>/<int:sid>', methods = ['GET'])
@login_required 
def view_patients_by_slots(did, sid):
    if session['user_id']:
        if current_user.user_role != 'Doctor':
            return 'You are not authorized'
        if current_user.doctor_relationship.doctor_id != did:
            return 'You can not view this'
        
        slot = SlotSchedules.query.filter(SlotSchedules.schedule_id == sid).first()
        slot_date = slot.date
        all_appointments = SlotSchedules.query.filter(and_(SlotSchedules.date == slot_date, SlotSchedules.schedule_slot_id == slot.schedule_slot_id, SlotSchedules.slot_patient_id != None)).all()
        return render_template('doctor/view-patients-by-slot.html', slot = slot, all_appointments = all_appointments)
    else:
        return redirect('/')

@app.route('/doctor/ongoing_appointment/<int:did>/<int:aid>', methods = ['GET', 'POST'])
@login_required 
def ongoing_appointments(did, aid):
    if session['user_id']:
        if current_user.user_role != 'Doctor':
            return 'You are not authorized'
        if current_user.doctor_relationship.doctor_id != did:
            return 'You can not view this'
        global date_today
        appointment = SlotSchedules.query.filter(SlotSchedules.schedule_id == aid).first()
        patient = Patient.query.filter(Patient.patient_id == appointment.slot_patient_id).first()
        past_appointments = Appointment.query.filter(and_(Appointment.doctor_id == did, Appointment.patient_id == patient.patient_id, Appointment.date_time <= date_today)).order_by(Appointment.date_time).all()
        last_visit = '--'
        age = relativedelta(date_today, patient.patient_dob) 

        if past_appointments == []:
            last_visit = '--'
        elif len(past_appointments) == 1:
            last_visit = past_appointments[0].date_time
        else:
            last_visit = past_appointments[-1].date_time
        if request.method == 'GET':
            return render_template('doctor/ongoing_treatment.html', patient = patient, appointment = appointment, last_visit = last_visit, age = age)
        else:
            treatment_details = request.form
            td = treatment_details.to_dict(flat=False)
            appointment = SlotSchedules.query.filter(SlotSchedules.schedule_id == aid).first()
            diagnosis = td['diagnosis'][0]
            notes = td['notes'][0]
            prescription = td['prescription'][0]
            tests = td['tests'][0]

            # validation
            if validate_treatment_details(diagnosis) == None:
                print('Problem 1')
                return render_template('doctor/ongoing_treatment.html', patient = patient, appointment = appointment, last_visit = last_visit, age = age)
            if validate_treatment_details(notes) == None:
                print('Problem 2')
                return render_template('doctor/ongoing_treatment.html', patient = patient, appointment = appointment, last_visit = last_visit, age = age)
            if validate_treatment_details(prescription) == None:
                print('Problem 3')
                return render_template('doctor/ongoing_treatment.html', patient = patient, appointment = appointment, last_visit = last_visit, age = age)
            if validate_treatment_details(tests) == None:
                print('Problem 4')
                return render_template('doctor/ongoing_treatment.html', patient = patient, appointment = appointment, last_visit = last_visit, age = age)

            appointment.slot_sch_appointment_rel.t.diagnosis = td['diagnosis'][0]
            appointment.slot_sch_appointment_rel.t.notes = td['notes'][0]
            appointment.slot_sch_appointment_rel.t.prescription = td['prescription'][0]
            appointment.slot_sch_appointment_rel.t.tests = td['tests'][0]

            diet_type = []

            for k in td:
                if k == 'non-dairy':
                    diet_type += [k]
                elif k == 'dairy':
                    diet_type += [k]
                elif k == 'clear-liquid':
                    diet_type += [k]
                elif k == 'liquid':
                    diet_type += [k]
                elif k == 'restricted-normal':
                    diet_type += [k]

            final_diet = ''
            if len(diet_type) > 1:
                for d in diet_type:
                    if diet_type.index(d) != len(diet_type)-1:
                        final_diet += d + ', '
                    else:
                        final_diet += d

            appointment.slot_sch_appointment_rel.t.treatment_dn = DieticianNotes(status = 'Pending', doctor_instructions = final_diet, patient_id = patient.patient_id, treatment_id = appointment.slot_sch_appointment_rel.t.treatment_id)
            db.session.commit()

            return redirect(f'/doctor/{did}')
    else:
        return redirect('/')

@app.route('/doctor/view-appointment/<int:did>/<int:tid>', methods = ['GET'])
@login_required
def doctor_view_appointment(tid, did):
    if session['user_id']:
        if current_user.user_role != 'Doctor':
            return 'You are not authorized'
        if current_user.doctor_relationship.doctor_id != did:
            return 'You can not view this'
        global date_today
        treatment = Treatment.query.filter(Treatment.treatment_id == tid).first()
        patient = Patient.query.filter(Patient.patient_id == treatment.ap[0].p_ref.patient_id).first()
        age = relativedelta(date_today, patient.patient_dob)
        dietician_notes = DieticianNotes.query.filter(DieticianNotes.treatment_id == treatment.treatment_id).first()
        print(dietician_notes)
        return render_template('doctor/view-appointment.html', treatment = treatment, patient = patient, dietician_notes = dietician_notes, date_today = date_today, age = age)

@app.route('/doctor/update-treatment-details/<int:did>/<int:tid>', methods = ['GET', 'POST'])
@login_required 
def update_treatment_details(tid, did):
    if session['user_id']:
        if current_user.user_role != 'Doctor':
            return 'You are not authorized'
        if current_user.doctor_relationship.doctor_id != did:
            return 'You can not view this'
        treatment = Treatment.query.filter(Treatment.treatment_id == tid).first()
        list_of_options = ['Completed', 'Booked', 'Cancelled'] 
        treatment_status = treatment.status

        dn = DieticianNotes.query.filter(DieticianNotes.treatment_id == treatment.treatment_id).first()
        if dn != None:
            doctor_instructions = treatment.treatment_dn.doctor_instructions
            di = []
            for a in doctor_instructions.split(','):
                di += [a.strip()]

        if request.method == 'GET':
            return render_template('doctor/update-treatment-details.html', treatment = treatment, list_of_options = list_of_options, treatment_status = treatment_status, di = di)
        else:
            new_data = Treatment.query.filter(Treatment.treatment_id == tid).first()
            diagnosis = request.form['diagnosis']
            status = request.form['status']
            prescription = request.form['prescription']
            notes = request.form['notes']
            tests = request.form['tests']

            treatment_details = request.form
            td = treatment_details.to_dict(flat=False)

            # validation
            if validate_treatment_details(diagnosis) == None:
                return render_template('doctor/update-treatment-details.html', treatment = treatment, list_of_options = list_of_options, treatment_status = treatment_status, di = di)
            if validate_treatment_details(notes) == None:
                return render_template('doctor/update-treatment-details.html', treatment = treatment, list_of_options = list_of_options, treatment_status = treatment_status, di = di)
            if validate_treatment_details(prescription) == None:
                return render_template('doctor/update-treatment-details.html', treatment = treatment, list_of_options = list_of_options, treatment_status = treatment_status, di = di)
            if validate_treatment_details(tests) == None:
                return render_template('doctor/update-treatment-details.html', treatment = treatment, list_of_options = list_of_options, treatment_status = treatment_status, di = di)

            new_data.diagnosis = request.form['diagnosis']
            new_data.status = request.form['status']
            new_data.prescription = request.form['prescription']
            new_data.notes = request.form['notes']
            new_data.tests = request.form['tests']

            diet_type = []

            for k in td:
                if k == 'non-dairy':
                    diet_type += [k]
                elif k == 'dairy':
                    diet_type += [k]
                elif k == 'clear-liquid':
                    diet_type += [k]
                elif k == 'liquid':
                    diet_type += [k]
                elif k == 'restricted-normal':
                    diet_type += [k]

            final_diet = ''
            if len(diet_type) > 1:
                for d in diet_type:
                    if diet_type.index(d) != len(diet_type)-1:
                        final_diet += d + ', '
                    else:
                        final_diet += d
            else:
                final_diet = diet_type[0]

            dn.status = 'Pending'
            dn.doctor_instructions = final_diet

            # notify patient
            message = PatientDoctorNotifications(message_content = f"Hi, Dr. { current_user.doctor_relationship.doctor_name } has updated your treatment details.", 
                                                 message_type = 'Treatment Details', role = 'Doctor', m_doctor_id = f'{ current_user.user_id }', 
                                                 m_patient_id = new_data.ap[0].p_ref.patient_id, appointment_id = new_data.ap[0].appointment_id, treatment_id = treatment.treatment_id)
            db.session.add(message)

            db.session.commit()
            return redirect(f'/doctor/{did}')
    else:
        return redirect('/')
    
@app.route('/doctor/cancel-appointment/<int:did>/<int:tid>', methods = ['GET'])
@login_required 
def cancel_appointment_doctor(tid, did):
    if session['user_id']:
        if current_user.user_role != 'Doctor':
            return 'You are not authorized'
        if current_user.doctor_relationship.doctor_id != did:
            return 'You can not view this'
        treatment = Treatment.query.filter(Treatment.treatment_id == tid).first()
        appointment = treatment.ap[0].appointment_sch
        doctor = current_user.doctor_relationship.doctor_id
        patient = treatment.ap[0].p_ref
        if treatment.status == 'Booked':
            treatment.status = 'Cancelled'
        # notify the patient that the doctor has cancelled the appointment
        notification = PatientDoctorNotifications(role = 'Doctor', m_doctor_id = appointment.slot_doctor_id, m_patient_id = patient.patient_id,
                                                  message_type = 'Appointment Cancelled', 
                                                  message_content = f'Your appointment scheduled on { appointment.date } ({ appointment.s_sch.slot_name }) with Dr. { doctor.doctor_name } was cancelled.')
        db.session.add(notification)
        db.session.commit()
        return redirect(f"/doctor/view-patient/{ patient.patient_id }/{ doctor.doctor_id }")
    else:
        return redirect('/')

@app.route('/doctor/<int:did>/notification-page')
@login_required 
def doctor_notification_page(did):
    if session['user_id']:
        if current_user.user_role != 'Doctor':
            return 'You are not authorized'
        if current_user.doctor_relationship.doctor_id != did:
            return 'You can not view this'
        global date_today      
        unread_admin_notifications = AdminDoctorNotifications.query.filter(AdminDoctorNotifications.message_doctor_id == did, AdminDoctorNotifications.doctor_message_recieved == 0).order_by(desc(AdminDoctorNotifications.message_date_time)).all()
        read_admin_notifications = AdminDoctorNotifications.query.filter(AdminDoctorNotifications.message_doctor_id == did, AdminDoctorNotifications.doctor_message_recieved == 1).order_by(desc(AdminDoctorNotifications.message_date_time)).all()
        unread_patient_notifications = PatientDoctorNotifications.query.filter(PatientDoctorNotifications.m_doctor_id == did, PatientDoctorNotifications.role == 'Patient', PatientDoctorNotifications.doctor_message_recieved == 0).order_by(desc(PatientDoctorNotifications.message_date_time)).all() 
        read_patient_notifications = PatientDoctorNotifications.query.filter(PatientDoctorNotifications.m_doctor_id == did, PatientDoctorNotifications.role == 'Patient', PatientDoctorNotifications.doctor_message_recieved == 1).order_by(desc(PatientDoctorNotifications.message_date_time)).all() 
        dietetics_dept = Department.query.filter(Department.department_name == 'Dietetics').first()
        
        # marking unread notifications as read
        for message in unread_admin_notifications:
            message.doctor_message_recieved = 1
        
        for message in unread_patient_notifications:
            message.doctor_message_recieved = 1
        db.session.commit()

        return render_template('doctor/doctor_notification_page.html', date_today = date_today, unread_admin_notifications = unread_admin_notifications, read_admin_notifications = read_admin_notifications, read_patient_notifications = read_patient_notifications, unread_patient_notifications = unread_patient_notifications, dietetics_dept = dietetics_dept)
    else:
        return redirect('/')

@app.route('/doctor/provide_slots/<int:did>', methods = ['GET', 'POST'])
@login_required 
def provide_availability(did):
    if session['user_id']:
        if current_user.user_role != 'Doctor':
            return 'You are not authorized'
        if current_user.doctor_relationship.doctor_id != did:
            return 'You can not view this'
        if request.method == 'GET':
            doctor = db.get_or_404(Doctor, did)
            list_of_next_7_dates = [(date_today + timedelta(days = i)) for i in range(8)]
            slots = Slot.query.all()

            appointments_dict = {}
            for d in list_of_next_7_dates:
                appointments_dict[d] = {}
                for s in slots:
                    query = SlotSchedules.query.filter(SlotSchedules.date == d, SlotSchedules.schedule_slot_id == s.slot_id, SlotSchedules.slot_doctor_id == doctor.doctor_id).first()
                    appointments_dict[d][s] = query
            return render_template('/doctor/provide_availability.html', appointments_dict = appointments_dict, doctor = doctor, slots = slots, list_of_next_7_dates = list_of_next_7_dates)
        
        else:
            doctor = db.get_or_404(Doctor, did)
            availability = request.form
            a = availability.to_dict(flat=False)
            print(a)
            slots = Slot.query.all()

            past_state = SlotSchedules.query.filter(and_(SlotSchedules.date > date_today, SlotSchedules.slot_doctor_id == did)).all()
            if past_state != []: #updating availability
                past_state_list = []
                for p in past_state:
                    past_state_list += [(str(p.schedule_slot_id), p.date.strftime("%Y-%m-%d"))]

                present_state_list = []
                present_state = a
                for pr in present_state.keys():
                    for i in range(len(present_state[pr])):
                        present_state_list += [(pr, present_state[pr][i])]

                unchanged_list = []
                for i in past_state_list:
                    if i in present_state_list:
                        unchanged_list += [i]

                cancel_list = [] #mark an existing appointments as cancelled
                for i in past_state_list:
                    if i not in present_state_list:
                        cancel_list += [i]

                cancel_appointments = []
                for c in cancel_list:
                    cancel_appointments += SlotSchedules.query.filter(and_(SlotSchedules.slot_doctor_id == did, SlotSchedules.date == c[1], SlotSchedules.schedule_slot_id == c[0])).all()

                    delete_slots_with_no_patients = SlotSchedules.query.filter(and_(SlotSchedules.slot_doctor_id == did, SlotSchedules.date == c[1], SlotSchedules.schedule_slot_id == c[0]), SlotSchedules.slot_patient_id == None).all()
                    for d in delete_slots_with_no_patients:
                        db.session.delete(d)

                for c in cancel_appointments:
                    c.status = 'Cancelled'

                new_list = [] #query into db
                for i in present_state_list:
                    if i not in past_state_list:
                        new_list += [i]

                for n in new_list:
                    x = n[1]
                    y = int(x[0:4])
                    m = int(x[5:7])
                    d = int(x[8:10])
                    slot_date = datetime.date(y,m,d)
                    new_entry = SlotSchedules(date = slot_date, slot_doctor_id = did, schedule_slot_id = n[0])
                    db.session.add(new_entry)
                db.session.commit()

            else: # new data 
                # check if there is any patient in waiting list
                waiting_list = AvailibilityNotifications.query.filter(AvailibilityNotifications.notif_doctor_id == did, AvailibilityNotifications.starting_date >= date_today).all()
                for s in a.keys():
                    slot_id = Slot.query.filter(Slot.slot_id == s).first()
                    for x in a[s]:
                        y = int(x[0:4])
                        m = int(x[5:7])
                        d = int(x[8:10])
                        slot_date = datetime.date(y,m,d)
                        slot = SlotSchedules(slot_doctor_id = did, schedule_slot_id = slot_id.slot_id, date = slot_date)
                        db.session.add(slot)

                        if waiting_list != []:
                            for row in waiting_list:
                                if slot.date == row.starting_date:
                                    row.doctor_available = True
            db.session.commit()
            return redirect(f'/doctor/{ doctor.doctor_id }')
    else:
        return redirect('/')

@app.route('/doctor/<int:did>/search', methods = ['POST'])
@login_required 
def search_doctor_dash(did):
    if session['user_id']:
        if current_user.user_role != 'Doctor':
            return 'You are not authorized'
        if current_user.doctor_relationship.doctor_id != did:
            return 'You can not view this'
        if request.method == 'POST':
            doctor = db.get_or_404(Doctor, did)
            input_value = request.form['query']

            # appointments_by_doctor = Appointment.query.filter(Appointment.doctor_id == did).all()
            # patients = [] #list of all patients which has booked an appointment with the doctor
            # helper_list = [] 
            # search_function = []
            # appointments_by_patient_name = []

            # doctors = Doctor.query.filter(or_(Doctor.doctor_name.like(f'%{input_value}%'), Doctor.doctor_contact_number.like(f'%{input_value}%'))).all()
            # departments = Department.query.filter(Department.department_name.like(f'%{input_value}%')).all()

            # for p in appointments_by_doctor:
            #     if p.p_ref.patient_name not in helper_list:
            #         patients += [p]
            #         helper_list += [p.p_ref.patient_name]

            # for p in patients:
            #     search_list = Patient.query.filter(or_(Patient.patient_name.like(f'%{input_value}%'), Patient.contact_info.like(f'%{input_value}%'))).all()
            #     if search_list != []:
            #         search_function += search_list
            
            # for p in search_function:
            #     appointments_by_patient_name += Appointment.query.filter(Appointment.patient_id == p.patient_id).all()

            appointments_by_doctor = Appointment.query.filter(Appointment.doctor_id == did).all()
            patients = [] #list of all patients which has booked an appointment with the doctor
            helper_list = [] 
            search_function = []
            appointments_by_patient_name = []


            doctors = Doctor.query.filter(or_(Doctor.doctor_name.like(f'%{input_value}%'), Doctor.doctor_contact_number.like(f'%{input_value}%'))).all()
            departments = Department.query.filter(Department.department_name.like(f'%{input_value}%')).all()

            # doctor can only search for his patients
            for p in appointments_by_doctor:
                if p.p_ref.patient_name not in helper_list:
                    patients += [p]
                    helper_list += [p.p_ref.patient_name]

            helper_list = []

            for p in patients:
                search_list = Patient.query.filter(or_(Patient.patient_name.like(f'%{input_value}%'), Patient.contact_info.like(f'%{input_value}%'))).all()
                if search_list != None:
                    if p.p_ref.patient_name not in helper_list:
                        search_function += search_list
                        helper_list += [p.p_ref.patient_name]

            for p in search_list:
                    appointments_by_patient_name += Appointment.query.filter(Appointment.patient_id == p.patient_id, Appointment.doctor_id == did).all()

            return render_template('doctor/search_doctor.html', input_value = input_value, search_function = search_function, doctor = doctor, appointments_by_patient_name = appointments_by_patient_name, doctors = doctors, departments = departments, search_list = search_list)
    else:
        return redirect('/')
    
# Find Dietetics

@app.route('/dietetics/doctor/<int:did>')
def dietetics_dashboard(did):
    pending_dn = DieticianNotes.query.filter(DieticianNotes.status == 'Pending').all()
    completed_dn = DieticianNotes.query.filter(DieticianNotes.status != 'Pending').all()
    return render_template('DieticianDash/dietician_dashboard.html', pending_dn = pending_dn, completed_dn = completed_dn)

@app.route('/dietetician_notes/<int:did>/<int:dn_id>', methods = ['GET', 'POST'])
def provide_dietician_notes(did, dn_id):
    dn = db.get_or_404(DieticianNotes, dn_id)
    patient = db.get_or_404(Patient, dn.patient_id)
    age = relativedelta(date_today, patient.patient_dob)
    return render_template('DieticianDash/provide_notes.html', dn = dn, patient = patient, age = age)

# Find Patient

# dashborad - register - view_profile - update_profile 
# book_appointment - confirm_appointment - cancel-appointment - reschedule-appointment
# notification-d-availability - notification_page - tymessage - send-notific-to-doctor
# view-doctor - view-dept - search

@app.route('/patient/<int:pid>', methods = ['GET'])
@login_required
def patient_dashboard(pid):
    if session.get('user_id'):
        if current_user.user_role != 'Patient':
            return 'You are not authorized'
        if current_user.patient_relationship.patient_id != pid:
            return 'You can not view this'
        if request.method == 'GET':
            global date_today
            appointments_this_week = []
            doctors = Doctor.query.all()
            departments = Department.query.filter(Department.department_name != 'Dietetics').all()
            past_appointments = SlotSchedules.query.filter(and_(SlotSchedules.slot_patient_id == pid, SlotSchedules.date < date_today)).order_by(desc(SlotSchedules.date)).all()
            appointments_today = SlotSchedules.query.filter(and_(SlotSchedules.date == date_today, SlotSchedules.slot_patient_id == pid)).order_by(SlotSchedules.schedule_slot_id).all()
            list_of_next_7_dates = [(date_today + timedelta(days = i)) for i in range(1,8)]
            for d in list_of_next_7_dates:
                appointments_this_week += SlotSchedules.query.filter(and_(SlotSchedules.date == d, SlotSchedules.slot_patient_id == pid)).order_by(SlotSchedules.date, SlotSchedules.schedule_slot_id).all()
            
            # dynamically changing status if the date of the appointment has passed
            for p in past_appointments:
                if p.date >= date_today:
                    p.slot_sch_appointment_rel.t.status == 'Completed'
            db.session.commit()
            return render_template('patient/patient-dashboard.html', past_appointments = past_appointments, appointments_today = appointments_today, doctors = doctors, appointments_this_week = appointments_this_week, departments = departments)
    else:
        return redirect('/')

@app.route('/register', methods = ['GET', 'POST'])
@login_required
def register_patient():
    if request.method == 'GET':
        return render_template('patient/register_patient.html')
    else:
        patient_name = request.form['p_name']
        if validate_name(patient_name) == None:
            return render_template('patient/register_patient.html')

        if Patient.query.filter(Patient.patient_name == patient_name).first():
            return render_template('exists.html') 
        
        # add as a user
        user_name = request.form['u_name']
        user_password = request.form['u_password']
        if validate_username(user_name) == None:
            return render_template('patient/register_patient.html') 
        if validate_password(user_password) == None:
            return render_template('patient/register_patient.html')

        user = User(user_name = user_name, user_password = user_password, user_role = 'Patient')
        db.session.add(user)

        # add as a patient
        contact_info = request.form['contact_info']
        patient_email = request.form['email']
        patient_dob = request.form['p_age']
        patient_gender = request.form['gender']
        patient_height = request.form['height']
        patient_weight = request.form['weight']

        if validate_contact_number(contact_info) == None:
            return render_template('patient/register_patient.html')
        if validate_email(patient_email) == None:
            return render_template('patient/register_patient.html')
        if validate_only_text_fields(str(patient_height)) == False:
            return render_template('patient/register_patient.html')
        if validate_only_text_fields(str(patient_weight)) == False:
            return render_template('patient/register_patient.html')

        patient_user_id = User.query.filter(User.user_name == user_name).first()
        patient = Patient(patient_name = patient_name, contact_info = contact_info, patient_email = patient_email, patient_user_id = patient_user_id.user_id, 
                          patient_dob = date.fromisoformat(patient_dob), patient_gender = patient_gender, patient_height = patient_height, patient_weight = patient_weight)
        db.session.add(patient)
        db.session.commit()

        welcome_notification = AdminPatientNotifications(admin_patient_message_type = 'Welcome Message', admin_patient_message_content = f'Hello, { user.patient_relationship.patient_name }! Thank you for choosing LDH Hospital.', message_patient_id = user.patient_relationship.patient_id)
        db.session.add(welcome_notification)
        return redirect(f'/patient/{ patient_user_id.patient_relationship.patient_id }') 

@app.route('/patient/<int:pid>/profile', methods = ['GET'])
@login_required
def view_profile_patient(pid):
    if session['user_id']:
        if current_user.user_role != 'Patient':
            return 'You are not authorized'
        if current_user.patient_relationship.patient_id != pid:
            return 'You can not view this'
        age = relativedelta(date_today, current_user.patient_relationship.patient_dob)
        return render_template('patient/patient_profile.html', age = age)
    else:
        return redirect('/')

@app.route('/patient/<int:pid>/profile/update', methods = ['GET', 'POST'])
@login_required
def update_patient_profile(pid):
    if session['user_id']:
        if current_user.user_role != 'Patient':
            return 'You are not authorized'
        if current_user.patient_relationship.patient_id != pid:
            return 'You can not view this'
        if request.method == 'GET':
            return render_template('patient/update_profile.html')
        else:
            # validation 
            # patients can not change thier gender or dob.
            user_name = request.form['u_name']
            user_password = request.form['u_password']
            patient_name = request.form['p_name']
            contact_info = request.form['contact_info']
            patient_email = request.form['email']
            patient_height = request.form['height']
            patient_weight = request.form['weight']
            
            if validate_username(user_name) == None:
                return render_template('patient/update_profile.html')
            if validate_password(user_password) == None:
                return render_template('patient/update_profile.html')
            if validate_name(patient_name) == None:
                return render_template('patient/update_profile.html')
            if validate_contact_number(contact_info) == None:
                return render_template('patient/update_profile.html')
            if validate_email(patient_email) == None:
                return render_template('patient/update_profile.html')
            if validate_only_text_fields(str(patient_height)) == False:
                return render_template('patient/update_profile.html')
            if validate_only_text_fields(str(patient_weight)) == False:
                return render_template('patient/update_profile.html')

            patient = db.get_or_404(Patient, current_user.patient_relationship.patient_id)
            patient.p.user_name = request.form['u_name']
            patient.p.user_password = request.form['u_password']
            patient.patient_name = request.form['p_name']
            patient.patient_email = request.form['email']
            patient.contact_info = request.form['contact_info']
            patient.patient_height = request.form['height']
            patient.patient_weight = request.form['weight']
            db.session.commit()
        return redirect(f'/patient/{ patient.patient_id }')
    else:
        return redirect('/')

@app.route('/book-appointment/<int:pid>', methods = ['GET', 'POST'])
@login_required
def book_appointment(pid):
    if session['user_id']:
        if current_user.user_role != 'Patient':
            return 'You are not authorized'
        if current_user.patient_relationship.patient_id != pid:
            return 'You can not view this'
        if request.method == 'GET':
            global date_today 
            # departments = Department.query.filter(Department.department_name != 'Dietetics').all()
            departments = Department.query.filter(Department.department_name != 'Dietetics').all()
            doctors = Doctor.query.all()
            appointment_dict = {i:0  for i in doctors}

            for i in doctors:
                doctor_availability_list = []
                helper_list = []
                doctor_availability = SlotSchedules.query.filter(and_(SlotSchedules.slot_doctor_id == i.doctor_id, SlotSchedules.date >= date_today)).order_by(SlotSchedules.date, SlotSchedules.schedule_slot_id).all()

                for a in doctor_availability:
                    if [a.date, a.s_sch.slot_name] not in helper_list:
                        helper_list += [[a.date, a.s_sch.slot_name]]
                        doctor_availability_list += [a]
                        appointment_dict[i] = doctor_availability_list
            return render_template('patient/book-appointment.html', departments = departments, doctors = doctors, appointment_dict = appointment_dict)
        else:
            return redirect('/')
    
@app.route('/patient/<int:pid>/confirm-appointment/<int:did>', methods = ['GET', 'POST'])
@login_required
def confirm_appointment(pid,did):
    if session['user_id']:
        if current_user.user_role != 'Patient':
            return 'You are not authorized'
        if current_user.patient_relationship.patient_id != pid:
            return 'You can not view this'
        
        global date_today 
        doctor = db.get_or_404(Doctor, did)
        list_of_next_7_dates = [(date_today + timedelta(days = i)) for i in range(8)]
        slots = {}
        all_slots = Slot.query.all()
        for d in list_of_next_7_dates:
            slots[d] = {}
            for s in all_slots:
                # doctor is not available for this date and this slot
                doctor_unavailable = SlotSchedules.query.filter(SlotSchedules.date == d, SlotSchedules.schedule_slot_id == s.slot_id, SlotSchedules.slot_doctor_id == doctor.doctor_id).all()
                if doctor_unavailable == []:
                    slots[d][s] = -1            
                else:
                    # patient has already has a booking on this date with this doctor
                    booked_slot = SlotSchedules.query.filter(SlotSchedules.date == d, SlotSchedules.schedule_slot_id == s.slot_id, SlotSchedules.slot_doctor_id == doctor.doctor_id, SlotSchedules.slot_patient_id == pid).first()
                    # patient has already has a booking on this date with other doctors
                    other_booked_slot = SlotSchedules.query.filter(SlotSchedules.date == d, SlotSchedules.schedule_slot_id == s.slot_id, SlotSchedules.slot_doctor_id != doctor.doctor_id, SlotSchedules.slot_patient_id == pid).first()
                    if booked_slot != None:
                        slots[d][s] = [1, booked_slot]
                    if other_booked_slot != None:
                        slots[d][s] = [2, other_booked_slot]
                    if (other_booked_slot == None) and (booked_slot == None):
                        unbooked_slot = SlotSchedules.query.filter(SlotSchedules.date == d, SlotSchedules.schedule_slot_id == s.slot_id, SlotSchedules.slot_doctor_id == doctor.doctor_id).first()
                        slots[d][s] = [0, unbooked_slot]

        if request.method == 'GET':
            return render_template('patient/confirm-appointment.html', doctor = doctor, patient = current_user.patient_relationship.patient_id, list_of_next_7_dates = list_of_next_7_dates, slots = slots, 
                                   all_slots = all_slots)
        else:
            form_content = request.form 
            form_content_to_dict = form_content.to_dict(flat = False)
            list_of_next_7_dates = [(date_today + timedelta(days = i)) for i in range(8)]

            input_slot = request.form['time_slot']
            selected_slot = db.get_or_404(SlotSchedules, int(input_slot))
            if selected_slot.slot_patient_id == None:
                selected_slot.slot_patient_id = current_user.patient_relationship.patient_id 
                selected_slot.slot_sch_appointment_rel = Appointment(date_time = selected_slot.date, doctor_id = doctor.doctor_id, patient_id = current_user.patient_relationship.patient_id)
                selected_slot.slot_sch_appointment_rel.t = Treatment(status = 'Booked')
                
                # notify patient
                notification = PatientDoctorNotifications(role = 'Doctor', message_type = 'Appointment Booking Confirmation', 
                                                          message_content = f'Hello, { current_user.patient_relationship.patient_name }! Your appointment with doctor { doctor.doctor_name } is on { selected_slot.date } ({ selected_slot.s_sch.slot_name })'
                                                          ,m_doctor_id = doctor.doctor_id, m_patient_id = current_user.patient_relationship.patient_id)
                db.session.add(notification)
                db.session.commit()
                return redirect(f'/patient/{ current_user.patient_relationship.patient_id}')
            
            else:
                new_entry = SlotSchedules(date = selected_slot.date, slot_doctor_id = selected_slot.slot_doctor_id, slot_patient_id = current_user.patient_relationship.patient_id, schedule_slot_id = selected_slot.schedule_slot_id)
                new_entry.slot_sch_appointment_rel = Appointment(date_time = selected_slot.date, doctor_id = doctor.doctor_id, patient_id = current_user.patient_relationship.patient_id)
                new_entry.slot_sch_appointment_rel.t = Treatment(status = 'Booked')
                db.session.add(new_entry)
                db.session.commit()

                # notify patient
                notification = PatientDoctorNotifications(role = 'Doctor', message_type = 'Appointment Booking Confirmation', 
                                                          message_content = f'Hello, { current_user.patient_relationship.patient_name }! Your appointment with Dr. { doctor.doctor_name } is on { new_entry.date } ({ new_entry.s_sch.slot_name })'
                                                          ,m_doctor_id = doctor.doctor_id, m_patient_id = current_user.patient_relationship.patient_id)
                db.session.add(notification)
                db.session.commit()
                return redirect(f'/patient/{ current_user.patient_relationship.patient_id}')
    else:
        return redirect('/')

@app.route('/patient/<int:pid>/cancel-appointment/<int:sid>', methods = ['GET'])
@login_required
def cancel_appointment_patient(pid, sid):
    if session['user_id']:
        if current_user.user_role != 'Patient':
            return 'You are not authorized'
        if current_user.patient_relationship.patient_id != pid:
            return 'You can not view this'
        # patient = db.get_or_404(Patient, pid)
        appointment = db.get_or_404(SlotSchedules, sid)
        if appointment.slot_sch_appointment_rel.t.status == 'Booked':
            appointment.slot_sch_appointment_rel.t.status = f'Cancelled by {current_user.patient_relationship.patient_name}'
        # notify the doctor that the patient has cancelled the appointment
        notification = PatientDoctorNotifications(role = 'Patient', m_doctor_id = appointment.slot_doctor_id, m_patient_id = current_user.patient_relationship.patient_id, 
                                                  message_type = 'Appointment Cancelled', 
                                                  message_content = f'Your appointment scheduled on { appointment.date } ({ appointment.s_sch.slot_name }) with Patient { current_user.patient_relationship.patient_name } was cancelled.')
        db.session.add(notification)
        db.session.commit()
        return redirect(f'/patient/{ current_user.patient_relationship.patient_id }')
    else:
        return redirect('/')
    
@app.route('/patient/<int:pid>/reschedule-appointment/doctor/<int:did>/<int:sid>', methods = ['GET', 'POST'])
@login_required
def reschedule_appointment(pid, did, sid):
    if session['user_id']:
        if current_user.user_role != 'Patient':
            return 'You are not authorized'
        if current_user.patient_relationship.patient_id != pid:
            return 'You can not view this'
        doctor = db.get_or_404(Doctor, did)
        reschedule_this_appointment = db.get_or_404(SlotSchedules, sid)
        all_slots = Slot.query.all()
        slots = {}
        list_of_next_7_dates = [(date_today + timedelta(days = i)) for i in range(8)]
        if request.method == 'GET':

            for d in list_of_next_7_dates:
                slots[d] = {}
                for s in all_slots:
                    # doctor is not available for this date and this slot
                    doctor_unavailable = SlotSchedules.query.filter(SlotSchedules.date == d, SlotSchedules.schedule_slot_id == s.slot_id, SlotSchedules.slot_doctor_id == doctor.doctor_id).all()
                    if doctor_unavailable == []:
                        slots[d][s] = -1            
                    else:
                        # patient has already has a booking on this date with this doctor
                        booked_slot = SlotSchedules.query.filter(SlotSchedules.date == d, SlotSchedules.schedule_slot_id == s.slot_id, SlotSchedules.slot_doctor_id == doctor.doctor_id, SlotSchedules.slot_patient_id == pid).first()
                        # patient has already has a booking on this date with other doctors
                        other_booked_slot = SlotSchedules.query.filter(SlotSchedules.date == d, SlotSchedules.schedule_slot_id == s.slot_id, SlotSchedules.slot_patient_id == pid, SlotSchedules.schedule_id != sid).first()
                        if booked_slot != None:
                            slots[d][s] = [1, booked_slot]
                        if other_booked_slot != None:
                            slots[d][s] = [2, other_booked_slot]
                        if (other_booked_slot == None) and (booked_slot == None):
                            unbooked_slot = SlotSchedules.query.filter(SlotSchedules.date == d, SlotSchedules.schedule_slot_id == s.slot_id, SlotSchedules.slot_doctor_id == doctor.doctor_id).first()
                            slots[d][s] = [0, unbooked_slot]

            return render_template('patient/reschedule_appointment.html', doctor = doctor, slots = slots, all_slots = all_slots, 
                                   list_of_next_7_dates = list_of_next_7_dates, reschedule_this_appointment = reschedule_this_appointment)

        else:
            input_slot = request.form['time_slot']
            slot = db.get_or_404(SlotSchedules, input_slot)
            revert_slot = db.get_or_404(SlotSchedules, sid)
            revert_slot.slot_sch_appointment_rel.t.status = f'Rescheduled by {current_user.patient_relationship.patient_name}'
            revert_slot.slot_patient_id == None

            if slot.slot_patient_id == None:
                slot.slot_patient_id = current_user.patient_relationship.patient_id
                slot.slot_sch_appointment_rel = Appointment(doctor_id = did, patient_id = current_user.patient_relationship.patient_id, s_sch_id = revert_slot.schedule_slot_id)
                slot.slot_sch_appointment_rel.t = Treatment(status = 'Booked') 
                message = PatientDoctorNotifications(message_type = 'Appointment Rescheduled by Patient', 
                                                 message_content = f'Your appointment with { current_user.patient_relationship.patient_name } scheduled on { revert_slot.date } ({ revert_slot.s_sch.slot_name }) was rescheduled to { slot.date } ({ slot.s_sch.slot_name })',
                                                 m_doctor_id = did, m_patient_id = pid)
                db.session.add(message)           
            else:
                new_entry = SlotSchedules(date = slot.date, slot_doctor_id = revert_slot.slot_doctor_id, slot_patient_id = current_user.patient_relationship.patient_id, schedule_slot_id = revert_slot.schedule_slot_id)
                new_entry.slot_sch_appointment_rel = Appointment(date_time = revert_slot.date, doctor_id = doctor.doctor_id, patient_id = current_user.patient_relationship.patient_id)
                new_entry.slot_sch_appointment_rel.t = Treatment(status = 'Booked')
                db.session.add(new_entry)
                db.session.commit()

                # notify patient
                notification = PatientDoctorNotifications(role = 'Doctor', message_type = 'Appointment Booking Confirmation', 
                                                          message_content = f'Hello, { current_user.patient_relationship.patient_name }! Your appointment with Dr. { doctor.doctor_name } is on { new_entry.date } ({ new_entry.s_sch.slot_name })'
                                                          ,m_doctor_id = doctor.doctor_id, m_patient_id = current_user.patient_relationship.patient_id)
                db.session.add(notification)

            db.session.commit()
            return redirect(f'/patient/{ current_user.patient_relationship.patient_id }') 
    else:
        return redirect('/')

@app.route('/patient/<int:pid>/send-message-to-admin', methods = ['GET', 'POST'])
@login_required
def patient_send_admin_messages(pid):
    if session['user_id']:
        if current_user.user_role != 'Patient':
            return 'You are not authorized'
        if current_user.patient_relationship.patient_id != pid:
            return 'You can not view this'
        global date_today
        if request.method == 'GET':
            return render_template('patient/admin_notify_profile_change.html', date_today = date_today)
        else:
            message_content = request.form['message']
            message = AdminPatientNotifications(admin_patient_message_type = f'From Patient {current_user.patient_relationship.patient_name}', admin_patient_message_content = message_content)
            db.session.add(message)
            db.session.commit()
            return redirect(f'/patient/{ current_user.patient_relationship.patient_id }')

@app.route('/patient/<int:pid>/notify-availabililty/<int:did>', methods = ['GET'])
@login_required
def notify_patient_doctor_availability(pid, did):
    if session['user_id']:
        if current_user.user_role != 'Patient':
            return 'You are not authorized'
        if current_user.patient_relationship.patient_id != pid:
            return 'You can not view this'
        global date_today
        patient = db.get_or_404(Patient, pid)
        doctor = db.get_or_404(Doctor, did)
        notification = AvailibilityNotifications(notif_doctor_id = doctor.doctor_id, notif_patient_id = patient.patient_id, starting_date = date_today)
        db.session.add(notification)
        db.session.commit()
        return redirect(f"/book-appointment/{ patient.patient_id }")
    else:
        return redirect('/')

@app.route('/patient/<int:pid>/notification-page', methods = ['GET'])
@login_required
def notification_page_patient(pid):
    if session['user_id']:
        if current_user.user_role != 'Patient':
            return 'You are not authorized'
        if current_user.patient_relationship.patient_id != pid:
            return 'You can not view this'
        global date_today
        patient = db.get_or_404(Patient, pid)
        unread_admin_notifications = AdminPatientNotifications.query.filter(AdminPatientNotifications.message_patient_id == pid, AdminPatientNotifications.patient_message_recieved == 0).order_by(desc(AdminPatientNotifications.message_date_time)).all()
        read_admin_notifications = AdminPatientNotifications.query.filter(AdminPatientNotifications.message_patient_id == pid, AdminPatientNotifications.patient_message_recieved == 1).order_by(desc(AdminPatientNotifications.message_date_time)).all()
        unread_doctor_notifications = PatientDoctorNotifications.query.filter(PatientDoctorNotifications.m_patient_id == pid, PatientDoctorNotifications.role == 'Doctor', PatientDoctorNotifications.patient_message_recieved == 0).order_by(desc(PatientDoctorNotifications.message_date_time)).all()
        read_doctor_notifications = PatientDoctorNotifications.query.filter(PatientDoctorNotifications.m_patient_id == pid, PatientDoctorNotifications.role == 'Doctor', PatientDoctorNotifications.patient_message_recieved == 1).order_by(desc(PatientDoctorNotifications.message_date_time)).all()
        unread_availibility_notifications = AvailibilityNotifications.query.filter(AvailibilityNotifications.starting_date >= date_today, AvailibilityNotifications.notif_patient_id == pid, AvailibilityNotifications.patient_message_recieved == 0).order_by(desc(AvailibilityNotifications.message_date_time)).all()
        read_availibility_notifications = AvailibilityNotifications.query.filter(AvailibilityNotifications.starting_date >= date_today, AvailibilityNotifications.notif_patient_id == pid, AvailibilityNotifications.patient_message_recieved == 1).order_by(desc(AvailibilityNotifications.message_date_time)).all()

        # Mark notifications as read
        for n in unread_doctor_notifications:
            n.patient_message_recieved = 1

        for n in unread_admin_notifications:
            n.patient_message_recieved = 1

        for n in unread_availibility_notifications:
            n.patient_message_recieved = 1

        db.session.commit()
        return render_template('patient/patient_notification_page.html', patient = patient, unread_admin_notifications = unread_admin_notifications, read_admin_notifications = read_admin_notifications, unread_availibility_notifications = unread_availibility_notifications, read_availibility_notifications = read_availibility_notifications, unread_doctor_notifications = unread_doctor_notifications, read_doctor_notifications = read_doctor_notifications)
    else:
        return redirect('/')
    
@app.route('/patient/<int:pid>/thank-you/doctor/<int:did>/<int:sid>', methods = ['GET'])
@login_required
def send_thank_you_messages(pid, did, sid):
    if session['user_id']:
        if current_user.user_role != 'Patient':
            return 'You are not authorized'
        if current_user.patient_relationship.patient_id != pid:
            return 'You can not view this'
        patient = db.get_or_404(Patient, pid)
        doctor = db.get_or_404(Doctor, did)
        appointment = db.get_or_404(SlotSchedules, sid)
        thank_you_message = PatientDoctorNotifications(m_doctor_id = doctor.doctor_id, m_patient_id = patient.patient_id, message_type = 'Thank_you_message', role = 'Patient')
        db.session.add(thank_you_message)
        db.session.commit()
        return redirect(f'/patient/view-appointment/{ patient.patient_id }/{ appointment.schedule_id }')
    else:
        return redirect('/')

@app.route('/patient/<int:pid>/messages/doctor/<int:did>', methods = ['GET', 'POST'])
@login_required
def patient_send_message_to_doctor(pid, did):
    if session['user_id']:
        if current_user.user_role != 'Patient':
            return 'You are not authorized'
        if current_user.patient_relationship.patient_id != pid:
            return 'You can not view this'
        global date_today
        patient = db.get_or_404(Patient, pid)
        doctor = db.get_or_404(Doctor, did)
        warning_message = None
        if request.method == 'GET':
            return render_template('patient/send_message_to_doctor.html', date_today = date_today, patient = patient, doctor = doctor, warning_message = None)
        else:
            message_content = request.form['message']

            # validation
            if validate_description(message_content) == None:
                return render_template('patient/send_message_to_doctor.html', date_today = date_today, patient = patient, doctor = doctor, warning_message = True)
            
            patient_message = PatientDoctorNotifications(m_doctor_id = doctor.doctor_id, m_patient_id = patient.patient_id, message_type = 'Doctor_Notifications', 
                                                         message_content = message_content, role = 'Patient')    
            db.session.add(patient_message)
            db.session.commit()
        return redirect(f'/patient/{ current_user.patient_relationship.patient_id }') 
    else:
        return redirect('/')


@app.route('/patient/view-appointment/<int:pid>/<int:sid>', methods = ['GET'])
@login_required
def view_appointment_patient(pid, sid):
    if session['user_id']:
        if current_user.user_role != 'Patient':
            return 'You are not authorized'
        if current_user.patient_relationship.patient_id != pid:
            return 'You can not view this'
        global date_today
        appointment = db.get_or_404(SlotSchedules, sid)
        doctor = appointment.slot_doctor
        past_appointments = SlotSchedules.query.filter(SlotSchedules.slot_patient_id == pid, SlotSchedules.slot_doctor_id == doctor.doctor_id, SlotSchedules.date < date_today).all()
        return render_template('patient/view-appointment.html', doctor = doctor, appointment = appointment, past_appointments = past_appointments, date_today  = date_today)
    else:
        return redirect('/')

@app.route('/patient/<int:pid>/view_doctor/<int:did>', methods = ['GET', 'POST'])
@login_required
def patient_view_doctor(pid, did):
    if session['user_id']:
        if current_user.user_role != 'Patient':
            return 'You are not authorized'
        if current_user.patient_relationship.patient_id != pid:
            return 'You can not view this'
        
        global date_today
        patient = db.get_or_404(Patient, pid)
        doctor = db.get_or_404(Doctor, did)
        past_appointments = Appointment.query.filter(and_(Appointment.doctor_id == did, Appointment.patient_id == pid, Appointment.date_time < date_today)).order_by(Appointment.date_time).all()
        upcoming_appointments = Appointment.query.filter(and_(Appointment.doctor_id == did, Appointment.patient_id == pid, Appointment.date_time >= date_today)).all()
        doctor_availability = SlotSchedules.query.filter(and_(SlotSchedules.slot_doctor_id == did, SlotSchedules.date >= date_today)).order_by(SlotSchedules.date, SlotSchedules.schedule_slot_id).order_by(desc(SlotSchedules.date)).all()
        doctor_availability_list = []
        helper_list = []
        for a in doctor_availability:
            if [a.date, a.s_sch.slot_name] not in helper_list:
                helper_list += [[a.date, a.s_sch.slot_name]]
                doctor_availability_list += [a]

        if request.method == 'GET':
            return render_template('patient/view_doctor.html', patient = patient, doctor = doctor, past_appointments = past_appointments, upcoming_appointments = upcoming_appointments, doctor_availability_list = doctor_availability_list, date_today = date_today)
        else:
            message_content = request.form['message']

            # validation
            if validate_description(message_content) == None:
                return render_template('patient/send_message_to_doctor.html', date_today = date_today, patient = patient, doctor = doctor, warning_message = True)
            
            patient_message = PatientDoctorNotifications(m_doctor_id = doctor.doctor_id, m_patient_id = patient.patient_id, message_type = 'Doctor_Notifications', 
                                                         message_content = message_content, role = 'Patient')    
            db.session.add(patient_message)
            db.session.commit()
        return redirect(f'/patient/{ current_user.patient_relationship.patient_id }') 
    else:
        return redirect('/')

@app.route('/patient/<int:pid>/view-dept/<int:did>', methods = ['GET'])
@login_required
def patient_view_dept(pid, did):
    if session['user_id']:
        if current_user.user_role != 'Patient':
            return 'You are not authorized'
        if current_user.patient_relationship.patient_id != pid:
            return 'You can not view this'
        patient = db.get_or_404(Patient, pid)
        department = db.get_or_404(Department, did)
        past_appointments = {i: {} for i in department.doctors }
        for doc in past_appointments.keys():
            past_appointments_list = Appointment.query.filter(and_(Appointment.doctor_id == doc.doctor_id, Appointment.patient_id == pid, Appointment.date_time < date_today)).order_by(Appointment.date_time).all()
            past_appointments[doc] = past_appointments_list

        upcoming_appointments = {i: {} for i in department.doctors }
        for doc in upcoming_appointments.keys():
            past_appointments_list = Appointment.query.filter(and_(Appointment.doctor_id == doc.doctor_id, Appointment.patient_id == pid, Appointment.date_time >= date_today)).order_by(Appointment.date_time).all()
            upcoming_appointments[doc] = past_appointments_list

        return render_template('patient/view_department.html', patient = patient, department = department, past_appointments = past_appointments, upcoming_appointments = upcoming_appointments)
    else:
        return redirect('/')

@app.route('/patient/<int:pid>/search', methods = ['POST'])
@login_required
def search_patient(pid):
    if session['user_id']:
        if current_user.user_role != 'Patient':
            return 'You are not authorized'
        if current_user.patient_relationship.patient_id != pid:
            return 'You can not view this'
        patient = db.get_or_404(Patient, current_user.patient_relationship.patient_id)
        input_value = request.form['query']

        if not input_value.isnumeric(): # search for name, email
            doctors = Doctor.query.filter(or_(Doctor.doctor_name.like(f'%{input_value}%'), Doctor.doctor_email.like(f'%{input_value}%'))).all()
            departments = Department.query.filter(Department.department_name.like(f'%{input_value}%')).all()
            return render_template('patient/search_patient.html',patient = patient, input_value = input_value, doctors = doctors, departments = departments)
        
        else: # search for contact number
            doctors = Doctor.query.filter(Doctor.doctor_contact_number.like(f'%{input_value}%')).all()
            departments = []
            return render_template('patient/search_patient.html', patient = patient, input_value = input_value, doctors = doctors, departments = departments)
    else:
        return redirect('/')
    
