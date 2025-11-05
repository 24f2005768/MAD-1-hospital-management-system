from flask import Flask, render_template, request, redirect
from sqlalchemy import and_, or_, distinct
from application.models import *
from app import app
import datetime
import os

date_today = date.today()

@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('login_page.html', flag1 = False, flag2 = False)
    else:
        user_name = request.form['u_name']
        user_password = request.form['u_password']

        u = User.query.filter(User.user_name == user_name).first()
        if u == None:
            return render_template('login_page.html', flag2 = True) # user is not registered

        u_id = u.user_id

        if user_password == u.user_password and u.user_role == 'Admin': #user is admin
            return redirect('/admin')
        elif user_password == u.user_password and u.user_role == 'Doctor': #user is a doctor
            d_id = Doctor.query.filter(Doctor.doctor_user_id == u_id).first()
            return redirect(f'/doctor/{d_id.doctor_id}')
        elif user_password == u.user_password and u.user_role == 'Patient': #user is a patient
            p_id = Patient.query.filter(Patient.patient_user_id == u_id).first()
            return redirect(f'/patient/{p_id.patient_id}')
        return render_template('login_page.html', flag1 = True) # Invalid username or password

# Admin
@app.route('/admin', methods = ['GET', 'POST'])
def admin_dashboard():
    if request.method == 'GET':
        doctors = Doctor.query.all()
        patients = Patient.query.all()
        appointments = Appointment.query.all()
        departments = Department.query.all()

        doctors_first_five = Doctor.query.limit(5).all()
        patients_first_five = Patient.query.limit(5).all()
        appointments_first_five = Appointment.query.limit(5).all()
        departments_first_four = Department.query.limit(4).all()
        appointments = Appointment.query.all()
        admin_name = Admin.query.first()

        return render_template('admin/admin-dashboard.html', doctors = doctors, patients = patients, appointments = appointments, departments = departments,
                               doctors_first_five = doctors_first_five, patients_first_five = patients_first_five, appointments_first_five = appointments_first_five, departments_first_four = departments_first_four, admin_name = admin_name)

@app.route('/admin/appointment/<int:pid>/<int:did>', methods = ['GET'])
def view_appointment_patient_doctor(pid, did):
    global date_today 
    patient = Patient.query.filter(Patient.patient_id == pid).first()
    doctor = Doctor.query.filter(Doctor.doctor_id == did).first()
    past_appointments = Appointment.query.filter(and_(Appointment.patient_id == pid, Appointment.doctor_id == did, Appointment.date_time <= date_today)).all()
    upcoming_appointments = Appointment.query.filter(and_(Appointment.patient_id == pid, Appointment.doctor_id == did, Appointment.date_time >= date_today)).all()
    return render_template('admin/view-appointment-p-d.html', past_appointments = past_appointments, doctor = doctor, patient = patient, pid = pid, did = did, upcoming_appointments = upcoming_appointments)

@app.route('/admin/view-all-appointments', methods = ['GET'])
def view_all_appointments():
    appointments = Appointment.query.all()
    global date_today 
    past_appointments = Appointment.query.filter(Appointment.date_time <= date_today).all()
    upcoming_appointments = Appointment.query.filter(Appointment.date_time >= date_today).all()
    return render_template('admin/view-all-appointments.html', appointments = appointments, past_appointments = past_appointments, upcoming_appointments = upcoming_appointments)

# admin - department: view - view_all - add - update - delete

@app.route('/department/<int:dept_id>', methods = ['GET'])
def view_department(dept_id):
    global date_today
    department = Department.query.filter(Department.department_id == dept_id).first()

    dept_doctors = department.doctors
    upcoming_dept_appointments = []
    for doc in dept_doctors:
        upcoming_dept_appointments += Appointment.query.filter(and_(Appointment.doctor_id == doc.doctor_id, Appointment.date_time >= date_today)).all()

    past_dept_appointments = []
    for doc in dept_doctors:
        past_dept_appointments += Appointment.query.filter(and_(Appointment.doctor_id == doc.doctor_id, Appointment.date_time <= date_today)).all()
    return render_template('view_department.html', department = department, upcoming_dept_appointments = upcoming_dept_appointments, past_dept_appointments = past_dept_appointments, flag = True)

