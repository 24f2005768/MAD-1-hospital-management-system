from app import *

# # if database file is deleted, run this file to populate db


# patients 

user1 = User(user_name = 'Shr_arya', user_password = '921369', user_role = 'Patient')
user1.patient_relationship = Patient(patient_name = 'Arya', contact_info = '887654123', patient_email = 'a@email.com', patient_age = 18, patient_gender = 'Male')

user2 = User(user_name = 'Little_deer', user_password = 'kriti', user_role = 'Patient')
user2.patient_relationship = Patient(patient_name = 'Kriti', contact_info = '963261297', patient_email = 'k@email.com', patient_age = 21, patient_gender = 'Female')

user3 = User(user_name = 'Mummy', user_password = 'mom', user_role = 'Patient')
user3.patient_relationship = Patient(patient_name = 'Saroj', contact_info = '9828646464', patient_email = 's@email.com', patient_age = 48, patient_gender = 'Female')

user4 = User(user_name = 'Aadi', user_password = 'aadi', user_role = 'Patient')
user4.patient_relationship = Patient(patient_name = 'Aadi', contact_info = '77734568', patient_email = 'a@email.com', patient_age = 20, patient_gender = 'Male')

user5 = User(user_name = 'Shruti', user_password = 'shruti', user_role = 'Patient')
user5.patient_relationship = Patient(patient_name = 'Shruti', contact_info = '881254466', patient_email = 'sh@email.com', patient_age = 24, patient_gender = 'Female')

db.session.add(user1)
db.session.add(user2)
db.session.add(user3)
db.session.add(user4)
db.session.add(user5)
db.session.commit()

# # doctors and departments 

dept1 = Department(department_name = 'Cardiology', department_description = 'LDH offers a comprehensive cardiology program dedicated to the prevention, diagnosis, and treatment of a full spectrum of heart-related conditions. We provide a complete breadth of both invasive and noninvasive cardiovascular services, supported by ongoing research initiatives. Our highly skilled clinicians specialize in managing complex cases, delivering individualized treatment plans tailored to each patient"s unique needs. This patient-centered approach ensures that every individual receives the most advanced and appropriate care for their specific cardiovascular health journey.')
db.session.add(dept1)

user1 = User(user_name = 'Ganesh_heart', user_password = 'ganesh', user_role = 'Doctor')
user1.doctor_relationship = Doctor(doctor_name = 'Ganesh', doctor_contact_number = '98755645',
                                   doctor_email = 'g@email.com', department_id = 1, doctor_desc = "Dr. Ganesh is a board-certified cardiologist with over 25 years of experience specializing in interventional cardiology. He is highly skilled in performing complex coronary interventions and has a special clinical interest in preventive cardiology and heart disease management in women. Dr. Ganesh is dedicated to providing compassionate, patient-centered care, developing personalized treatment plans to help his patients achieve their best possible heart health.")

user2 = User(user_name = 'Vignesh_heart', user_password = 'vignesh', user_role = 'Doctor')
user2.doctor_relationship = Doctor(doctor_name = 'Vignesh', doctor_contact_number = '654215453',
                                   doctor_email = 'v@email.com', department_id = 1, doctor_desc = "Dr. Vignesh is a board-certified cardiologist with over 7 years of experience specializing in interventional cardiology. He is highly skilled in performing complex coronary interventions and has a special clinical interest in preventive cardiology and heart disease management in women. Dr. Vignesh is dedicated to providing compassionate, patient-centered care, developing personalized treatment plans to help his patients achieve their best possible heart health.")



dept2 = Department(department_name = 'Pediatrics', department_description = "LDH offers a comprehensive pediatrics program and dedicated pediatricians, all of whom are board-certified and have pursued advanced training in specialized fields such as cardiology and dermatology. This unique combination of general pediatrics and specialized knowledge allows our team to work collaboratively, offering comprehensive care for your child. Together, our pediatricians and pediatric specialists are equipped to accurately diagnose, effectively treat, and proactively help prevent a wide spectrum of childhood conditions, illnesses, and injuries, ensuring the highest standard of health from infancy through adolescence.")
db.session.add(dept2)

