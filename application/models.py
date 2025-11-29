from .database import db
from datetime import datetime, timedelta, date
import bcrypt

# User Specific Tables: User, Patient, Doctor
# Doctor Specific Tables: Appointment, Treatment, SlotSchedules
# Slots
# Patient-Doctor Notification Tables: AvailabilityNotifications, PatientDoctorNotifications
# Patient-Admin Notification Tables: AdminPatientNotifications
# Doctor-Admin Notification Tables: AdminDoctorNotifications
# ProfilePictures

# One-to-One relationships: User-Admin, User-Doctor, User-Patient, Appointment-Treatment, Treatment-DieticianNotes, Appointment-SlotSchedules
# One-to-Many relationships: ProfilePictures-Department, ProfilePictures-Doctor, ProfilePictures-Patients, Slot-SlotSchedules, Patient-AvailabilityNotifications, 
# Doctor-AvailabilityNotifications, Doctor-PatientDoctorNotifications, Patient-PatientDoctorNotifications, Doctor-AdminDoctorNotifications , Patient-AdminPatientNotifications 

class User(db.Model):
    __tablename__ = 'user'
    user_id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    user_name = db.Column(db.String(32), nullable = False, unique = True)
    user_password = db.Column(db.String(32), nullable = False)
    user_role = db.Column(db.String)

    admin_relationship = db.relationship('Admin', back_populates = 'a', uselist = False)
    doctor_relationship = db.relationship('Doctor', back_populates = 'd', uselist = False)
    patient_relationship = db.relationship('Patient', back_populates = 'p', uselist = False)

    def is_authenticated(self):
        return False    
    def is_active(self):
        return False 
    def is_anonymous(self):
        return False
    def get_id(self):
        return str(self.user_id)

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
    department_description = db.Column(db.String, default = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum')
    status = db.Column(db.String) # DeletedbyAdmin

    department_profile_picture = db.Column(db.Integer, db.ForeignKey('profile_pictures.name'))
    
    doctors = db.relationship('Doctor', back_populates = 'dept')
    department_pfp = db.relationship('ProfilePictures', back_populates = 'pfp_department')

class Doctor(db.Model):
    __tablename__ = 'doctor'
    doctor_id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    doctor_name = db.Column(db.String(64), nullable = False)
    doctor_contact_number = db.Column(db.String, nullable = False)
    doctor_email = db.Column(db.String)
    doctor_dob = db.Column(db.Date, nullable = False)
    doctor_blacklisted = db.Column(db.Boolean, default = False)
    doctor_desc = db.Column(db.String, default = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum')
    doctor_gender = db.Column(db.String)
    status = db.Column(db.String) # DeletedbyAdmin

    doctor_profile_picture = db.Column(db.String, db.ForeignKey('profile_pictures.name'))
    department_id = db.Column(db.Integer, db.ForeignKey(Department.department_id))
    doctor_user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))

    dept = db.relationship('Department', back_populates = 'doctors')
    d = db.relationship('User', back_populates = 'doctor_relationship')
    appointment_d = db.relationship('Appointment', back_populates = 'd_ref')
    doctor_slot = db.relationship('SlotSchedules', back_populates = 'slot_doctor')
    doctor_notif = db.relationship('AvailabilityNotifications', back_populates = 'notif_doctor')
    doctor_pfp = db.relationship('ProfilePictures', back_populates = 'pfp_doctor')
    doctor_pdn = db.relationship('PatientDoctorNotifications', back_populates = 'pdn_doctor')
    doctor_adn = db.relationship('AdminDoctorNotifications', back_populates = 'adn_doctor')

class Patient(db.Model):
    __tablename__ = 'patient'
    patient_id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    patient_name = db.Column(db.String(64), nullable = False)
    contact_info = db.Column(db.String(10), nullable = False)
    patient_gender = db.Column(db.String)
    patient_email = db.Column(db.String)
    patient_dob = db.Column(db.Date, nullable = False)
    patient_blacklisted = db.Column(db.Boolean, default = False)
    patient_age = db.Column(db.Integer)
    patient_height = db.Column(db.String, default = '--')
    patient_weight = db.Column(db.String, default = '--')
    status = db.Column(db.String) # DeletedbyAdmin

    patient_profile_picture = db.Column(db.String, db.ForeignKey('profile_pictures.name'))
    patient_user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))

    p = db.relationship('User', back_populates = 'patient_relationship')
    appointment_p = db.relationship('Appointment', back_populates = 'p_ref', uselist = False)
    patient_slot = db.relationship('SlotSchedules', back_populates = 'slot_patient')
    patient_notif = db.relationship('AvailabilityNotifications', back_populates = 'notif_patient')
    patient_pfp = db.relationship('ProfilePictures', back_populates = 'pfp_patient')
    patient_pdn = db.relationship('PatientDoctorNotifications', back_populates = 'pdn_patient')
    patient_apn = db.relationship('AdminPatientNotifications', back_populates = 'apn_patient')

