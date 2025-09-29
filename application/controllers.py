from flask import Flask, render_template, request, redirect
from application.models import *
from app import app
import datetime

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
@app.route('/admin', methods = ['GET'])
def admin_dashboard():
    if request.method == 'GET':
        return render_template('admin/admin-dashboard.html')

# Doctor    
@app.route('/doctor/<int:d_id>', methods = ['GET'])
def doctor_dashboard(d_id):
    if request.method == 'GET':
        doctor = Doctor.query.filter(Doctor.doctor_id == d_id).first()
        return render_template('doctor/doctor-dashboard.html')

# Patient
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


