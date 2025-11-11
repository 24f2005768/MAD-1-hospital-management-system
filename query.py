from app import *
from sqlalchemy import and_, or_, desc
from datetime import date
from dateutil.relativedelta import relativedelta
from flask import url_for

date_today = date.today()
list_of_next_7_dates = [(date_today + timedelta(days = i)) for i in range(8)]

'''
a = Appointment.query.first()
p_id  = a.patient_id
# p_name = Patient.query.filter(Patient.patient_id == p_id).first()
# print(p_id)
print(a.date_time.date)
'''


# did = 2
# a = Appointment.query.filter(Appointment.doctor_id == did).all()
# lst = []
# for p in a:
#     lst += [(p.appointment_id, p.p_ref.patient_name, p.t.diagnosis, p.t.notes, p.t.prescription)]
# print(lst)

# pid = 1
# did = 3
# a = Appointment.query.filter(and_(Appointment.patient_id == pid, Appointment.doctor_id == did)).all()
# print(a)

# date_today = date.today()
# d = [i for i in range(8)]
# d_list = []
# for i in d:
#     d_list += [(date_today + timedelta(days = i))]
# print(d_list)

# l = [(date_today + timedelta(days = i)) for i in range(8)]
# print(l)

# can add a sch manually

# sch1 = SlotSchedules(slot_doctor_id = 1, slot_patient_id = 2, schedule_slot_id = 2)
# db.session.add(sch1)
# db.session.commit()

# doctor can give their slots on a date
# d1 = db.get_or_404(Doctor, 4)
# t1 = SlotSchedules(slot_doctor_id = d1.doctor_id, schedule_slot_id = 1)
# t2 = SlotSchedules(slot_doctor_id = d1.doctor_id, schedule_slot_id = 2)
# db.session.add(t1)
# db.session.add(t2)
# db.session.commit()

# d2 = db.get_or_404(Doctor, 3)


# patient will book first slot

# d1 = db.get_or_404(Doctor, 4)
# p1 = db.get_or_404(Patient, 4)
# pt1 = SlotSchedules.query.filter(SlotSchedules.slot_doctor_id == d1.doctor_id).all()
# w = db.get_or_404(Slot, 1)
# slot_app_1 = SlotSchedules.query.filter(and_(SlotSchedules.slot_doctor_id == d1.doctor_id, SlotSchedules.schedule_slot_id == w.slot_id)).first()
# slot_app_1.slot_patient_id = p1.patient_id
# db.session.commit()

# import datetime
# x = datetime.date(2025, 9, 28)

# a = {'1': ['2025-09-26', '2025-09-27', '2025-09-28'], '2': ['2025-09-28']}
# d_id = 2

# slot1 = Slot.query.filter(Slot.slot_id == 2).first()
# s1 = SlotSchedules (slot_doctor_id = d_id, schedule_slot_id = slot1.slot_id, date = x)
# db.session.add(s1)
# db.session.commit()

# for s in a.keys():
#     slot_id = Slot.query.filter(Slot.slot_id == s).first()
#     for x in a[s]:
#         y = int(x[0:4])
#         m = int(x[5:7])
#         d = int(x[8:9])
#         slot_date = datetime.date(y,m,d)
#         slot = SlotSchedules(slot_doctor_id = d_id, schedule_slot_id = slot_id.slot_id, date = slot_date)
#         db.session.add(slot)
# db.session.commit()

# departments = Department.query.all()
# for dept in departments:
#     for doc in dept.doctors:
#         print(doc.doctor_name)

'''
doctor = db.get_or_404(Doctor, 3)

# print(doctor.doctor_slot)
# for sch in doctor.doctor_slot:
    # print(sch.date) #all

date_today = date.today()
for sch in doctor.doctor_slot:
    # print(sch.date)
    if date_today >  sch.date:
        print(sch.date, 'I am working: PREV') #prev

for sch in doctor.doctor_slot:
    # print(sch.date)
    if date_today <  sch.date:
        print(sch.date,'I am working: UPCOMING') #prev
'''
# Book an Appointment

