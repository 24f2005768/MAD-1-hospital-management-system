from .database import db
from datetime import datetime, timedelta, date

# relationshps
#  User - Doctor, User - Patient, User - Admin, Appointment - Treatment : One-to-one
#  Department - Doctor : One-to-many

class User(db.Model):
    __tablename__ = 'user'
    user_id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    user_name = db.Column(db.String(32), nullable = False, unique = True)
    user_password = db.Column(db.String, nullable = False)
    user_role = db.Column(db.String)

    admin_relationship = db.relationship('Admin', back_populates = 'a', uselist = False)
    doctor_relationship = db.relationship('Doctor', back_populates = 'd', uselist = False)
    patient_relationship = db.relationship('Patient', back_populates = 'p', uselist = False)

class Admin(db.Model):
    __tablename__ = 'admin'
    admin_id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    admin_name = db.Column(db.String, nullable = False)
    admin_password = db.Column(db.String, nullable = False)

    admin_user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))

    a = db.relationship('User', back_populates = 'admin_relationship')
    
class Department(db.Model):
    __tablename__ = 'department'
    department_id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    department_name = db.Column(db.String, nullable = False)
    department_description = db.Column(db.String)

    doctors = db.relationship('Doctor', back_populates = 'dept')

class Doctor(db.Model):
    __tablename__ = 'doctor'
    doctor_id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    doctor_name = db.Column(db.String, nullable = False)
    doctor_contact_number = db.Column(db.String, nullable = False)
    doctor_email = db.Column(db.String)
    doctor_blacklisted = db.Column(db.Boolean, default = False)
    doctor_desc = db.Column(db.String)

    department_id = db.Column(db.Integer, db.ForeignKey(Department.department_id))
    doctor_user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))

    dept = db.relationship('Department', back_populates = 'doctors')
    d = db.relationship('User', back_populates = 'doctor_relationship')
    appointment_d = db.relationship('Appointment', back_populates = 'd_ref')
    doctor_slot = db.relationship('SlotSchedules', back_populates = 'slot_doctor')

class Patient(db.Model):
    __tablename__ = 'patient'
    patient_id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    patient_name = db.Column(db.String, nullable = False)
    contact_info = db.Column(db.String(10), nullable = False)
    patient_gender = db.Column(db.String)
    patient_email = db.Column(db.String)
    patient_blacklisted = db.Column(db.Boolean, default = False)
    patient_age = db.Column(db.Integer)

    patient_user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))

    p = db.relationship('User', back_populates = 'patient_relationship')
    appointment_p = db.relationship('Appointment', back_populates = 'p_ref', uselist = False)
    patient_slot = db.relationship('SlotSchedules', back_populates = 'slot_patient')

class Appointment(db.Model):
    __tablename__ = 'appointment'
    appointment_id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    date_time = db.Column(db.Date, nullable = False, default = datetime.now)

    t_id = db.Column(db.Integer, db.ForeignKey('treatment.treatment_id'))
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctor.doctor_id'))
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.patient_id'))

    d_ref = db.relationship('Doctor', back_populates = 'appointment_d')
    p_ref = db.relationship('Patient', back_populates = 'appointment_p')
    t = db.relationship('Treatment', back_populates = 'ap', uselist = False)

class Treatment(db.Model):
    __tablename__ = 'treatment'
    treatment_id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    status = db.Column(db.String)
    diagnosis = db.Column(db.String) 
    prescription = db.Column(db.String)
    notes = db.Column(db.String)    
    tests = db.Column(db.String)

    ap = db.relationship('Appointment', back_populates = 't')

class Slot(db.Model):
    __tablename__ = 'slot'
    slot_id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    slot_name = db.Column(db.String)
    slot_time = db.Column(db.String)

    s_schedule = db.relationship('SlotSchedules', back_populates = 's_sch')

class SlotSchedules(db.Model):
    __tablename__ = 'slot_schedules'
    schedule_id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    date = db.Column(db.Date, default = datetime.now)

    slot_doctor_id = db.Column(db.Integer, db.ForeignKey('doctor.doctor_id'))
    slot_patient_id = db.Column(db.Integer, db.ForeignKey('patient.patient_id'))
    schedule_slot_id = db.Column(db.Integer, db.ForeignKey('slot.slot_id'))

    slot_doctor = db.relationship('Doctor', back_populates = 'doctor_slot')
    slot_patient = db.relationship('Patient', back_populates = 'patient_slot')
    s_sch = db.relationship('Slot', back_populates = 's_schedule')