@app.route('/all-dept', methods = ['GET'])
def view_all_departments():
    departments = Department.query.all()
    return render_template('admin/view-all-dept.html', departments = departments)

@app.route('/add_dept', methods = ['GET', 'POST'])
def add_department():
    if request.method == 'GET':
        return render_template('admin/add_department.html')
    else:
        department_name = request.form['d_name']
        if Department.query.filter(Department.department_name == department_name).first():
            return render_template('exists.html')       
        department_description = request.form['d_desc']
        dept = Department(department_name = department_name, department_description = department_description)
        db.session.add(dept)
        db.session.commit()
        return redirect('/admin')

@app.route('/admin/department/update/<int:dept_id>', methods = ['GET', 'POST'])
def update_dept(dept_id):
    if request.method == 'GET':
        department = db.get_or_404(Department, dept_id)
        return render_template('admin/update-department.html', department = department)
    else:
        department = db.get_or_404(Department, dept_id)
        department.department_name = request.form['dept_name']
        department.department_description = request.form['dept_description']
        db.session.commit()
        return redirect('/admin')

@app.route('/admin/department/delete/<int:dept_id>')
def delete_dept(dept_id):
        department = db.get_or_404(Department, dept_id)
        doctors = department.doctors
        for doctor in doctors:
            doctor = db.get_or_404(Doctor, doctor.doctor_id)

            user = doctor.d 
            doctor_appointments = doctor.appointment_d
            doctor_slots = doctor.doctor_slot 

            for slot in doctor_slots:
                db.session.delete(slot)

            if doctor_appointments == None: 
                pass
            else:
                for appointment in doctor_appointments:
                    db.session.delete(appointment)

            db.session.delete(doctor)
            db.session.delete(user)

        db.session.delete(department)
        db.session.commit()
        return redirect('/admin')

# admin - doctor: view - add - update - delete

@app.route('/admin/doctor/<int:did>', methods = ['GET'])
def view_doctor(did):
    doctor = db.get_or_404(Doctor, did)
    global date_today 
    past_appointments = Appointment.query.filter(and_(Appointment.date_time <= date_today, Appointment.doctor_id == doctor.doctor_id)).all()
    upcoming_appointments = Appointment.query.filter(and_(Appointment.date_time >= date_today, Appointment.doctor_id == doctor.doctor_id, Appointment.patient_id != None)).all()
    available_slots = SlotSchedules.query.filter(and_(SlotSchedules.date >= date_today, SlotSchedules.slot_doctor_id == doctor.doctor_id)).all()
    return render_template('admin/view_doctor.html', doctor = doctor,upcoming_appointments = upcoming_appointments, past_appointments = past_appointments, available_slots = available_slots)

@app.route('/admin/view-all-doctors', methods = ['GET'])
def view_all_doctors():
    doctors = Doctor.query.all()
    return render_template('admin/view-all-doctors.html', doctors = doctors)

@app.route('/admin/doctor/add', methods = ['GET', 'POST'])
def add_doctor():
    if request.method == 'GET':
        departments = Department.query.all()
        return render_template('admin/add_doctor.html', departments = departments)
    else:
        doctor_name = request.form['d_name']
        if Doctor.query.filter(Doctor.doctor_name == doctor_name).first():
            return render_template('exists.html')
        
        # add as a user
        user_name = request.form['u_name']
        user_password = request.form['u_password']
        user = User(user_name = user_name, user_password = user_password, user_role = 'Doctor')
        db.session.add(user)

        # add as a doctor
        dept = request.form['dept']
        d = Department.query.filter(Department.department_name == dept).first()

        doctor_contact_number = request.form['contact_info']
        doctor_user_id = User.query.filter(User.user_name == user_name).first()
        doctor_email = request.form['email']
        doctor_desc = request.form['desc']
        doctor = Doctor(doctor_name = doctor_name, department_id = d.department_id, doctor_contact_number = doctor_contact_number, doctor_user_id = doctor_user_id.user_id, doctor_email = doctor_email, doctor_desc = doctor_desc)
        
        db.session.add(doctor)
        db.session.commit()
        return redirect('/admin')