user3 = User(user_name = 'Preeti_pediatrics', user_password = 'preeti', user_role = 'Doctor')
user3.doctor_relationship = Doctor(doctor_name = 'Preeti', doctor_contact_number = '5456451315',
                                   doctor_email = 'p@email.com', department_id = 2, doctor_desc = "Dr. Preeti is a board-certified pediatrician with over 19 years of experience dedicated to the health and well-being of children, from newborns to young adults. Known for her warm and compassionate approach, she specializes in preventive care, childhood immunizations, and the management of common childhood illnesses like asthma and allergies. Dr. Preeti believes in building strong, trusting relationships with both her young patients and their families to foster a lifetime of good health.")

user4 = User(user_name = 'Raju_pediatrics', user_password = 'raju', user_role = 'Doctor')
user4.doctor_relationship = Doctor(doctor_name = 'Raju', doctor_contact_number = '4845434621',
                                   doctor_email = 'r@email.com', department_id = 2, doctor_desc = "Dr. Raju is a board-certified pediatrician with over 10 years of experience dedicated to the health and well-being of children, from newborns to young adults. Known for his warm and compassionate approach, he specializes in preventive care, childhood immunizations, and the management of common childhood illnesses like asthma and allergies. Dr. Raju believes in building strong, trusting relationships with both his young patients and their families to foster a lifetime of good health.")



dept3 = Department(department_name = 'General Surgery', department_description = "LDH's General Surgery department is comprised of highly experienced senior surgeons and a specialized clinical team dedicated to achieving optimal patient outcomes. We utilize a modern approach, employing advanced surgical techniques and technology to ensure precision and promote excellent surgical results. Our expertise encompasses the comprehensive care of a wide range of acute and complex conditions, including diseases of the oesophagus, stomach, colon, liver, gallbladder, bile ducts, abdomen, and thyroid gland, as well as the repair of hernias. You can trust our skilled team to provide compassionate and effective surgical solutions.")
db.session.add(dept3)

user5 = User(user_name = 'Dev_surgery', user_password = 'dev', user_role = 'Doctor')
user5.doctor_relationship = Doctor(doctor_name = 'Dev', doctor_contact_number = '785613516',
                                   doctor_email = 'd@email.com', department_id = 3, doctor_desc = "Dr. Dev is a board-certified General Surgeon with over 15 years of experience performing a wide range of abdominal procedures. His clinical expertise includes minimally invasive surgery for conditions of the gallbladder, colon, and hernias, with a dedicated focus on patient safety and achieving optimal recovery outcomes. Dr. Dev is committed to providing clear communication and compassionate care, ensuring his patients feel confident and well-informed at every step of their surgical journey.")

user6 = User(user_name = 'Vikas_surgery', user_password = 'vikas', user_role = 'Doctor')
user6.doctor_relationship = Doctor(doctor_name = 'Vikas', doctor_contact_number = '9889454545',
                                   doctor_email = 'vk@email.com', department_id = 3, doctor_desc = "Dr. Vikas is a board-certified General Surgeon with over 13 years of experience performing a wide range of abdominal procedures. His clinical expertise includes minimally invasive surgery for conditions of the gallbladder, colon, and hernias, with a dedicated focus on patient safety and achieving optimal recovery outcomes. Dr. Vikas is committed to providing clear communication and compassionate care, ensuring his patients feel confident and well-informed at every step of their surgical journey.")

dept4 = Department(department_name = 'Gastrology', department_description = "LDH's Gastrology department is dedicated to providing high-quality, comprehensive care for a wide spectrum of gastrointestinal conditions, including colon cancer, acid reflux, and other complex digestive disorders. We offer a full range of advanced diagnostic and therapeutic procedures to accurately identify and effectively manage issues affecting your digestive health. Our expertise also extends to personalized nutritional guidance, ensuring a holistic approach to your well-being. You can trust our specialized team to deliver exceptional, patient-centered care for all your digestive health needs.")
db.session.add(dept4)

db.session.add(user1)
db.session.add(user2)
db.session.add(user3)
db.session.add(user4)
db.session.add(user5)
db.session.add(user6)
db.session.commit()