class Appointment(db.Model):
    __tablename__ = 'appointment'
    appointment_id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    date_time = db.Column(db.Date, nullable = False, default = datetime.now)

    t_id = db.Column(db.Integer, db.ForeignKey('treatment.treatment_id'))
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctor.doctor_id'))
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.patient_id'))
    s_sch_id = db.Column(db.Integer, db.ForeignKey('slot_schedules.schedule_id'))

    d_ref = db.relationship('Doctor', back_populates = 'appointment_d')
    p_ref = db.relationship('Patient', back_populates = 'appointment_p')
    t = db.relationship('Treatment', back_populates = 'ap', uselist = False)
    appointment_sch = db.relationship('SlotSchedules', back_populates = 'slot_sch_appointment_rel')

class Treatment(db.Model):
    __tablename__ = 'treatment'
    treatment_id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    status = db.Column(db.String)
    diagnosis = db.Column(db.String) 
    prescription = db.Column(db.String)
    notes = db.Column(db.String)    
    tests = db.Column(db.String)
    diet_type = db.Column(db.String)

    ap = db.relationship('Appointment', back_populates = 't')
    treatment_dn = db.relationship('DieticianNotes', back_populates = 'dn_treatment', uselist = False)

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
    slot_sch_appointment_rel = db.relationship('Appointment', back_populates = 'appointment_sch', uselist = False)

class AvailabilityNotifications(db.Model):
    __tablename__ = 'availability_notifications'
    notification_id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    date = db.Column(db.Date, default = datetime.now)
    patient_message_received = db.Column(db.Boolean, default = False)
    doctor_available = db.Column(db.Boolean, default = False)

    notif_doctor_id = db.Column(db.Integer, db.ForeignKey('doctor.doctor_id'))
    notif_patient_id = db.Column(db.Integer, db.ForeignKey('patient.patient_id'))

    notif_doctor = db.relationship('Doctor', back_populates = 'doctor_notif')
    notif_patient = db.relationship('Patient', back_populates = 'patient_notif')

class ProfilePictures(db.Model):
    __tablename__ = 'profile_pictures'
    picture_id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.String)
    role = db.Column(db.String)

    pfp_doctor = db.relationship('Doctor', back_populates = 'doctor_pfp')
    pfp_patient = db.relationship('Patient', back_populates = 'patient_pfp')
    pfp_department = db.relationship('Department', back_populates = 'department_pfp')

class PatientDoctorNotifications(db.Model):
    __tablename__ = 'patient_doctor_notifications'
    message_id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    message_type = db.Column(db.String) #Doctor_Notifications, Thank_you_message: Messages from patients; TreatmentDetails; AppointmentCancelled
    message_content = db.Column(db.String)
    role = db.Column(db.String) #message sent from 
    patient_message_received = db.Column(db.Boolean, default = False)
    doctor_message_received = db.Column(db.Boolean, default = False)
    message_date_time = db.Column(db.DateTime, default = datetime.now)
    appointment_id = db.Column(db.Integer)

    m_doctor_id = db.Column(db.Integer, db.ForeignKey('doctor.doctor_id'))
    m_patient_id = db.Column(db.Integer, db.ForeignKey('patient.patient_id'))

    pdn_doctor = db.relationship('Doctor', back_populates = 'doctor_pdn')
    pdn_patient = db.relationship('Patient', back_populates = 'patient_pdn')

class AdminPatientNotifications(db.Model):
    __tablename__ = 'admin_patient_notifications'
    admin_patient_message_id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    admin_patient_message_type = db.Column(db.String) #WelcomeMessage, 
    admin_patient_message_content = db.Column(db.String)
    patient_message_received = db.Column(db.Boolean, default = False)
    admin_message_received = db.Column(db.Boolean, default = False)
    message_date_time = db.Column(db.DateTime, default = datetime.now)
    role = db.Column(db.String) #message sent from      Admin, Patient

    message_patient_id = db.Column(db.Integer, db.ForeignKey('patient.patient_id'))

    apn_patient = db.relationship('Patient', back_populates = 'patient_apn')

class AdminDoctorNotifications(db.Model):
    __tablename__ = 'admin_doctor_notifications'
    admin_doctor_message_id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    admin_doctor_message_type = db.Column(db.String)
    admin_doctor_message_content = db.Column(db.String)
    doctor_message_received = db.Column(db.Boolean, default = False)
    admin_message_received = db.Column(db.Boolean, default = False)
    message_date_time = db.Column(db.DateTime, default = datetime.now)
    role = db.Column(db.String) #message sent from      Admin, Doctor

    message_doctor_id = db.Column(db.Integer, db.ForeignKey('doctor.doctor_id'))

    adn_doctor = db.relationship('Doctor', back_populates = 'doctor_adn')

class DieticianNotes(db.Model):
    __tablename__ = 'dietician_notes'
    d_notes_id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    status = db.Column(db.String, default = 'Pending')
    doctor_instructions = db.Column(db.String)
    patient_id = db.Column(db.String)
    morning_plan = db.Column(db.String, default = 'Will be provided soon')
    afternoon_plan = db.Column(db.String, default = 'Will be provided soon')
    evening_plan = db.Column(db.String, default = 'Will be provided soon')
    additional_notes = db.Column(db.String)

    treatment_id = db.Column(db.Integer, db.ForeignKey('treatment.treatment_id'))

    dn_treatment = db.relationship('Treatment', back_populates = 'treatment_dn')