@app.route('/admin/doctor/update/<int:did>', methods = ['GET', 'POST'])
def update_doctor(did):
    if request.method == 'GET':
        old_data = Doctor.query.filter_by(doctor_id = did).first()
        departments = Department.query.all()
        return render_template('admin/update_doctor.html',did = did, old_data = old_data, departments = departments)
    else:
        new_data = Doctor.query.filter_by(doctor_id = did).first()
        new_data.doctor_name = request.form['d_name']
        new_data.doctor_contact_number = request.form['contact_info']
        new_data.doctor_email = request.form['email']

        dept = request.form['dept']
        d = Department.query.filter(Department.department_name == dept).first()
        new_data.department_id = d.department_id

        blacklisted = request.form['blacklist']
        if blacklisted == 'True':
            new_data.doctor_blacklisted = True
        else:
            new_data.doctor_blacklisted = False
        db.session.commit()
        return redirect('/admin')

@app.route('/admin/doctor/delete/<int:did>', methods = ['GET'])
def delete_doctor(did):
    doctor = db.get_or_404(Doctor, did)

    user = doctor.d 
    doctor_appointments = doctor.appointment_d
    doctor_slots = doctor.doctor_slot 
    for slot in doctor_slots:
        db.session.delete(slot)

    for appointment in doctor_appointments:
        db.session.delete(appointment)

    db.session.delete(doctor)
    db.session.delete(user)

    db.session.commit()
    return redirect('/admin')

@app.route('/admin/doctor/check-availability/<int:did>', methods = ['GET'])
def check_availabilty(did):
    doctor_slots = SlotSchedules.query.filter(and_(SlotSchedules.slot_doctor_id == did, SlotSchedules.date >= date_today)).order_by(SlotSchedules.date).all()
    doctor = db.get_or_404(Doctor, did)
    return render_template('admin/check-availability.html', doctor_slots = doctor_slots, doctor = doctor)

# admin - patient: view - view_all - update - delete

@app.route('/admin/patient/<int:pid>', methods = ['GET'])
def view_patient_admin(pid):
    global date_today 
    patient = db.get_or_404(Patient, pid)
    past_appointments = Appointment.query.filter(and_(Appointment.date_time <= date_today, Appointment.patient_id == patient.patient_id)).all()
    upcoming_appointments = Appointment.query.filter(and_(Appointment.date_time >= date_today, Appointment.patient_id == patient.patient_id)).all()

    return render_template('admin/view-patient.html', patient = patient, past_appointments = past_appointments, upcoming_appointments = upcoming_appointments)

@app.route('/admin/view-all-patients', methods = ['GET'])
def view_all_patients():
    patients = Patient.query.all()
    return render_template('admin/view-all-patients.html', patients = patients)


@app.route('/admin/patient/update/<int:pid>', methods = ['GET', 'POST'])
def update_patient(pid):
    if request.method == 'GET':
        old_data = db.get_or_404(Patient,pid)
        return render_template('admin/update_patient.html', pid = pid, old_data = old_data)
    else:
        new_data = Patient.query.filter(Patient.patient_id == pid).first()
        new_data.patient_name = request.form['p_name']
        new_data.patient_email = request.form['email']
        new_data.contact_info = request.form['contact_info']

        blacklisted = request.form['blacklist']
        if blacklisted == 'True':
            new_data.patient_blacklisted = True
        else:
            new_data.patient_blacklisted = False

        db.session.commit()
        return redirect('/admin')

@app.route('/admin/patient/delete/<int:pid>', methods = ['GET'])
def delete_patient(pid):
    patient = db.get_or_404(Patient, pid)

    user = patient.p
    patient_appointments = patient.appointment_p
    patient_slots = patient.patient_slot

    for slot in patient_slots:
        db.session.delete(slot)
    db.session.delete(patient_appointments)
    db.session.delete(patient)
    db.session.delete(user)

    db.session.commit()
    return redirect('/admin')