# Slots
s1 = Slot(slot_time = '09:00 - 12:00', slot_name = 'Morning')
s2 = Slot(slot_time = '15:00 - 17:00', slot_name = 'Evening')
s3 = Slot(slot_time = '19:00 - 22:00', slot_name = 'Night')
db.session.add(s1)
db.session.add(s2)
db.session.add(s3)
db.session.commit()

# Appointments

slot1 = db.get_or_404(Slot, 1)
slot2 = db.get_or_404(Slot, 2)
slot3 = db.get_or_404(Slot, 3)

patient1 = db.get_or_404(Patient, 1)
patient2 = db.get_or_404(Patient, 5)
patient3 = db.get_or_404(Patient, 4)
patient4 = db.get_or_404(Patient, 3)
patient5 = db.get_or_404(Patient, 2)

# Slots and past appointment bookings for doctor 1

doctor = db.get_or_404(Doctor, 1)

slot_for_doctor1 = SlotSchedules(date = date(2025,10,5), slot_doctor_id = doctor.doctor_id, schedule_slot_id = slot2.slot_id)
slot_for_doctor2 = SlotSchedules(date = date(2025,10,4), slot_doctor_id = doctor.doctor_id, schedule_slot_id = slot1.slot_id)
slot_for_doctor3 = SlotSchedules(date = date(2025,10,3), slot_doctor_id = doctor.doctor_id, schedule_slot_id = slot3.slot_id)
slot_for_doctor4 = SlotSchedules(date = date(2025,10,1), slot_doctor_id = doctor.doctor_id, schedule_slot_id = slot1.slot_id)
db.session.add(slot_for_doctor1)
db.session.add(slot_for_doctor2)
db.session.add(slot_for_doctor3)
db.session.add(slot_for_doctor4)

available_slots = SlotSchedules.query.filter(SlotSchedules.slot_doctor_id == doctor.doctor_id).all()

book_slot1 = available_slots[0]
book_slot1.slot_patient_id = patient4.patient_id
db.session.add(book_slot1)
appointment = Appointment(date_time = available_slots[0].date, doctor_id = doctor.doctor_id, patient_id = patient4.patient_id)
appointment.t = Treatment(diagnosis = 'Chest Pain', prescription = 'Tablets', notes = 'Patient is experiencing chest pain since 5 days', tests = '--', status = 'Completed')
db.session.add(appointment)

book_slot2 = available_slots[1]
book_slot2.slot_patient_id = patient5.patient_id
db.session.add(book_slot2)
appointment = Appointment(date_time = available_slots[1].date, doctor_id = doctor.doctor_id, patient_id = patient5.patient_id)
appointment.t = Treatment(diagnosis = 'Follow up', prescription = '--', notes = 'Follow up after surgery', tests = '--', status = 'Completed')
db.session.add(appointment)

book_slot3 = available_slots[2]
book_slot3.slot_patient_id = patient3.patient_id
db.session.add(book_slot3)
appointment = Appointment(date_time = available_slots[2].date, doctor_id = doctor.doctor_id, patient_id = patient3.patient_id)
appointment.t = Treatment(diagnosis = 'Regular Checkup', prescription = 'Tablets', notes = 'Regular Checkup', tests = '--', status = 'Completed')
db.session.add(appointment)


# Slots and past appointment bookings for doctor 2

doctor = db.get_or_404(Doctor, 2)

slot_for_doctor1 = SlotSchedules(date = date(2025,10,5), slot_doctor_id = doctor.doctor_id, schedule_slot_id = slot1.slot_id)
slot_for_doctor2 = SlotSchedules(date = date(2025,10,2), slot_doctor_id = doctor.doctor_id, schedule_slot_id = slot2.slot_id)
slot_for_doctor3 = SlotSchedules(date = date(2025,10,3), slot_doctor_id = doctor.doctor_id, schedule_slot_id = slot3.slot_id)
slot_for_doctor4 = SlotSchedules(date = date(2025,10,4), slot_doctor_id = doctor.doctor_id, schedule_slot_id = slot1.slot_id)
db.session.add(slot_for_doctor1)
db.session.add(slot_for_doctor2)
db.session.add(slot_for_doctor3)
db.session.add(slot_for_doctor4)