'''
doctor = db.get_or_404(Doctor, 3)

patient1 = db.get_or_404(Patient, 1)
patient2 = db.get_or_404(Patient, 5)
patient3 = db.get_or_404(Patient, 4)
patient4 = db.get_or_404(Patient, 3)
patient5 = db.get_or_404(Patient, 2)

available_slots = SlotSchedules.query.filter(and_(SlotSchedules.slot_doctor_id == doctor.doctor_id, SlotSchedules.schedule_slot_id == 1)).all()
# print(available_slots)

book_slot1 = available_slots[0]
if book_slot1.slot_patient_id == None:
    book_slot1.slot_patient_id = patient1.patient_id
    db.session.add(book_slot1)
    appointment = Appointment(date_time = available_slots[0].date, doctor_id = doctor.doctor_id, patient_id = patient1.patient_id)
    appointment.t = Treatment(diagnosis = '--', prescription = '--', notes = '--', tests = '--')
    db.session.add(appointment)

book_slot2 = available_slots[1]
if book_slot2.slot_patient_id == None:
    book_slot2.slot_patient_id = patient2.patient_id
    db.session.add(book_slot2)
    appointment = Appointment(date_time = available_slots[1].date, doctor_id = doctor.doctor_id, patient_id = patient2.patient_id)
    appointment.t = Treatment(diagnosis = '--', prescription = '--', notes = '--', tests = '--')
    db.session.add(appointment)

book_slot3 = available_slots[2]
if book_slot3.slot_patient_id == None:
    book_slot3.slot_patient_id = patient3.patient_id
    db.session.add(book_slot3)
    appointment = Appointment(date_time = available_slots[2].date, doctor_id = doctor.doctor_id, patient_id = patient3.patient_id)
    appointment.t = Treatment(diagnosis = '--', prescription = '--', notes = '--', tests = '--')
    db.session.add(appointment)

book_slot4 = available_slots[3]
if book_slot4.slot_patient_id == None: #prevent double booking
    book_slot4.slot_patient_id = patient1.patient_id
    db.session.add(book_slot4)
    appointment = Appointment(date_time = available_slots[3].date, doctor_id = doctor.doctor_id, patient_id = patient1.patient_id)
    appointment.t = Treatment(diagnosis = '--', prescription = '--', notes = '--', tests = '--')
    db.session.add(appointment)


# book_slot5 = available_slots[3]
# book_slot5.slot_patient_id = patient5.patient_id
# db.session.add(book_slot5)

# appointment = Appointment(date_time = available_slots[3].date, doctor_id = doctor.doctor_id, patient_id = patient5.patient_id)
# appointment.t = Treatment(diagnosis = '--', prescription = '--', notes = '--', tests = '--')
# db.session.add(appointment)

db.session.commit()
'''

# Multiple patients booking one slot

# patient = db.get_or_404(Patient,2)
# slots = ['1', '34']
# for slot in slots:
#     s = SlotSchedules.query.filter(SlotSchedules.schedule_id == slot).first()
#     if s.slot_patient_id == None:
#         s.slot_patient_id = patient.patient_id
#         s.status = 'Booked'
#     else:
#         new_entry = SlotSchedules(date = s.date, status = 'Booked', slot_doctor_id = s.slot_doctor_id, slot_patient_id = patient.patient_id, schedule_slot_id = s.schedule_slot_id)
#         db.session.add(new_entry)
# db.session.commit()

# new_appointment = Appointment(patient_id = 3, doctor_id = 1, date_time = date_today)
# new_appointment.t = diagnosis = Treatment(diagnosis = '1', prescription = '1', notes = '1', tests = '1', status = '1')
# db.session.add(new_appointment)

# new_appointment = Appointment(patient_id = 3, doctor_id = 1, date_time = date(2025, 12, 26))
# new_appointment.t = diagnosis = Treatment(diagnosis = '2', prescription = '2', notes = '2', tests = '2', status = '2')
# db.session.add(new_appointment)
# db.session.commit()

# did, pid = 1,3
# patient = Appointment.query.filter(and_(Appointment.doctor_id == did, Appointment.patient_id == pid)).order_by(Appointment.date_time).all()
# print(patient)
# if len(patient) == 1:
#     print(patient[0].date_time)
# else:
#     print(patient[-1].date_time)

# tid = 1
# list_of_options = ['Completed', 'Booked', 'Cancelled']
# treatment = Treatment.query.filter(Treatment.treatment_id == tid).first()
# # print(treatment.status)
# for option in list_of_options:
#     if option == treatment.status:
#         print('HI', option)