# admin - search 

@app.route('/admin/search', methods = ['POST'])
def search():
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

            patients = Patient.query.filter(Patient.patient_name == input_value).all()
            if patients != []:
                for patient in patients:
                    appointments_by_patient_name = Appointment.query.filter(Appointment.patient_id == patient.patient_id).all()

            doctors = Doctor.query.filter(Doctor.doctor_name == input_value).all()
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

# Doctor   
 
@app.route('/doctor/<int:did>', methods = ['GET'])
def doctor_dashboard(did):
    if request.method == 'GET':
        global date_today
        patients_list = []
        show_patients = []
        helper_lst = []
        availabilty_list = []
        appointments_today = []
        appointments_this_week = []
        slot_patients_dict = {}

        doctor = Doctor.query.filter(Doctor.doctor_id == did).first()
        patients = Appointment.query.filter(Appointment.doctor_id == did).all()
        # availabilty = SlotSchedules.query.filter(and_(SlotSchedules.slot_doctor_id == did, SlotSchedules.date >= date_today, SlotSchedules.slot_patient_id != None)).order_by(SlotSchedules.date, SlotSchedules.schedule_slot_id).all()
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
        # print(slot_patients_dict)

        # appointments scheduled today
        appointments_today = SlotSchedules.query.filter(and_(SlotSchedules.date == date_today, SlotSchedules.slot_doctor_id == did, SlotSchedules.slot_patient_id != None)).all()
        
        # appointments scheduled this week 
        list_of_next_7_dates = [(date_today + timedelta(days = i)) for i in range(1,8)]
        for d in list_of_next_7_dates:
            appointments_this_week += SlotSchedules.query.filter(and_(SlotSchedules.date == d, SlotSchedules.slot_doctor_id == did,  SlotSchedules.slot_patient_id != None)).order_by(SlotSchedules.date, SlotSchedules.schedule_slot_id).all()

        # past appointments
        past_appointments = SlotSchedules.query.filter(and_(SlotSchedules.slot_doctor_id == did, SlotSchedules.date < date_today, SlotSchedules.slot_patient_id != None)).all()

        return render_template('doctor/doctor-dashboard.html', doctor = doctor, show_patients = show_patients, availabilty_list = availabilty_list, slot_patients_dict = slot_patients_dict, 
                               appointments_today = appointments_today, appointments_this_week = appointments_this_week, past_appointments = past_appointments)

@app.route('/doctor/<int:did>/doctor-profile', methods = ['GET'])
def view_doctor_profile(did):
    doctor = db.get_or_404(Doctor, did)
    return render_template('doctor/profile.html', doctor = doctor)

@app.route('/doctor/<int:did>/doctor-profile/update', methods = ['GET', 'POST'])
def update_doctor_profile(did):
    if request.method == 'GET':
        doctor = db.get_or_404(Doctor, did)
        return render_template('doctor/update_profile.html', doctor = doctor, did = did)
    else:
        did = did
        doctor = db.get_or_404(Doctor, did)
        doctor.doctor_name = request.form['d_name']
        doctor.doctor_desc = request.form['descprition']
        doctor.doctor_email = request.form['email']
        doctor.doctor_contact_number = request.form['contact_info']
        db.session.commit()
        return redirect(f'/doctor/{did}')