available_slots = SlotSchedules.query.filter(SlotSchedules.slot_doctor_id == doctor.doctor_id).all()

book_slot1 = available_slots[0]
book_slot1.slot_patient_id = patient2.patient_id
db.session.add(book_slot1)
appointment = Appointment(date_time = available_slots[0].date, doctor_id = doctor.doctor_id, patient_id = patient2.patient_id)
appointment.t = Treatment(diagnosis = 'Chest Pain', prescription = 'Tablets', notes = 'Patient is experiencing chest pain since 5 days', tests = '--', status = 'Completed')
db.session.add(appointment)

book_slot2 = available_slots[1]
book_slot2.slot_patient_id = patient1.patient_id
db.session.add(book_slot2)
appointment = Appointment(date_time = available_slots[1].date, doctor_id = doctor.doctor_id, patient_id = patient1.patient_id)
appointment.t = Treatment(diagnosis = 'Follow up', prescription = '--', notes = 'Follow up after surgery', tests = '--', status = 'Completed')
db.session.add(appointment)

book_slot3 = available_slots[2]
book_slot3.slot_patient_id = patient4.patient_id
db.session.add(book_slot3)
appointment = Appointment(date_time = available_slots[2].date, doctor_id = doctor.doctor_id, patient_id = patient4.patient_id)
appointment.t = Treatment(diagnosis = 'Regular Checkup', prescription = 'Tablets', notes = 'Regular Checkup', tests = '--', status = 'Completed')
db.session.add(appointment)


# Slots and past appointment bookings for doctor 3

doctor = db.get_or_404(Doctor, 3)

slot_for_doctor1 = SlotSchedules(date = date(2025,10,9), slot_doctor_id = doctor.doctor_id, schedule_slot_id = slot3.slot_id)
slot_for_doctor2 = SlotSchedules(date = date(2025,10,6), slot_doctor_id = doctor.doctor_id, schedule_slot_id = slot1.slot_id)
slot_for_doctor3 = SlotSchedules(date = date(2025,10,4), slot_doctor_id = doctor.doctor_id, schedule_slot_id = slot2.slot_id)
slot_for_doctor4 = SlotSchedules(date = date(2025,10,4), slot_doctor_id = doctor.doctor_id, schedule_slot_id = slot1.slot_id)
db.session.add(slot_for_doctor1)
db.session.add(slot_for_doctor2)
db.session.add(slot_for_doctor3)
db.session.add(slot_for_doctor4)

available_slots = SlotSchedules.query.filter(SlotSchedules.slot_doctor_id == doctor.doctor_id).all()

book_slot1 = available_slots[0]
book_slot1.slot_patient_id = patient1.patient_id
db.session.add(book_slot1)
appointment = Appointment(date_time = available_slots[0].date, doctor_id = doctor.doctor_id, patient_id = patient1.patient_id)
appointment.t = Treatment(diagnosis = 'Fever', prescription = 'Medicines', notes = 'Patient has fever since 3 days, no signicant pain', tests = '--', status = 'Completed')
db.session.add(appointment)

book_slot2 = available_slots[1]
book_slot2.slot_patient_id = patient4.patient_id
db.session.add(book_slot2)
appointment = Appointment(date_time = available_slots[1].date, doctor_id = doctor.doctor_id, patient_id = patient4.patient_id)
appointment.t = Treatment(diagnosis = 'Regular Checkup', prescription = '--', notes = 'Regular Checkup', tests = 'Blood Test', status = 'Completed')
db.session.add(appointment)

book_slot3 = available_slots[2]
book_slot3.slot_patient_id = patient3.patient_id
db.session.add(book_slot3)
appointment = Appointment(date_time = available_slots[2].date, doctor_id = doctor.doctor_id, patient_id = patient3.patient_id)
appointment.t = Treatment(diagnosis = 'Regular Checkup', prescription = 'Multi-vitamins', notes = 'Patient is recovering well', tests = '--', status = 'Completed')
db.session.add(appointment)