# sid = 31

# slot = SlotSchedules.query.filter(SlotSchedules.schedule_id == sid).first()
# # print(slot.date)
# slot_date = slot.date

# all_appointments = SlotSchedules.query.filter(and_(SlotSchedules.date == slot_date, SlotSchedules.schedule_slot_id == slot.schedule_slot_id)).all()
# # print(all_appointments)

# date_today = date.today()
# did = 2

# appointments_today = SlotSchedules.query.filter(and_(SlotSchedules.date == date_today, SlotSchedules.slot_doctor_id == did)).all()
# list_of_next_7_dates = [(date_today + timedelta(days = i)) for i in range(1,8)]

# for d in list_of_next_7_dates:
#     print(SlotSchedules.query.filter(and_(SlotSchedules.date == d, SlotSchedules.slot_doctor_id == did)).all())
'''
list_of_next_7_dates = [(date_today + timedelta(days = i)) for i in range(1,8)]
# print(list_of_next_7_dates)

slot1 = db.get_or_404(Slot, 1)
slot2 = db.get_or_404(Slot, 2)
slot3 = db.get_or_404(Slot, 3)

patient1 = db.get_or_404(Patient, 1)
patient2 = db.get_or_404(Patient, 2)
patient3 = db.get_or_404(Patient, 3)
patient4 = db.get_or_404(Patient, 4)
patient5 = db.get_or_404(Patient, 5)
patient6 = db.get_or_404(Patient, 6)
patient7 = db.get_or_404(Patient, 7)
patient8 = db.get_or_404(Patient, 8)
patient9 = db.get_or_404(Patient, 9)

# D1
doctor = db.get_or_404(Doctor, 1)
# slot_for_doctor1 = SlotSchedules(date = date.today(), slot_doctor_id = doctor.doctor_id, schedule_slot_id = slot1.slot_id, slot_patient_id = patient1.patient_id)
slot_for_doctor2 = SlotSchedules(date = list_of_next_7_dates[1], slot_doctor_id = doctor.doctor_id, schedule_slot_id = slot2.slot_id, slot_patient_id = patient8.patient_id)
# slot_for_doctor3 = SlotSchedules(date = list_of_next_7_dates[2], slot_doctor_id = doctor.doctor_id, schedule_slot_id = slot1.slot_id)
# slot_for_doctor4 = SlotSchedules(date = list_of_next_7_dates[5], slot_doctor_id = doctor.doctor_id, schedule_slot_id = slot3.slot_id)
# db.session.add(slot_for_doctor1)
db.session.add(slot_for_doctor2)
# db.session.add(slot_for_doctor3)
# db.session.add(slot_for_doctor4)

available_slots = SlotSchedules.query.filter(and_(SlotSchedules.slot_doctor_id == doctor.doctor_id, SlotSchedules.date >= date_today)).all()

# today's appointments for D1
# if slot_for_doctor1.slot_patient_id != None:
#     book_slot1 = available_slots[0]
#     slot = book_slot1
#     new_entry1 = SlotSchedules(date = slot.date, slot_doctor_id = slot.slot_doctor_id, slot_patient_id = patient2.patient_id, schedule_slot_id = slot.schedule_slot_id)
#     db.session.add(new_entry1)
#     appointment = Appointment(date_time = slot.date, doctor_id = doctor.doctor_id, patient_id = patient2.patient_id)
#     appointment.t = Treatment(status = 'Booked')
#     db.session.add(appointment)

#     new_entry2 = SlotSchedules(date = slot.date, slot_doctor_id = slot.slot_doctor_id, slot_patient_id = patient3.patient_id, schedule_slot_id = slot.schedule_slot_id)
#     db.session.add(new_entry2)
#     appointment = Appointment(date_time = slot.date, doctor_id = doctor.doctor_id, patient_id = patient3.patient_id)
#     appointment.t = Treatment(status = 'Booked')
#     db.session.add(appointment)


# next week's appointments for D1
if slot_for_doctor2.slot_patient_id != None:
    book_slot1 = available_slots[1]
    slot = book_slot1
    new_entry1 = SlotSchedules(date = slot.date, slot_doctor_id = slot.slot_doctor_id, slot_patient_id = patient1.patient_id, schedule_slot_id = slot.schedule_slot_id)
    db.session.add(new_entry1)
    appointment = Appointment(date_time = slot.date, doctor_id = doctor.doctor_id, patient_id = patient1.patient_id)
    appointment.t = Treatment(status = 'Booked')
    db.session.add(appointment)

db.session.commit()
'''
# list_of_next_7_dates = [(date_today + timedelta(days = i)) for i in range(1,8)]
# slots = Slot.query.all()
# doctor = db.get_or_404(Doctor, 3)
# da_dict = {}
# doctor_slots = SlotSchedules.query.filter(and_(SlotSchedules.slot_doctor_id == doctor.doctor_id, SlotSchedules.date >= date_today)).order_by(SlotSchedules.date, SlotSchedules.schedule_slot_id).all()
# print(doctor_slots)