@app.route('/doctor/view-patient/<int:pid>/<int:did>', methods = ['GET'])
def view_patient_doctor(pid, did):
    global date_today

    doctor = db.get_or_404(Doctor, did)
    patient = Appointment.query.filter(and_(Appointment.doctor_id == did, Appointment.patient_id == pid)).first()
    past_appointments = Appointment.query.filter(and_(Appointment.doctor_id == did, Appointment.patient_id == pid, Appointment.date_time < date_today)).order_by(Appointment.date_time).all()
    all_past_appointments = Appointment.query.filter(and_(Appointment.patient_id == pid, Appointment.date_time < date_today)).order_by(Appointment.date_time).all()
    upcoming_appointments = Appointment.query.filter(and_(Appointment.doctor_id == did, Appointment.patient_id == pid, Appointment.date_time >= date_today)).all()
    if past_appointments == []:
        last_visit = '--'
    elif len(past_appointments) == 1:
        last_visit = past_appointments[0].date_time
    else:
        last_visit = past_appointments[-1].date_time

    return render_template('doctor/view-patient.html', doctor = doctor, patient = patient, past_appointments = past_appointments, last_visit = last_visit, upcoming_appointments = upcoming_appointments, all_past_appointments = all_past_appointments)

@app.route('/doctor/patients-by-slot/<int:did>/<int:sid>', methods = ['GET'])
def view_patients_by_slots(did, sid):
    doctor = db.get_or_404(Doctor, did)
    slot = SlotSchedules.query.filter(SlotSchedules.schedule_id == sid).first()
    slot_date = slot.date
    all_appointments = SlotSchedules.query.filter(and_(SlotSchedules.date == slot_date, SlotSchedules.schedule_slot_id == slot.schedule_slot_id, SlotSchedules.slot_patient_id != None)).all()
    return render_template('doctor/view-patients-by-slot.html', slot = slot, all_appointments = all_appointments, doctor = doctor)

@app.route('/doctor/ongoing_appointment/<int:did>/<int:aid>', methods = ['GET', 'POST'])
def ongoing_appointments(did, aid):
    if request.method == 'GET':
        doctor = db.get_or_404(Doctor, did)
        appointment = SlotSchedules.query.filter(SlotSchedules.schedule_id == aid).first()
        patient = Patient.query.filter(Patient.patient_id == appointment.slot_patient_id).first()
        past_appointments = Appointment.query.filter(and_(Appointment.doctor_id == did, Appointment.patient_id == patient.patient_id, Appointment.date_time <= date_today)).order_by(Appointment.date_time).all()
        print(past_appointments)
        if past_appointments == []:
            last_visit = '--'
        elif len(past_appointments) == 1:
            last_visit = past_appointments[0].date_time
        else:
            last_visit = past_appointments[-1].date_time
        return render_template('doctor/ongoing_treatment.html', doctor = doctor, patient = patient, appointment = appointment, last_visit = last_visit)
    else:
        diagnosis = request.form['diagnosis']
        notes = request.form['notes']
        prescription = request.form['prescription']
        tests = request.form['tests']

        doctor = db.get_or_404(Doctor, did)
        return redirect(f'/doctor/{did}')

@app.route('/doctor/update-treatment-details/<int:did>/<int:tid>', methods = ['GET', 'POST'])
def update_treatment_details(tid, did):
    if request.method == 'GET':
        treatment = Treatment.query.filter(Treatment.treatment_id == tid).first()
        list_of_options = ['Completed', 'Booked', 'Cancelled'] 
        treatment_status = treatment.status
        return render_template('doctor/update-treatment-details.html', treatment = treatment, list_of_options = list_of_options, treatment_status = treatment_status)
    else:
        new_data = Treatment.query.filter(Treatment.treatment_id == tid).first()
        new_data.diagnosis = request.form['diagnosis']
        new_data.status = request.form['status']
        new_data.prescription = request.form['prescription']
        new_data.notes = request.form['notes']
        new_data.tests = request.form['tests']

        db.session.commit()
        return redirect(f'/doctor/{did}')
    
@app.route('/doctor/cancel-appointment/<int:did>/<int:tid>', methods = ['GET'])
def cancel_appointment_doctor(tid, did):
    treatment = Treatment.query.filter(Treatment.treatment_id == tid).first()
    doctor = db.get_or_404(Doctor, did)
    patient = treatment.ap[0].p_ref
    if treatment.status == 'Booked':
        treatment.status = 'Cancelled'
        db.session.commit()

    return redirect(f"/doctor/view-patient/{ patient.patient_id }/{ doctor.doctor_id }")
    