book_slot4 = available_slots[3]
book_slot4.slot_patient_id = patient2.patient_id
db.session.add(book_slot4)
appointment = Appointment(date_time = available_slots[3].date, doctor_id = doctor.doctor_id, patient_id = patient2.patient_id)
appointment.t = Treatment(diagnosis = 'Fever', prescription = 'Medicines and Injections', notes = 'Admitted for 3 days', tests = '--', status = 'Completed')
db.session.add(appointment)


# Slots and past appointment bookings for doctor 4

doctor = db.get_or_404(Doctor, 4)

slot_for_doctor1 = SlotSchedules(date = date(2025,10,8), slot_doctor_id = doctor.doctor_id, schedule_slot_id = slot1.slot_id)
slot_for_doctor2 = SlotSchedules(date = date(2025,10,5), slot_doctor_id = doctor.doctor_id, schedule_slot_id = slot1.slot_id)
slot_for_doctor3 = SlotSchedules(date = date(2025,10,1), slot_doctor_id = doctor.doctor_id, schedule_slot_id = slot2.slot_id)
slot_for_doctor4 = SlotSchedules(date = date(2025,10,4), slot_doctor_id = doctor.doctor_id, schedule_slot_id = slot1.slot_id)
db.session.add(slot_for_doctor1)
db.session.add(slot_for_doctor2)
db.session.add(slot_for_doctor3)
db.session.add(slot_for_doctor4)

available_slots = SlotSchedules.query.filter(SlotSchedules.slot_doctor_id == doctor.doctor_id).all()

book_slot1 = available_slots[0]
book_slot1.slot_patient_id = patient3.patient_id
db.session.add(book_slot1)
appointment = Appointment(date_time = available_slots[0].date, doctor_id = doctor.doctor_id, patient_id = patient3.patient_id)
appointment.t = Treatment(diagnosis = 'Fever', prescription = 'Medicines', notes = 'Patient has fever since 3 days, no signicant pain', tests = '--', status = 'Completed')
db.session.add(appointment)

book_slot2 = available_slots[1]
book_slot2.slot_patient_id = patient2.patient_id
db.session.add(book_slot2)
appointment = Appointment(date_time = available_slots[1].date, doctor_id = doctor.doctor_id, patient_id = patient2.patient_id)
appointment.t = Treatment(diagnosis = 'Regular Checkup', prescription = '--', notes = 'Regular Checkup', tests = 'Blood Test', status = 'Completed')
db.session.add(appointment)

book_slot3 = available_slots[2]
book_slot3.slot_patient_id = patient5.patient_id
db.session.add(book_slot3)
appointment = Appointment(date_time = available_slots[2].date, doctor_id = doctor.doctor_id, patient_id = patient5.patient_id)
appointment.t = Treatment(diagnosis = 'Regular Checkup', prescription = 'Multi-vitamins', notes = 'Patient is recovering well', tests = '--', status = 'Completed')
db.session.add(appointment)


# Slots and past appointment bookings for doctor 5

doctor = db.get_or_404(Doctor, 5)

slot_for_doctor1 = SlotSchedules(date = date(2025,10,7), slot_doctor_id = doctor.doctor_id, schedule_slot_id = slot2.slot_id)
slot_for_doctor2 = SlotSchedules(date = date(2025,10,3), slot_doctor_id = doctor.doctor_id, schedule_slot_id = slot1.slot_id)
slot_for_doctor3 = SlotSchedules(date = date(2025,10,4), slot_doctor_id = doctor.doctor_id, schedule_slot_id = slot3.slot_id)
slot_for_doctor4 = SlotSchedules(date = date(2025,10,4), slot_doctor_id = doctor.doctor_id, schedule_slot_id = slot1.slot_id)
db.session.add(slot_for_doctor1)
db.session.add(slot_for_doctor2)
db.session.add(slot_for_doctor3)
db.session.add(slot_for_doctor4)

available_slots = SlotSchedules.query.filter(SlotSchedules.slot_doctor_id == doctor.doctor_id).all()

book_slot1 = available_slots[0]
book_slot1.slot_patient_id = patient5.patient_id
db.session.add(book_slot1)
appointment = Appointment(date_time = available_slots[0].date, doctor_id = doctor.doctor_id, patient_id = patient5.patient_id)
appointment.t = Treatment(diagnosis = 'Femur Fracture', prescription = 'Calcium Syrup', notes = 'Femur Fracture due to accident', tests = 'X-Ray', status = 'Completed')
db.session.add(appointment)