# for d in list_of_next_7_dates:
#     da_dict[d] = {}
#     for s in slots:
#         query = SlotSchedules.query.filter(SlotSchedules.date == d, SlotSchedules.schedule_slot_id == s.slot_id).all()
#         da_dict[d][s] = query

# print(da_dict)

# notif1 = AdminPatientNotifications(message_patient_id = 3, admin_patient_message_type = 'Welcome to LDH Hospital', admin_patient_message_content = 'Greetings from LDH Hospital')
# notif2 = AdminPatientNotifications(message_patient_id = 3, admin_patient_message_type = 'You can book appointments now', admin_patient_message_content = 'You can book appointments now')

# notif3 = PatientDoctorNotifications(m_patient_id = 3, m_doctor_id = 3, role = 'Doctor', message_type = 'Booking Confirmation', message_content = 'Thank You for trusting LDH Hospital')
# notif4 = PatientDoctorNotifications(m_patient_id = 3, m_doctor_id = 2, role = 'Doctor', message_type = 'Booking Confirmation', message_content = 'Thank You for trusting LDH Hospital')

# db.session.add(notif1)
# db.session.add(notif2)
# db.session.add(notif3)
# db.session.add(notif4)
# db.session.commit()

# doctor = db.get_or_404(Doctor, 1)
# slot3 = db.get_or_404(Slot, 3)
# s = SlotSchedules(date = date(2025,10,6), slot_doctor_id = doctor.doctor_id, schedule_slot_id = slot3.slot_id)
# # db.session.add(s)
# # db.session.commit()

# available_slots = SlotSchedules.query.filter(SlotSchedules.slot_doctor_id == doctor.doctor_id).all()
# book_slot3 = available_slots[0]
# patient1 = db.get_or_404(Patient, 1)

# book_slot3.slot_patient_id = patient1.patient_id
# book_slot3.slot_sch_appointment_rel = Appointment(date_time = available_slots[0].date, doctor_id = doctor.doctor_id, patient_id = patient1.patient_id)
# book_slot3.slot_sch_appointment_rel.t = Treatment(diagnosis = 'Follow Up after emergency surgery', prescription = 'Calcium Syrup', notes = 'Leg fracture due to accident', tests = 'X-Ray', status = 'Completed')
# # db.session.add(book_slot3)

# message = PatientDoctorNotifications(message_content = f"Hi, now you can check your treatment details for today's appointment with { doctor.doctor_name }.", message_type = 'Treatment Details', role = 'Doctor', m_doctor_id = f'{ doctor.doctor_id }', m_patient_id = book_slot3.slot_patient_id)
# db.session.add(message)


unread_message = PatientDoctorNotifications(message_type = 'unread', message_content = '--', m_doctor_id = 1, m_patient_id = 1)
read_message = PatientDoctorNotifications(message_type = 'read', message_content = '--', m_doctor_id = 1, m_patient_id = 1, doctor_message_recieved = 1)
db.session.add(unread_message)
db.session.add(read_message)

unread_message1 = AdminDoctorNotifications(admin_doctor_message_type = 'unread', admin_doctor_message_content = '--', message_doctor_id = 1)
read_message1 = AdminDoctorNotifications(admin_doctor_message_type = 'read', admin_doctor_message_content = '--', message_doctor_id = 1, doctor_message_recieved = 1)

db.session.add(unread_message1)
db.session.add(read_message1)

db.session.commit()