@app.route('/doctor/provide_slots/<int:did>', methods = ['GET', 'POST'])
def provide_availability(did):
    if request.method == 'GET':
        doctor = db.get_or_404(Doctor, did)
        list_of_next_7_dates = [(date_today + timedelta(days = i)) for i in range(8)]
        slots = Slot.query.all()

        appointments_dict = {}
        for d in list_of_next_7_dates:
            appointments_dict[d] = {}
            for s in slots:
                appointments = SlotSchedules.query.filter(and_(SlotSchedules.slot_doctor_id == did, SlotSchedules.date == d, SlotSchedules.schedule_slot_id == s.slot_id, SlotSchedules.status != 'Cancelled')).all()
                appointments_dict[d][s] = appointments
                appointments = SlotSchedules.query.filter(and_(SlotSchedules.slot_doctor_id == did, SlotSchedules.date == d, SlotSchedules.schedule_slot_id == s.slot_id, SlotSchedules.status == None)).all()
                appointments_dict[d][s] += appointments
        return render_template('/doctor/provide_availability.html', appointments_dict = appointments_dict, doctor = doctor, slots = slots, list_of_next_7_dates = list_of_next_7_dates)
    
    else:
        doctor = db.get_or_404(Doctor, did)
        availability = request.form
        a = availability.to_dict(flat=False)
        # print(a)
        slots = Slot.query.all()

        past_state = SlotSchedules.query.filter(and_(SlotSchedules.date > date_today, SlotSchedules.slot_doctor_id == did)).all()
        if past_state != []:
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

        else:
            for s in a.keys():
                slot_id = Slot.query.filter(Slot.slot_id == s).first()
                for x in a[s]:
                    y = int(x[0:4])
                    m = int(x[5:7])
                    d = int(x[8:10])
                    slot_date = datetime.date(y,m,d)
                    slot = SlotSchedules(slot_doctor_id = did, schedule_slot_id = slot_id.slot_id, date = slot_date)
                    db.session.add(slot)
        db.session.commit()
        return redirect(f'/doctor/{ doctor.doctor_id }')

@app.route('/doctor/<int:did>/search', methods = ['POST'])
def search_doctor_dash(did):
    if request.method == 'POST':
        doctor = db.get_or_404(Doctor, did)
        input_value = request.form['query']

        if not input_value.isnumeric():
            appointments_by_doctor = Appointment.query.filter(Appointment.doctor_id == did).all()
            patients = [] #list of all patients which has booked an appointment with the doctor
            helper_list = [] 
            search_function = []
            appointments_by_patient_name = []

            doctors = Doctor.query.filter(or_(Doctor.doctor_name.like(f'%{input_value}%'), Doctor.doctor_contact_number.like(f'%{input_value}%'), Doctor.doctor_id.like(f'%{input_value}%'))).all()
            departments = Department.query.filter(Department.department_name.like(f'%{input_value}%')).all()

            for p in appointments_by_doctor:
                if p.p_ref.patient_name not in helper_list:
                    patients += [p]
                    helper_list += [p.p_ref.patient_name]

            for p in patients:
                search_list = Patient.query.filter(Patient.patient_name.like(f'%{input_value}%'), Patient.patient_id == p.patient_id).all()
                if search_list != []:
                    search_function += search_list
            
            for p in search_function:
                appointments_by_patient_name += Appointment.query.filter(Appointment.patient_id == p.patient_id).all()
            return render_template('doctor/search_doctor.html', input_value = input_value, search_function = search_function, doctor = doctor, appointments_by_patient_name = appointments_by_patient_name, doctors = doctors, departments = departments)

# Patient: dashboard - register - book_appointment - confirm_appointment
@app.route('/patient/<int:pid>', methods = ['GET'])
def patient_dashboard(pid):
    if request.method == 'GET':
        return render_template('patient/patient-dashboard.html')
    