book_slot2 = available_slots[1]
book_slot2.slot_patient_id = patient3.patient_id
db.session.add(book_slot2)
appointment = Appointment(date_time = available_slots[1].date, doctor_id = doctor.doctor_id, patient_id = patient3.patient_id)
appointment.t = Treatment(diagnosis = 'Arm Fracture', prescription = 'Calcium Syrup', notes = 'Arm Fracture due to accident', tests = 'X-Ray', status = 'Completed')
db.session.add(appointment)

book_slot3 = available_slots[2]
book_slot3.slot_patient_id = patient2.patient_id
db.session.add(book_slot3)
appointment = Appointment(date_time = available_slots[2].date, doctor_id = doctor.doctor_id, patient_id = patient2.patient_id)
appointment.t = Treatment(diagnosis = 'Unexplained pain in wrist', prescription = '--', notes = 'Unexplained pain in wrist', tests = 'X-Ray', status = 'Completed')
db.session.add(appointment)

book_slot4 = available_slots[3]
book_slot4.slot_patient_id = patient1.patient_id
db.session.add(book_slot4)
appointment = Appointment(date_time = available_slots[3].date, doctor_id = doctor.doctor_id, patient_id = patient1.patient_id)
appointment.t = Treatment(diagnosis = 'Follow Up after emergency surgery', prescription = 'Calcium Syrup', notes = 'Leg fracture due to accident', tests = 'X-Ray', status = 'Completed')
db.session.add(appointment)


# Slots and past appointment bookings for doctor 6

doctor = db.get_or_404(Doctor, 6)

slot_for_doctor1 = SlotSchedules(date = date(2025,10,6), slot_doctor_id = doctor.doctor_id, schedule_slot_id = slot3.slot_id)
slot_for_doctor2 = SlotSchedules(date = date(2025,10,3), slot_doctor_id = doctor.doctor_id, schedule_slot_id = slot1.slot_id)
slot_for_doctor3 = SlotSchedules(date = date(2025,10,2), slot_doctor_id = doctor.doctor_id, schedule_slot_id = slot2.slot_id)
slot_for_doctor4 = SlotSchedules(date = date(2025,10,4), slot_doctor_id = doctor.doctor_id, schedule_slot_id = slot1.slot_id)
db.session.add(slot_for_doctor1)
db.session.add(slot_for_doctor2)
db.session.add(slot_for_doctor3)
db.session.add(slot_for_doctor4)

available_slots = SlotSchedules.query.filter(SlotSchedules.slot_doctor_id == doctor.doctor_id).all()

book_slot2 = available_slots[0]
book_slot2.slot_patient_id = patient2.patient_id
db.session.add(book_slot2)
appointment = Appointment(date_time = available_slots[1].date, doctor_id = doctor.doctor_id, patient_id = patient2.patient_id)
appointment.t = Treatment(diagnosis = 'Arm Fracture', prescription = 'Calcium Syrup', notes = 'Arm Fracture due to accident', tests = 'X-Ray', status = 'Completed')
db.session.add(appointment)

book_slot3 = available_slots[1]
book_slot3.slot_patient_id = patient4.patient_id
db.session.add(book_slot3)
appointment = Appointment(date_time = available_slots[2].date, doctor_id = doctor.doctor_id, patient_id = patient4.patient_id)
appointment.t = Treatment(diagnosis = 'Unexplained pain in wrist', prescription = '--', notes = 'Unexplained pain in wrist', tests = 'X-Ray', status = 'Completed')
db.session.add(appointment)

book_slot4 = available_slots[2]
book_slot4.slot_patient_id = patient1.patient_id
db.session.add(book_slot4)
appointment = Appointment(date_time = available_slots[3].date, doctor_id = doctor.doctor_id, patient_id = patient1.patient_id)
appointment.t = Treatment(diagnosis = 'Follow Up after emergency surgery', prescription = 'Calcium Syrup', notes = 'Leg fracture due to accident', tests = 'X-Ray', status = 'Completed')
db.session.add(appointment)

db.session.commit()

# Future Slots 