@app.route('/register', methods = ['GET', 'POST'])
def register_patient():
    if request.method == 'GET':
        return render_template('patient/register_patient.html')
    else:
        patient_name = request.form['p_name']
        if Patient.query.filter(Patient.patient_name == patient_name).first():
            return render_template('exists.html') 
        
        # add as a user
        user_name = request.form['u_name']
        user_password = request.form['u_password']
        user = User(user_name = user_name, user_password = user_password, user_role = 'Patient')
        db.session.add(user)

        # add as a patient
        contact_info = request.form['contact_info']
        patient_email = request.form['email']
        patient_age = request.form['p_age']
        patient_user_id = User.query.filter(User.user_name == user_name).first()
        patient = Patient(patient_name = patient_name, contact_info = contact_info, patient_email = patient_email, patient_user_id = patient_user_id.user_id, patient_age = patient_age)
        db.session.add(patient)
        db.session.commit()
        return redirect(f'/patient/{patient_user_id.user_id}') 

@app.route('/book-appointment', methods = ['GET', 'POST'])
def book_appointment():
    if request.method == 'GET':
        global date_today 
        patients = Patient.query.all()
        departments = Department.query.all()
        doctors = Doctor.query.all()
        appointment_dict = {i:0  for i in doctors}

        for i in doctors:
            lst = []
            lst += SlotSchedules.query.filter(SlotSchedules.slot_doctor_id == i.doctor_id, SlotSchedules.date >= date_today, or_(SlotSchedules.status != 'Cancelled', SlotSchedules.status == None)).order_by(SlotSchedules.date, SlotSchedules.schedule_slot_id).all()
            appointment_dict[i] = lst
        return render_template('patient/book-appointment.html', departments = departments, patients = patients, doctors = doctors, appointment_dict = appointment_dict)
    
@app.route('/confirm-appointment/<int:did>', methods = ['GET', 'POST'])
def confirm_appointment(did):
    if request.method == 'GET':
        doctor = db.get_or_404(Doctor, did)
        global date_today 
        doctor_slots = SlotSchedules.query.filter(and_(SlotSchedules.slot_doctor_id == doctor.doctor_id, SlotSchedules.date >= date_today, or_(SlotSchedules.status != 'Cancelled', SlotSchedules.status == None))).order_by(SlotSchedules.date, SlotSchedules.schedule_slot_id).all()
        return render_template('patient/confirm-appointment.html', doctor = doctor, doctor_slots = doctor_slots, flag = False)
    else: 
        doctor = Doctor.query.filter(Doctor.doctor_id == did).first()
        doctor_slots = SlotSchedules.query.filter(and_(SlotSchedules.slot_doctor_id == doctor.doctor_id, SlotSchedules.date >= date_today)).all()

        form_content = request.form 
        form_content_to_dict = form_content.to_dict(flat = False)

        patient_name = form_content_to_dict['patient_name']
        patient = Patient.query.filter(Patient.patient_name == patient_name[0]).first()
        if patient == None:
            return render_template('patient/confirm-appointment.html', doctor = doctor, doctor_slots = doctor_slots, flag = True)
        slots = []

        for slot in form_content_to_dict.keys():
            if slot != 'patient_name':
                slots += [slot]

        for slot in slots:
            slot = SlotSchedules.query.filter(SlotSchedules.schedule_id == slot).first()
            if slot.slot_patient_id == None:
                slot.status = 'Booked'
                slot.slot_patient_id = patient.patient_id
                    
                slot.slot_sch_appointment_rel = Appointment(date_time = slot.date, doctor_id = doctor.doctor_id, patient_id = patient.patient_id)
                slot.slot_sch_appointment_rel.t = Treatment(status = 'Booked')
                db.session.add(slot)
            else:
                new_entry = SlotSchedules(date = slot.date, slot_doctor_id = slot.slot_doctor_id, slot_patient_id = patient.patient_id, schedule_slot_id = slot.schedule_slot_id, status = 'Booked')
                new_entry.slot_sch_appointment_rel = Appointment(date_time = slot.date, doctor_id = doctor.doctor_id, patient_id = patient.patient_id)
                new_entry.slot_sch_appointment_rel.t = Treatment(status = 'Booked')
                db.session.add(new_entry)

        db.session.commit()
        return redirect('/admin')
