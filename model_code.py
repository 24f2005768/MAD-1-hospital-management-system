from app import *

# # if database file is deleted, run this file to populate db

# , patient_height = , patient_weight = , patient_blood_pressure = , patient_blood_sugar_level =
# patients 

user1 = User(user_name = 'Shr_arya', user_password = '921369', user_role = 'Patient')
user1.patient_relationship = Patient(patient_name = 'Arya Sharma', contact_info = '1783731407', patient_email = 'a@email.com', patient_age = 18, patient_gender = 'Male' , patient_height = 186, patient_weight = 65, patient_dob = date(2007, 10, 3))
user1.patient_relationship.patient_pfp = ProfilePictures(name = 'male_patient', role = 'Patient')

user2 = User(user_name = 'Little_deer', user_password = 'kriti', user_role = 'Patient')
user2.patient_relationship = Patient(patient_name = 'Kriti Tiwari', contact_info = '4191156744', patient_email = 'k@email.com', patient_age = 21, patient_gender = 'Female', patient_height = 168, patient_weight = 60, patient_dob = date(2004, 9, 18))
user2.patient_relationship.patient_pfp = ProfilePictures(name = 'female_patient', role = 'Patient')

user3 = User(user_name = 'Mummy', user_password = 'mommy', user_role = 'Patient')
user3.patient_relationship = Patient(patient_name = 'Saroj Mishra', contact_info = '5865194463', patient_email = 's@email.com', patient_age = 47, patient_gender = 'Female', patient_height = 162, patient_weight = 75, patient_dob = date(1976, 6, 22))
user3.patient_relationship.patient_pfp = ProfilePictures(name = 'female_patient', role = 'Patient')

user4 = User(user_name = 'Aadi', user_password = 'aaditya', user_role = 'Patient')
user4.patient_relationship = Patient(patient_name = 'Aadi Trivedi', contact_info = '8030974434', patient_email = 'a@email.com', patient_age = 20, patient_gender = 'Male', patient_height = 183, patient_weight = 64, patient_dob = date(2005, 10, 4))
user4.patient_relationship.patient_pfp = ProfilePictures(name = 'male_patient', role = 'Patient')

user5 = User(user_name = 'Shruti', user_password = 'shruti', user_role = 'Patient')
user5.patient_relationship = Patient(patient_name = 'Shruti Hasan', contact_info = '2155059723', patient_email = 'sh@email.com', patient_age = 24, patient_gender = 'Female', patient_height = 170, patient_weight = 65, patient_dob = date(2001, 8, 10))
user5.patient_relationship.patient_pfp = ProfilePictures(name = 'female_patient', role = 'Patient')

user6 = User(user_name = 'Dheeraj', user_password = 'dheeraj', user_role = 'Patient')
user6.patient_relationship = Patient(patient_name = 'Dheeraj Chauhan', contact_info = '5207633762', patient_email = 'dc@gmail.com', patient_age = 41, patient_gender = 'Male', patient_height = 155, patient_weight = 52, patient_dob = date(1984, 3, 11)) 
user6.patient_relationship.patient_pfp = ProfilePictures(name = 'male_patient', role = 'Patient')

user7 = User(user_name = 'Jason', user_password = 'jason', user_role = 'Patient')
user7.patient_relationship = Patient(patient_name = 'Jason Perry', contact_info = '4240629978', patient_email = 'jp@gmail.com', patient_age = 32, patient_gender = 'Male', patient_height = 166, patient_weight = 68, patient_dob = date(2013, 4, 13)) 
user7.patient_relationship.patient_pfp = ProfilePictures(name = 'male_patient', role = 'Patient')

user8 = User(user_name = 'Tom', user_password = 'tommy', user_role = 'Patient')
user8.patient_relationship = Patient(patient_name = 'Tom Hilfiger', contact_info = '9355035218', patient_email = 'th@gmail.com', patient_age = 22, patient_gender = 'Male', patient_height = 175, patient_weight = 98, patient_dob = date(2003, 5, 4)) 
user8.patient_relationship.patient_pfp = ProfilePictures(name = 'male_patient', role = 'Patient')

user9 = User(user_name = 'Viena', user_password = 'vienaa', user_role = 'Patient')
user9.patient_relationship = Patient(patient_name = 'Viena Skye', contact_info = '9576063488', patient_email = 'vs@gmail.com', patient_age = 31, patient_gender = 'Female', patient_height = 140, patient_weight = 70, patient_dob = date(1994, 10, 7)) 
user9.patient_relationship.patient_pfp = ProfilePictures(name = 'female_patient', role = 'Patient')

# for pediatrics

user10 = User(user_name = 'Kashish', user_password = 'kashish', user_role = 'Patient')
user10.patient_relationship = Patient(patient_name = 'Kashish Mathur', contact_info = '1149508564', patient_email = 'km@gmail.com', patient_age = 11, patient_gender = 'Female', patient_height = 149, patient_weight = 82, patient_dob = date(2014, 11, 6)) 
user10.patient_relationship.patient_pfp = ProfilePictures(name = 'girl', role = 'Patient')

user11 = User(user_name = 'Rudraksh', user_password = 'rudraksh', user_role = 'Patient')
user11.patient_relationship = Patient(patient_name = 'Rudraksh Patel', contact_info = '3127523027', patient_email = 'rp@gmail.com', patient_age = 1, patient_gender = 'Male', patient_height = 56, patient_weight = 4.5, patient_dob = date(2024, 9, 4)) 
user11.patient_relationship.patient_pfp = ProfilePictures(name = 'boy', role = 'Patient')

user12 = User(user_name = 'Vipul', user_password = 'vipul', user_role = 'Patient')
user12.patient_relationship = Patient(patient_name = 'Vipul Raj', contact_info = '1024037587', patient_email = 'vr@gmail.com', patient_age = 15, patient_gender = 'Male', patient_height = 130, patient_weight = 48, patient_dob = date(2010, 1, 4)) 
user12.patient_relationship.patient_pfp = ProfilePictures(name = 'boy', role = 'Patient')

user13 = User(user_name = 'Anamika', user_password = 'anamika', user_role = 'Patient')
user13.patient_relationship = Patient(patient_name = 'Anamika Sen', contact_info = '9040428872', patient_email = 'as@gmail.com', patient_age = 7, patient_gender = 'Female', patient_height = 100, patient_weight = 25, patient_dob = date(2018, 7, 30)) 
user13.patient_relationship.patient_pfp = ProfilePictures(name = 'girl', role = 'Patient')

db.session.add(user1)
db.session.add(user2)
db.session.add(user3)
db.session.add(user4)
db.session.add(user5)
db.session.add(user6)
db.session.add(user7)
db.session.add(user8)
db.session.add(user9)
db.session.add(user10)
db.session.add(user11)
db.session.add(user12)
db.session.add(user13)

user1 = db.get_or_404(User, 2)
welcome_notification = AdminPatientNotifications(admin_patient_message_type = 'Welcome Message', admin_patient_message_content = f'Hello, { user1.patient_relationship.patient_name }! Thank you for choosing LDH Hospital.', message_patient_id = user1.patient_relationship.patient_id)
db.session.add(welcome_notification)

user2 = db.get_or_404(User, 3)
welcome_notification = AdminPatientNotifications(admin_patient_message_type = 'Welcome Message', admin_patient_message_content = f'Hello, { user2.patient_relationship.patient_name }! Thank you for choosing LDH Hospital.', message_patient_id = user2.patient_relationship.patient_id)
db.session.add(welcome_notification)

user3 = db.get_or_404(User, 4)
welcome_notification = AdminPatientNotifications(admin_patient_message_type = 'Welcome Message', admin_patient_message_content = f'Hello, { user3.patient_relationship.patient_name }! Thank you for choosing LDH Hospital.', message_patient_id = user3.patient_relationship.patient_id)
db.session.add(welcome_notification)

user4 = db.get_or_404(User, 5)
welcome_notification = AdminPatientNotifications(admin_patient_message_type = 'Welcome Message', admin_patient_message_content = f'Hello, { user4.patient_relationship.patient_name }! Thank you for choosing LDH Hospital.', message_patient_id = user4.patient_relationship.patient_id)
db.session.add(welcome_notification)

user5 = db.get_or_404(User, 6)
welcome_notification = AdminPatientNotifications(admin_patient_message_type = 'Welcome Message', admin_patient_message_content = f'Hello, { user5.patient_relationship.patient_name }! Thank you for choosing LDH Hospital.', message_patient_id = user5.patient_relationship.patient_id)
db.session.add(welcome_notification)

user6 = db.get_or_404(User, 7)
welcome_notification = AdminPatientNotifications(admin_patient_message_type = 'Welcome Message', admin_patient_message_content = f'Hello, { user6.patient_relationship.patient_name }! Thank you for choosing LDH Hospital.', message_patient_id = user6.patient_relationship.patient_id)
db.session.add(welcome_notification)

user7 = db.get_or_404(User, 8)
welcome_notification = AdminPatientNotifications(admin_patient_message_type = 'Welcome Message', admin_patient_message_content = f'Hello, { user7.patient_relationship.patient_name }! Thank you for choosing LDH Hospital.', message_patient_id = user7.patient_relationship.patient_id)
db.session.add(welcome_notification)

user8 = db.get_or_404(User, 9)
welcome_notification = AdminPatientNotifications(admin_patient_message_type = 'Welcome Message', admin_patient_message_content = f'Hello, { user8.patient_relationship.patient_name }! Thank you for choosing LDH Hospital.', message_patient_id = user8.patient_relationship.patient_id)
db.session.add(welcome_notification)

user9 = db.get_or_404(User, 10)
welcome_notification = AdminPatientNotifications(admin_patient_message_type = 'Welcome Message', admin_patient_message_content = f'Hello, { user9.patient_relationship.patient_name }! Thank you for choosing LDH Hospital.', message_patient_id = user9.patient_relationship.patient_id)
db.session.add(welcome_notification)

user10 = db.get_or_404(User, 11)
welcome_notification = AdminPatientNotifications(admin_patient_message_type = 'Welcome Message', admin_patient_message_content = f'Hello, { user10.patient_relationship.patient_name }! Thank you for choosing LDH Hospital.', message_patient_id = user10.patient_relationship.patient_id)
db.session.add(welcome_notification)

user11 = db.get_or_404(User, 12)
welcome_notification = AdminPatientNotifications(admin_patient_message_type = 'Welcome Message', admin_patient_message_content = f'Hello, { user11.patient_relationship.patient_name }! Thank you for choosing LDH Hospital.', message_patient_id = user11.patient_relationship.patient_id)
db.session.add(welcome_notification)

user12 = db.get_or_404(User, 13)
welcome_notification = AdminPatientNotifications(admin_patient_message_type = 'Welcome Message', admin_patient_message_content = f'Hello, { user12.patient_relationship.patient_name }! Thank you for choosing LDH Hospital.', message_patient_id = user12.patient_relationship.patient_id)
db.session.add(welcome_notification)

user13 = db.get_or_404(User, 14)
welcome_notification = AdminPatientNotifications(admin_patient_message_type = 'Welcome Message', admin_patient_message_content = f'Hello, { user13.patient_relationship.patient_name }! Thank you for choosing LDH Hospital.', message_patient_id = user13.patient_relationship.patient_id)
db.session.add(welcome_notification)

# # doctors and departments 

dept1 = Department(department_name = 'Cardiology', department_description = 'LDH offers a comprehensive cardiology program dedicated to the prevention, diagnosis, and treatment of a full spectrum of heart-related conditions. We provide a complete breadth of both invasive and noninvasive cardiovascular services, supported by ongoing research initiatives. Our highly skilled clinicians specialize in managing complex cases, delivering individualized treatment plans tailored to each patient"s unique needs. This patient-centered approach ensures that every individual receives the most advanced and appropriate care for their specific cardiovascular health journey.')
dept1.department_pfp = ProfilePictures(name = 'Cardiology', role = 'Department')
db.session.add(dept1)

user1 = User(user_name = 'Ganesh_heart', user_password = 'ganesh', user_role = 'Doctor')
user1.doctor_relationship = Doctor(doctor_name = 'Ganesh Rathi', doctor_contact_number = '5746160792', doctor_gender = 'Male', doctor_dob = date(1978, 3, 12),
                                   doctor_email = 'g@email.com', department_id = 1, doctor_desc = "Dr. Ganesh is a board-certified cardiologist with over 25 years of experience specializing in interventional cardiology. He is highly skilled in performing complex coronary interventions and has a special clinical interest in preventive cardiology and heart disease management in women. Dr. Ganesh is dedicated to providing compassionate, patient-centered care, developing personalized treatment plans to help his patients achieve their best possible heart health.")
user1.doctor_relationship.doctor_pfp = ProfilePictures(name = 'MaleDoctor', role = 'Doctor')

user2 = User(user_name = 'Vignesh_heart', user_password = 'vignesh', user_role = 'Doctor')
user2.doctor_relationship = Doctor(doctor_name = 'Vignesh Kumar', doctor_contact_number = '8166956143', doctor_gender = 'Male', doctor_dob = date(1966, 2, 14),
                                   doctor_email = 'v@email.com', department_id = 1, doctor_desc = "Dr. Vignesh is a board-certified cardiologist with over 7 years of experience specializing in interventional cardiology. He is highly skilled in performing complex coronary interventions and has a special clinical interest in preventive cardiology and heart disease management in women. Dr. Vignesh is dedicated to providing compassionate, patient-centered care, developing personalized treatment plans to help his patients achieve their best possible heart health.")
user2.doctor_relationship.doctor_pfp = ProfilePictures(name = 'MaleDoctor', role = 'Doctor')


dept2 = Department(department_name = 'Pediatrics', department_description = "LDH offers a comprehensive pediatrics program and dedicated pediatricians, all of whom are board-certified and have pursued advanced training in specialized fields such as cardiology and dermatology. This unique combination of general pediatrics and specialized knowledge allows our team to work collaboratively, offering comprehensive care for your child. Together, our pediatricians and pediatric specialists are equipped to accurately diagnose, effectively treat, and proactively help prevent a wide spectrum of childhood conditions, illnesses, and injuries, ensuring the highest standard of health from infancy through adolescence.")
dept2.department_pfp = ProfilePictures(name = 'Pediatrics', role = 'Department')
db.session.add(dept2)

user3 = User(user_name = 'Preeti_pediatrics', user_password = 'preeti', user_role = 'Doctor')
user3.doctor_relationship = Doctor(doctor_name = 'Preeti Rai', doctor_contact_number = '9370595052', doctor_gender = 'Female', doctor_dob = date(1988, 3, 17),
                                   doctor_email = 'p@email.com', department_id = 2, doctor_desc = "Dr. Preeti is a board-certified pediatrician with over 19 years of experience dedicated to the health and well-being of children, from newborns to young adults. Known for her warm and compassionate approach, she specializes in preventive care, childhood immunizations, and the management of common childhood illnesses like asthma and allergies. Dr. Preeti believes in building strong, trusting relationships with both her young patients and their families to foster a lifetime of good health.")
user3.doctor_relationship.doctor_pfp = ProfilePictures(name = 'FemaleDoctor1', role = 'Doctor')

user4 = User(user_name = 'Raju_pediatrics', user_password = 'raju', user_role = 'Doctor')
user4.doctor_relationship = Doctor(doctor_name = 'Raju Desai', doctor_contact_number = '7996673737', doctor_gender = 'Male', doctor_dob = date(1973, 5, 8),
                                   doctor_email = 'r@email.com', department_id = 2, doctor_desc = "Dr. Raju is a board-certified pediatrician with over 10 years of experience dedicated to the health and well-being of children, from newborns to young adults. Known for his warm and compassionate approach, he specializes in preventive care, childhood immunizations, and the management of common childhood illnesses like asthma and allergies. Dr. Raju believes in building strong, trusting relationships with both his young patients and their families to foster a lifetime of good health.")
user4.doctor_relationship.doctor_pfp = ProfilePictures(name = 'MaleDoctor', role = 'Doctor')


dept3 = Department(department_name = 'General Surgery', department_description = "LDH's General Surgery department is comprised of highly experienced senior surgeons and a specialized clinical team dedicated to achieving optimal patient outcomes. We utilize a modern approach, employing advanced surgical techniques and technology to ensure precision and promote excellent surgical results. Our expertise encompasses the comprehensive care of a wide range of acute and complex conditions, including diseases of the oesophagus, stomach, colon, liver, gallbladder, bile ducts, abdomen, and thyroid gland, as well as the repair of hernias. You can trust our skilled team to provide compassionate and effective surgical solutions.")
dept3.department_pfp = ProfilePictures(name = 'General Surgery', role = 'Department')
db.session.add(dept3)

user5 = User(user_name = 'Dev_surgery', user_password = 'dev', user_role = 'Doctor')
user5.doctor_relationship = Doctor(doctor_name = 'Dev Sharma', doctor_contact_number = '1059832795', doctor_gender = 'Male', doctor_dob = date(1998, 4, 10),
                                   doctor_email = 'd@email.com', department_id = 3, doctor_desc = "Dr. Dev is a board-certified General Surgeon with over 15 years of experience performing a wide range of abdominal procedures. His clinical expertise includes minimally invasive surgery for conditions of the gallbladder, colon, and hernias, with a dedicated focus on patient safety and achieving optimal recovery outcomes. Dr. Dev is committed to providing clear communication and compassionate care, ensuring his patients feel confident and well-informed at every step of their surgical journey.")
user5.doctor_relationship.doctor_pfp = ProfilePictures(name = 'MaleDoctor', role = 'Doctor')

user6 = User(user_name = 'Vikas_surgery', user_password = 'vikas', user_role = 'Doctor')
user6.doctor_relationship = Doctor(doctor_name = 'Vikas Jindal', doctor_contact_number = '2073880656', doctor_gender = 'Male', doctor_dob = date(1980, 6, 12),
                                   doctor_email = 'vk@email.com', department_id = 3, doctor_desc = "Dr. Vikas is a board-certified General Surgeon with over 13 years of experience performing a wide range of abdominal procedures. His clinical expertise includes minimally invasive surgery for conditions of the gallbladder, colon, and hernias, with a dedicated focus on patient safety and achieving optimal recovery outcomes. Dr. Vikas is committed to providing clear communication and compassionate care, ensuring his patients feel confident and well-informed at every step of their surgical journey.")
user6.doctor_relationship.doctor_pfp = ProfilePictures(name = 'MaleDoctor', role = 'Doctor')

dept4 = Department(department_name = 'Gastrology', department_description = "LDH's Gastrology department is dedicated to providing high-quality, comprehensive care for a wide spectrum of gastrointestinal conditions, including colon cancer, acid reflux, and other complex digestive disorders. We offer a full range of advanced diagnostic and therapeutic procedures to accurately identify and effectively manage issues affecting your digestive health. Our expertise also extends to personalized nutritional guidance, ensuring a holistic approach to your well-being. You can trust our specialized team to deliver exceptional, patient-centered care for all your digestive health needs.")
dept4.department_pfp = ProfilePictures(name = 'Gastrology', role = 'Department')
db.session.add(dept4)

dept5 = Department(department_name = 'Dietetics', department_description = '')
dept5.department_pfp = ProfilePictures(name = 'Dietetics', role = 'Department')
db.session.add(dept5)

user7 = User(user_name = 'Tanuja_dietetics', user_password = 'tanuja', user_role = 'Doctor')
user7.doctor_relationship = Doctor(doctor_name = 'Tanuja Rathore', doctor_contact_number = '8336977903', doctor_gender = 'Female', doctor_dob = date(1988, 3, 17),
                                   doctor_email = 't@email.com', department_id = 5, doctor_desc = "")
user7.doctor_relationship.doctor_pfp = ProfilePictures(name = 'FemaleDoctor1', role = 'Doctor')

db.session.add(user1)
db.session.add(user2)
db.session.add(user3)
db.session.add(user4)
db.session.add(user5)
db.session.add(user6)
db.session.add(user7)
db.session.commit()

doctors = Doctor.query.all()
for d in doctors:
    message = AdminDoctorNotifications(admin_doctor_message_type = 'Welcome message', admin_doctor_message_content = f'Hello, Dr. { d.doctor_name }! Greetings from the LDH Family.', role = 'Admin', message_doctor_id = d.doctor_id)
    db.session.add(message)

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
patient2 = db.get_or_404(Patient, 2)
patient3 = db.get_or_404(Patient, 3)
patient4 = db.get_or_404(Patient, 4)
patient5 = db.get_or_404(Patient, 5)
patient6 = db.get_or_404(Patient, 6)
patient7 = db.get_or_404(Patient, 7)
patient8 = db.get_or_404(Patient, 8)
patient9 = db.get_or_404(Patient, 9)
patient10 = db.get_or_404(Patient, 10)
patient11 = db.get_or_404(Patient, 11)
patient12 = db.get_or_404(Patient, 12)
patient13 = db.get_or_404(Patient, 13)

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
book_slot1.slot_sch_appointment_rel = Appointment(date_time = available_slots[0].date, doctor_id = doctor.doctor_id, patient_id = patient4.patient_id)
book_slot1.slot_sch_appointment_rel.t = Treatment(diagnosis = 'Chest Pain', prescription = 'Tablets', notes = 'Patient is experiencing chest pain since 5 days', tests = '--', status = 'Completed')
book_slot1.slot_sch_appointment_rel.t.treatment_dn = DieticianNotes(status = 'Completed', patient_id = patient4.patient_id, doctor_instructions = 'restricted-normal', morning_plan = 'Non-oily food', afternoon_plan = 'Non-oily food', evening_plan = 'Non-oily food')
db.session.add(book_slot1)
message = PatientDoctorNotifications(message_content = f"Hi, now you can check your treatment details for today's appointment with { doctor.doctor_name }.", message_type = 'Treatment Details', role = 'Doctor', m_doctor_id = f'{ doctor.doctor_id }', m_patient_id = book_slot1.slot_patient_id)
db.session.add(message)

book_slot2 = available_slots[1]
book_slot2.slot_patient_id = patient5.patient_id
book_slot2.slot_sch_appointment_rel = Appointment(date_time = available_slots[1].date, doctor_id = doctor.doctor_id, patient_id = patient5.patient_id)
book_slot2.slot_sch_appointment_rel.t = Treatment(diagnosis = 'Follow up', prescription = '--', notes = 'Follow up after surgery', tests = '--', status = 'Completed')
book_slot2.slot_sch_appointment_rel.t.treatment_dn = DieticianNotes(status = 'Completed', patient_id = patient5.patient_id, doctor_instructions = 'restricted-normal', morning_plan = 'Non-oily food', afternoon_plan = 'Non-oily food', evening_plan = 'Non-oily food')
db.session.add(book_slot2)
message = PatientDoctorNotifications(message_content = f"Hi, now you can check your treatment details for today's appointment with { doctor.doctor_name }.", message_type = 'Treatment Details', role = 'Doctor', m_doctor_id = f'{ doctor.doctor_id }', m_patient_id = book_slot2.slot_patient_id)
db.session.add(message)

book_slot3 = available_slots[2]
book_slot3.slot_patient_id = patient3.patient_id
book_slot3.slot_sch_appointment_rel = Appointment(date_time = available_slots[2].date, doctor_id = doctor.doctor_id, patient_id = patient3.patient_id)
book_slot3.slot_sch_appointment_rel.t = Treatment(diagnosis = 'Regular Checkup', prescription = 'Tablets', notes = 'Regular Checkup', tests = '--', status = 'Completed')
book_slot3.slot_sch_appointment_rel.t.treatment_dn = DieticianNotes(status = 'Completed', patient_id = patient3.patient_id, doctor_instructions = 'restricted-normal', morning_plan = 'Non-oily food', afternoon_plan = 'Non-oily food', evening_plan = 'Non-oily food')
db.session.add(book_slot3)
message = PatientDoctorNotifications(message_content = f"Hi, now you can check your treatment details for today's appointment with { doctor.doctor_name }.", message_type = 'Treatment Details', role = 'Doctor', m_doctor_id = f'{ doctor.doctor_id }', m_patient_id = book_slot3.slot_patient_id)
db.session.add(message)

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
book_slot1.slot_sch_appointment_rel = Appointment(date_time = available_slots[0].date, doctor_id = doctor.doctor_id, patient_id = patient2.patient_id)
book_slot1.slot_sch_appointment_rel.t = Treatment(diagnosis = 'Chest Pain', prescription = 'Tablets', notes = 'Patient is experiencing chest pain since 5 days', tests = '--', status = 'Completed')
book_slot1.slot_sch_appointment_rel.t.treatment_dn = DieticianNotes(status = 'Completed', patient_id = patient2.patient_id, doctor_instructions = 'restricted-normal', morning_plan = 'Non-oily food', afternoon_plan = 'Non-oily food', evening_plan = 'Non-oily food')
db.session.add(book_slot1)
message = PatientDoctorNotifications(message_content = f"Hi, now you can check your treatment details for today's appointment with { doctor.doctor_name }.", message_type = 'Treatment Details', role = 'Doctor', m_doctor_id = f'{ doctor.doctor_id }', m_patient_id = book_slot1.slot_patient_id)
db.session.add(message)

book_slot2 = available_slots[1]
book_slot2.slot_patient_id = patient1.patient_id
book_slot2.slot_sch_appointment_rel = Appointment(date_time = available_slots[1].date, doctor_id = doctor.doctor_id, patient_id = patient1.patient_id)
book_slot2.slot_sch_appointment_rel.t = Treatment(diagnosis = 'Follow up', prescription = '--', notes = 'Follow up after surgery', tests = '--', status = 'Completed')
book_slot2.slot_sch_appointment_rel.t.treatment_dn = DieticianNotes(status = 'Completed', patient_id = patient1.patient_id, doctor_instructions = 'restricted-normal', morning_plan = 'Non-oily food', afternoon_plan = 'Non-oily food', evening_plan = 'Non-oily food')
db.session.add(book_slot2)
message = PatientDoctorNotifications(message_content = f"Hi, now you can check your treatment details for today's appointment with { doctor.doctor_name }.", message_type = 'Treatment Details', role = 'Doctor', m_doctor_id = f'{ doctor.doctor_id }', m_patient_id = book_slot2.slot_patient_id)
db.session.add(message)

book_slot3 = available_slots[2]
book_slot3.slot_patient_id = patient4.patient_id
book_slot3.slot_sch_appointment_rel = Appointment(date_time = available_slots[2].date, doctor_id = doctor.doctor_id, patient_id = patient4.patient_id)
book_slot3.slot_sch_appointment_rel.t = Treatment(diagnosis = 'Regular Checkup', prescription = 'Tablets', notes = 'Regular Checkup', tests = '--', status = 'Completed')
book_slot3.slot_sch_appointment_rel.t.treatment_dn = DieticianNotes(status = 'Completed', patient_id = patient4.patient_id, doctor_instructions = 'restricted-normal', morning_plan = 'Non-oily food', afternoon_plan = 'Non-oily food', evening_plan = 'Non-oily food')
db.session.add(book_slot3)
message = PatientDoctorNotifications(message_content = f"Hi, now you can check your treatment details for today's appointment with { doctor.doctor_name }.", message_type = 'Treatment Details', role = 'Doctor', m_doctor_id = f'{ doctor.doctor_id }', m_patient_id = book_slot3.slot_patient_id)
db.session.add(message)

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
book_slot1.slot_patient_id = patient11.patient_id
book_slot1.slot_sch_appointment_rel = Appointment(date_time = available_slots[0].date, doctor_id = doctor.doctor_id, patient_id = patient12.patient_id)
book_slot1.slot_sch_appointment_rel.t = Treatment(diagnosis = 'Fever', prescription = 'Medicines', notes = 'Patient has fever since 3 days, no signicant pain', tests = '--', status = 'Completed')
db.session.add(book_slot1)
message = PatientDoctorNotifications(message_content = f"Hi, now you can check your treatment details for today's appointment with { doctor.doctor_name }.", message_type = 'Treatment Details', role = 'Doctor', m_doctor_id = f'{ doctor.doctor_id }', m_patient_id = book_slot1.slot_patient_id)
db.session.add(message)

book_slot2 = available_slots[1]
book_slot2.slot_patient_id = patient13.patient_id
book_slot2.slot_sch_appointment_rel = Appointment(date_time = available_slots[1].date, doctor_id = doctor.doctor_id, patient_id = patient13.patient_id)
book_slot2.slot_sch_appointment_rel.t = Treatment(diagnosis = 'Regular Checkup', prescription = '--', notes = 'Regular Checkup', tests = 'Blood Test', status = 'Completed')
db.session.add(book_slot2)
message = PatientDoctorNotifications(message_content = f"Hi, now you can check your treatment details for today's appointment with { doctor.doctor_name }.", message_type = 'Treatment Details', role = 'Doctor', m_doctor_id = f'{ doctor.doctor_id }', m_patient_id = book_slot2.slot_patient_id)
db.session.add(message)

book_slot3 = available_slots[2]
book_slot3.slot_patient_id = patient10.patient_id
book_slot3.slot_sch_appointment_rel = Appointment(date_time = available_slots[2].date, doctor_id = doctor.doctor_id, patient_id = patient10.patient_id)
book_slot3.slot_sch_appointment_rel.t = Treatment(diagnosis = 'Regular Checkup', prescription = 'Multi-vitamins', notes = 'Patient is recovering well', tests = '--', status = 'Completed')
db.session.add(book_slot3)
message = PatientDoctorNotifications(message_content = f"Hi, now you can check your treatment details for today's appointment with { doctor.doctor_name }.", message_type = 'Treatment Details', role = 'Doctor', m_doctor_id = f'{ doctor.doctor_id }', m_patient_id = book_slot3.slot_patient_id)
db.session.add(message)

book_slot4 = available_slots[3]
book_slot4.slot_patient_id = patient12.patient_id
book_slot4.slot_sch_appointment_rel = Appointment(date_time = available_slots[3].date, doctor_id = doctor.doctor_id, patient_id = patient12.patient_id)
book_slot4.slot_sch_appointment_rel.t = Treatment(diagnosis = 'Fever', prescription = 'Medicines and Injections', notes = 'Admitted for 3 days', tests = '--', status = 'Completed')
db.session.add(book_slot4)
message = PatientDoctorNotifications(message_content = f"Hi, now you can check your treatment details for today's appointment with { doctor.doctor_name }.", message_type = 'Treatment Details', role = 'Doctor', m_doctor_id = f'{ doctor.doctor_id }', m_patient_id = book_slot4.slot_patient_id)
db.session.add(message)


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
book_slot1.slot_patient_id = patient13.patient_id
book_slot1.slot_sch_appointment_rel = Appointment(date_time = available_slots[0].date, doctor_id = doctor.doctor_id, patient_id = patient13.patient_id)
book_slot1.slot_sch_appointment_rel.t = Treatment(diagnosis = 'Fever', prescription = 'Medicines', notes = 'Patient has fever since 3 days, no signicant pain', tests = '--', status = 'Completed')
db.session.add(book_slot1)
message = PatientDoctorNotifications(message_content = f"Hi, now you can check your treatment details for today's appointment with { doctor.doctor_name }.", message_type = 'Treatment Details', role = 'Doctor', m_doctor_id = f'{ doctor.doctor_id }', m_patient_id = book_slot1.slot_patient_id)
db.session.add(message)

book_slot2 = available_slots[1]
book_slot2.slot_patient_id = patient12.patient_id
book_slot2.slot_sch_appointment_rel = Appointment(date_time = available_slots[1].date, doctor_id = doctor.doctor_id, patient_id = patient12.patient_id)
book_slot2.slot_sch_appointment_rel.t = Treatment(diagnosis = 'Regular Checkup', prescription = '--', notes = 'Regular Checkup', tests = 'Blood Test', status = 'Completed')
db.session.add(book_slot2)
message = PatientDoctorNotifications(message_content = f"Hi, now you can check your treatment details for today's appointment with { doctor.doctor_name }.", message_type = 'Treatment Details', role = 'Doctor', m_doctor_id = f'{ doctor.doctor_id }', m_patient_id = book_slot2.slot_patient_id)
db.session.add(message)

book_slot3 = available_slots[2]
book_slot3.slot_patient_id = patient10.patient_id
book_slot3.slot_sch_appointment_rel = Appointment(date_time = available_slots[2].date, doctor_id = doctor.doctor_id, patient_id = patient10.patient_id)
book_slot3.slot_sch_appointment_rel.t = Treatment(diagnosis = 'Regular Checkup', prescription = 'Multi-vitamins', notes = 'Patient is recovering well', tests = '--', status = 'Completed')
db.session.add(book_slot3)
message = PatientDoctorNotifications(message_content = f"Hi, now you can check your treatment details for today's appointment with { doctor.doctor_name }.", message_type = 'Treatment Details', role = 'Doctor', m_doctor_id = f'{ doctor.doctor_id }', m_patient_id = book_slot3.slot_patient_id)
db.session.add(message)


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
book_slot1.slot_sch_appointment_rel = Appointment(date_time = available_slots[0].date, doctor_id = doctor.doctor_id, patient_id = patient5.patient_id)
book_slot1.slot_sch_appointment_rel.t = Treatment(diagnosis = 'Femur Fracture', prescription = 'Calcium Syrup', notes = 'Femur Fracture due to accident', tests = 'X-Ray', status = 'Completed')
db.session.add(book_slot1)
message = PatientDoctorNotifications(message_content = f"Hi, now you can check your treatment details for today's appointment with { doctor.doctor_name }.", message_type = 'Treatment Details', role = 'Doctor', m_doctor_id = f'{ doctor.doctor_id }', m_patient_id = book_slot1.slot_patient_id)
db.session.add(message)

book_slot2 = available_slots[1]
book_slot2.slot_patient_id = patient3.patient_id
book_slot2.slot_sch_appointment_rel = Appointment(date_time = available_slots[1].date, doctor_id = doctor.doctor_id, patient_id = patient3.patient_id)
book_slot2.slot_sch_appointment_rel.t = Treatment(diagnosis = 'Arm Fracture', prescription = 'Calcium Syrup', notes = 'Arm Fracture due to accident', tests = 'X-Ray', status = 'Completed')
db.session.add(book_slot2)
message = PatientDoctorNotifications(message_content = f"Hi, now you can check your treatment details for today's appointment with { doctor.doctor_name }.", message_type = 'Treatment Details', role = 'Doctor', m_doctor_id = f'{ doctor.doctor_id }', m_patient_id = book_slot2.slot_patient_id)
db.session.add(message)

book_slot3 = available_slots[2]
book_slot3.slot_patient_id = patient2.patient_id
book_slot3.slot_sch_appointment_rel = Appointment(date_time = available_slots[2].date, doctor_id = doctor.doctor_id, patient_id = patient2.patient_id)
book_slot3.slot_sch_appointment_rel.t = Treatment(diagnosis = 'Unexplained pain in wrist', prescription = '--', notes = 'Unexplained pain in wrist', tests = 'X-Ray', status = 'Completed')
db.session.add(book_slot3)
message = PatientDoctorNotifications(message_content = f"Hi, now you can check your treatment details for today's appointment with { doctor.doctor_name }.", message_type = 'Treatment Details', role = 'Doctor', m_doctor_id = f'{ doctor.doctor_id }', m_patient_id = book_slot3.slot_patient_id)
db.session.add(message)

book_slot4 = available_slots[3]
book_slot4.slot_patient_id = patient1.patient_id
book_slot4.slot_sch_appointment_rel = Appointment(date_time = available_slots[3].date, doctor_id = doctor.doctor_id, patient_id = patient1.patient_id)
book_slot4.slot_sch_appointment_rel.t = Treatment(diagnosis = 'Follow Up after emergency surgery', prescription = 'Calcium Syrup', notes = 'Leg fracture due to accident', tests = 'X-Ray', status = 'Completed')
db.session.add(book_slot4)
message = PatientDoctorNotifications(message_content = f"Hi, now you can check your treatment details for today's appointment with { doctor.doctor_name }.", message_type = 'Treatment Details', role = 'Doctor', m_doctor_id = f'{ doctor.doctor_id }', m_patient_id = book_slot4.slot_patient_id)
db.session.add(message)


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

book_slot1 = available_slots[0]
book_slot1.slot_patient_id = patient2.patient_id
book_slot1.slot_sch_appointment_rel = Appointment(date_time = available_slots[1].date, doctor_id = doctor.doctor_id, patient_id = patient2.patient_id)
book_slot1.slot_sch_appointment_rel.t = Treatment(diagnosis = 'Arm Fracture', prescription = 'Calcium Syrup', notes = 'Arm Fracture due to accident', tests = 'X-Ray', status = 'Completed')
db.session.add(book_slot1)
message = PatientDoctorNotifications(message_content = f"Hi, now you can check your treatment details for today's appointment with { doctor.doctor_name }.", message_type = 'Treatment Details', role = 'Doctor', m_doctor_id = f'{ doctor.doctor_id }', m_patient_id = book_slot1.slot_patient_id)
db.session.add(message)

book_slot2 = available_slots[1]
book_slot2.slot_patient_id = patient4.patient_id
book_slot2.slot_sch_appointment_rel = Appointment(date_time = available_slots[2].date, doctor_id = doctor.doctor_id, patient_id = patient4.patient_id)
book_slot2.slot_sch_appointment_rel.t = Treatment(diagnosis = 'Unexplained pain in wrist', prescription = '--', notes = 'Unexplained pain in wrist', tests = 'X-Ray', status = 'Completed')
db.session.add(book_slot2)
message = PatientDoctorNotifications(message_content = f"Hi, now you can check your treatment details for today's appointment with { doctor.doctor_name }.", message_type = 'Treatment Details', role = 'Doctor', m_doctor_id = f'{ doctor.doctor_id }', m_patient_id = book_slot2.slot_patient_id)
db.session.add(message)

book_slot3 = available_slots[2]
book_slot3.slot_patient_id = patient1.patient_id
book_slot3.slot_sch_appointment_rel = Appointment(date_time = available_slots[3].date, doctor_id = doctor.doctor_id, patient_id = patient1.patient_id)
book_slot3.slot_sch_appointment_rel.t = Treatment(diagnosis = 'Follow Up after emergency surgery', prescription = 'Calcium Syrup', notes = 'Leg fracture due to accident', tests = 'X-Ray', status = 'Completed')
db.session.add(book_slot3)
message = PatientDoctorNotifications(message_content = f"Hi, now you can check your treatment details for today's appointment with { doctor.doctor_name }.", message_type = 'Treatment Details', role = 'Doctor', m_doctor_id = f'{ doctor.doctor_id }', m_patient_id = book_slot3.slot_patient_id)
db.session.add(message)

# Future Slots 

list_of_next_7_dates = [(date_today + timedelta(days = i)) for i in range(8)]

# Doctor1
doctor = db.get_or_404(Doctor, 1)

slot_for_doctor0 = SlotSchedules(date = list_of_next_7_dates[0], slot_doctor_id = doctor.doctor_id, schedule_slot_id = slot3.slot_id, slot_patient_id = patient1.patient_id)
slot_for_doctor0.slot_sch_appointment_rel = Appointment(date_time = slot_for_doctor0.date, doctor_id = doctor.doctor_id, patient_id = patient1.patient_id)
slot_for_doctor0.slot_sch_appointment_rel.t = Treatment(status = 'Booked')

slot_for_doctor1 = SlotSchedules(date = list_of_next_7_dates[0], slot_doctor_id = doctor.doctor_id, schedule_slot_id = slot3.slot_id, slot_patient_id = patient7.patient_id)
slot_for_doctor1.slot_sch_appointment_rel = Appointment(date_time = slot_for_doctor1.date, doctor_id = doctor.doctor_id, patient_id = patient7.patient_id)
slot_for_doctor1.slot_sch_appointment_rel.t = Treatment(status = 'Booked')

slot_for_doctor2 = SlotSchedules(date = list_of_next_7_dates[0], slot_doctor_id = doctor.doctor_id, schedule_slot_id = slot3.slot_id, slot_patient_id = patient4.patient_id)
slot_for_doctor2.slot_sch_appointment_rel = Appointment(date_time = slot_for_doctor1.date, doctor_id = doctor.doctor_id, patient_id = patient4.patient_id)
slot_for_doctor2.slot_sch_appointment_rel.t = Treatment(status = 'Booked')

slot_for_doctor3 = SlotSchedules(date = list_of_next_7_dates[1], slot_doctor_id = doctor.doctor_id, schedule_slot_id = slot2.slot_id, slot_patient_id = patient2.patient_id)
slot_for_doctor3.slot_sch_appointment_rel = Appointment(date_time = slot_for_doctor2.date, doctor_id = doctor.doctor_id, patient_id = patient2.patient_id)
slot_for_doctor3.slot_sch_appointment_rel.t = Treatment(status = 'Booked')

slot_for_doctor4 = SlotSchedules(date = list_of_next_7_dates[4], slot_doctor_id = doctor.doctor_id, schedule_slot_id = slot1.slot_id, slot_patient_id = patient5.patient_id)
slot_for_doctor4.slot_sch_appointment_rel = Appointment(date_time = slot_for_doctor3.date, doctor_id = doctor.doctor_id, patient_id = patient5.patient_id)
slot_for_doctor4.slot_sch_appointment_rel.t = Treatment(status = 'Booked')

slot_for_doctor5 = SlotSchedules(date = list_of_next_7_dates[5], slot_doctor_id = doctor.doctor_id, schedule_slot_id = slot2.slot_id)

db.session.add(slot_for_doctor0)
db.session.add(slot_for_doctor1)
db.session.add(slot_for_doctor2)
db.session.add(slot_for_doctor3)
db.session.add(slot_for_doctor4)
db.session.add(slot_for_doctor5)

# Doctor2
doctor = db.get_or_404(Doctor, 2)

slot_for_doctor0 = SlotSchedules(date = list_of_next_7_dates[0], slot_doctor_id = doctor.doctor_id, schedule_slot_id = slot3.slot_id, slot_patient_id = patient2.patient_id)
slot_for_doctor0.slot_sch_appointment_rel = Appointment(date_time = slot_for_doctor0.date, doctor_id = doctor.doctor_id, patient_id = patient2.patient_id)
slot_for_doctor0.slot_sch_appointment_rel.t = Treatment(status = 'Booked')

slot_for_doctor1 = SlotSchedules(date = list_of_next_7_dates[0], slot_doctor_id = doctor.doctor_id, schedule_slot_id = slot3.slot_id, slot_patient_id = patient5.patient_id)
slot_for_doctor1.slot_sch_appointment_rel = Appointment(date_time = slot_for_doctor1.date, doctor_id = doctor.doctor_id, patient_id = patient5.patient_id)
slot_for_doctor1.slot_sch_appointment_rel.t = Treatment(status = 'Booked')

slot_for_doctor2 = SlotSchedules(date = list_of_next_7_dates[0], slot_doctor_id = doctor.doctor_id, schedule_slot_id = slot3.slot_id, slot_patient_id = patient6.patient_id)
slot_for_doctor2.slot_sch_appointment_rel = Appointment(date_time = slot_for_doctor1.date, doctor_id = doctor.doctor_id, patient_id = patient6.patient_id)
slot_for_doctor2.slot_sch_appointment_rel.t = Treatment(status = 'Booked')

slot_for_doctor3 = SlotSchedules(date = list_of_next_7_dates[1], slot_doctor_id = doctor.doctor_id, schedule_slot_id = slot2.slot_id, slot_patient_id = patient2.patient_id)
slot_for_doctor3.slot_sch_appointment_rel = Appointment(date_time = slot_for_doctor2.date, doctor_id = doctor.doctor_id, patient_id = patient2.patient_id)
slot_for_doctor3.slot_sch_appointment_rel.t = Treatment(status = 'Booked')

slot_for_doctor4 = SlotSchedules(date = list_of_next_7_dates[4], slot_doctor_id = doctor.doctor_id, schedule_slot_id = slot1.slot_id, slot_patient_id = patient3.patient_id)
slot_for_doctor4.slot_sch_appointment_rel = Appointment(date_time = slot_for_doctor3.date, doctor_id = doctor.doctor_id, patient_id = patient3.patient_id)
slot_for_doctor4.slot_sch_appointment_rel.t = Treatment(status = 'Booked')

slot_for_doctor5 = SlotSchedules(date = list_of_next_7_dates[5], slot_doctor_id = doctor.doctor_id, schedule_slot_id = slot2.slot_id)

db.session.add(slot_for_doctor0)
db.session.add(slot_for_doctor1)
db.session.add(slot_for_doctor2)
db.session.add(slot_for_doctor3)
db.session.add(slot_for_doctor4)
db.session.add(slot_for_doctor5)

# Doctor3
doctor = db.get_or_404(Doctor, 3)

slot_for_doctor0 = SlotSchedules(date = list_of_next_7_dates[0], slot_doctor_id = doctor.doctor_id, schedule_slot_id = slot3.slot_id, slot_patient_id = patient11.patient_id)
slot_for_doctor0.slot_sch_appointment_rel = Appointment(date_time = slot_for_doctor0.date, doctor_id = doctor.doctor_id, patient_id = patient11.patient_id)
slot_for_doctor0.slot_sch_appointment_rel.t = Treatment(status = 'Booked')

slot_for_doctor1 = SlotSchedules(date = list_of_next_7_dates[0], slot_doctor_id = doctor.doctor_id, schedule_slot_id = slot3.slot_id, slot_patient_id = patient10.patient_id)
slot_for_doctor1.slot_sch_appointment_rel = Appointment(date_time = slot_for_doctor1.date, doctor_id = doctor.doctor_id, patient_id = patient10.patient_id)
slot_for_doctor1.slot_sch_appointment_rel.t = Treatment(status = 'Booked')

slot_for_doctor2 = SlotSchedules(date = list_of_next_7_dates[0], slot_doctor_id = doctor.doctor_id, schedule_slot_id = slot3.slot_id, slot_patient_id = patient9.patient_id)
slot_for_doctor2.slot_sch_appointment_rel = Appointment(date_time = slot_for_doctor1.date, doctor_id = doctor.doctor_id, patient_id = patient9.patient_id)
slot_for_doctor2.slot_sch_appointment_rel.t = Treatment(status = 'Booked')

slot_for_doctor3 = SlotSchedules(date = list_of_next_7_dates[1], slot_doctor_id = doctor.doctor_id, schedule_slot_id = slot2.slot_id, slot_patient_id = patient12.patient_id)
slot_for_doctor3.slot_sch_appointment_rel = Appointment(date_time = slot_for_doctor2.date, doctor_id = doctor.doctor_id, patient_id = patient12.patient_id)
slot_for_doctor3.slot_sch_appointment_rel.t = Treatment(status = 'Booked')

slot_for_doctor4 = SlotSchedules(date = list_of_next_7_dates[4], slot_doctor_id = doctor.doctor_id, schedule_slot_id = slot1.slot_id, slot_patient_id = patient13.patient_id)
slot_for_doctor4.slot_sch_appointment_rel = Appointment(date_time = slot_for_doctor3.date, doctor_id = doctor.doctor_id, patient_id = patient13.patient_id)
slot_for_doctor4.slot_sch_appointment_rel.t = Treatment(status = 'Booked')

slot_for_doctor5 = SlotSchedules(date = list_of_next_7_dates[5], slot_doctor_id = doctor.doctor_id, schedule_slot_id = slot2.slot_id)

db.session.add(slot_for_doctor0)
db.session.add(slot_for_doctor1)
db.session.add(slot_for_doctor2)
db.session.add(slot_for_doctor3)
db.session.add(slot_for_doctor4)
db.session.add(slot_for_doctor5)

# Doctor4
doctor = db.get_or_404(Doctor, 4)

slot_for_doctor0 = SlotSchedules(date = list_of_next_7_dates[0], slot_doctor_id = doctor.doctor_id, schedule_slot_id = slot3.slot_id, slot_patient_id = patient11.patient_id)
slot_for_doctor0.slot_sch_appointment_rel = Appointment(date_time = slot_for_doctor0.date, doctor_id = doctor.doctor_id, patient_id = patient11.patient_id)
slot_for_doctor0.slot_sch_appointment_rel.t = Treatment(status = 'Booked')

slot_for_doctor1 = SlotSchedules(date = list_of_next_7_dates[0], slot_doctor_id = doctor.doctor_id, schedule_slot_id = slot3.slot_id, slot_patient_id = patient10.patient_id)
slot_for_doctor1.slot_sch_appointment_rel = Appointment(date_time = slot_for_doctor1.date, doctor_id = doctor.doctor_id, patient_id = patient10.patient_id)
slot_for_doctor1.slot_sch_appointment_rel.t = Treatment(status = 'Booked')

slot_for_doctor2 = SlotSchedules(date = list_of_next_7_dates[0], slot_doctor_id = doctor.doctor_id, schedule_slot_id = slot3.slot_id, slot_patient_id = patient9.patient_id)
slot_for_doctor2.slot_sch_appointment_rel = Appointment(date_time = slot_for_doctor1.date, doctor_id = doctor.doctor_id, patient_id = patient9.patient_id)
slot_for_doctor2.slot_sch_appointment_rel.t = Treatment(status = 'Booked')

slot_for_doctor3 = SlotSchedules(date = list_of_next_7_dates[1], slot_doctor_id = doctor.doctor_id, schedule_slot_id = slot2.slot_id, slot_patient_id = patient12.patient_id)
slot_for_doctor3.slot_sch_appointment_rel = Appointment(date_time = slot_for_doctor2.date, doctor_id = doctor.doctor_id, patient_id = patient12.patient_id)
slot_for_doctor3.slot_sch_appointment_rel.t = Treatment(status = 'Booked')

slot_for_doctor4 = SlotSchedules(date = list_of_next_7_dates[4], slot_doctor_id = doctor.doctor_id, schedule_slot_id = slot1.slot_id, slot_patient_id = patient13.patient_id)
slot_for_doctor4.slot_sch_appointment_rel = Appointment(date_time = slot_for_doctor3.date, doctor_id = doctor.doctor_id, patient_id = patient13.patient_id)
slot_for_doctor4.slot_sch_appointment_rel.t = Treatment(status = 'Booked')

slot_for_doctor5 = SlotSchedules(date = list_of_next_7_dates[5], slot_doctor_id = doctor.doctor_id, schedule_slot_id = slot2.slot_id)

db.session.add(slot_for_doctor0)
db.session.add(slot_for_doctor1)
db.session.add(slot_for_doctor2)
db.session.add(slot_for_doctor3)
db.session.add(slot_for_doctor4)
db.session.add(slot_for_doctor5)

# Doctor5
doctor = db.get_or_404(Doctor, 5)

slot_for_doctor0 = SlotSchedules(date = list_of_next_7_dates[0], slot_doctor_id = doctor.doctor_id, schedule_slot_id = slot3.slot_id, slot_patient_id = patient1.patient_id)
slot_for_doctor0.slot_sch_appointment_rel = Appointment(date_time = slot_for_doctor0.date, doctor_id = doctor.doctor_id, patient_id = patient1.patient_id)
slot_for_doctor0.slot_sch_appointment_rel.t = Treatment(status = 'Booked')

slot_for_doctor1 = SlotSchedules(date = list_of_next_7_dates[0], slot_doctor_id = doctor.doctor_id, schedule_slot_id = slot3.slot_id, slot_patient_id = patient5.patient_id)
slot_for_doctor1.slot_sch_appointment_rel = Appointment(date_time = slot_for_doctor1.date, doctor_id = doctor.doctor_id, patient_id = patient5.patient_id)
slot_for_doctor1.slot_sch_appointment_rel.t = Treatment(status = 'Booked')

slot_for_doctor2 = SlotSchedules(date = list_of_next_7_dates[0], slot_doctor_id = doctor.doctor_id, schedule_slot_id = slot3.slot_id, slot_patient_id = patient3.patient_id)
slot_for_doctor2.slot_sch_appointment_rel = Appointment(date_time = slot_for_doctor1.date, doctor_id = doctor.doctor_id, patient_id = patient3.patient_id)
slot_for_doctor2.slot_sch_appointment_rel.t = Treatment(status = 'Booked')

slot_for_doctor3 = SlotSchedules(date = list_of_next_7_dates[1], slot_doctor_id = doctor.doctor_id, schedule_slot_id = slot2.slot_id, slot_patient_id = patient2.patient_id)
slot_for_doctor3.slot_sch_appointment_rel = Appointment(date_time = slot_for_doctor2.date, doctor_id = doctor.doctor_id, patient_id = patient2.patient_id)
slot_for_doctor3.slot_sch_appointment_rel.t = Treatment(status = 'Booked')

slot_for_doctor4 = SlotSchedules(date = list_of_next_7_dates[4], slot_doctor_id = doctor.doctor_id, schedule_slot_id = slot1.slot_id, slot_patient_id = patient9.patient_id)
slot_for_doctor4.slot_sch_appointment_rel = Appointment(date_time = slot_for_doctor3.date, doctor_id = doctor.doctor_id, patient_id = patient9.patient_id)
slot_for_doctor4.slot_sch_appointment_rel.t = Treatment(status = 'Booked')

slot_for_doctor5 = SlotSchedules(date = list_of_next_7_dates[5], slot_doctor_id = doctor.doctor_id, schedule_slot_id = slot2.slot_id)

db.session.add(slot_for_doctor0)
db.session.add(slot_for_doctor1)
db.session.add(slot_for_doctor2)
db.session.add(slot_for_doctor3)
db.session.add(slot_for_doctor4)
db.session.add(slot_for_doctor5)

# Doctor6
doctor = db.get_or_404(Doctor, 6)

slot_for_doctor0 = SlotSchedules(date = list_of_next_7_dates[0], slot_doctor_id = doctor.doctor_id, schedule_slot_id = slot3.slot_id, slot_patient_id = patient5.patient_id)
slot_for_doctor0.slot_sch_appointment_rel = Appointment(date_time = slot_for_doctor0.date, doctor_id = doctor.doctor_id, patient_id = patient5.patient_id)
slot_for_doctor0.slot_sch_appointment_rel.t = Treatment(status = 'Booked')

slot_for_doctor1 = SlotSchedules(date = list_of_next_7_dates[0], slot_doctor_id = doctor.doctor_id, schedule_slot_id = slot3.slot_id, slot_patient_id = patient2.patient_id)
slot_for_doctor1.slot_sch_appointment_rel = Appointment(date_time = slot_for_doctor1.date, doctor_id = doctor.doctor_id, patient_id = patient2.patient_id)
slot_for_doctor1.slot_sch_appointment_rel.t = Treatment(status = 'Booked')

slot_for_doctor2 = SlotSchedules(date = list_of_next_7_dates[0], slot_doctor_id = doctor.doctor_id, schedule_slot_id = slot3.slot_id, slot_patient_id = patient7.patient_id)
slot_for_doctor2.slot_sch_appointment_rel = Appointment(date_time = slot_for_doctor1.date, doctor_id = doctor.doctor_id, patient_id = patient7.patient_id)
slot_for_doctor2.slot_sch_appointment_rel.t = Treatment(status = 'Booked')

slot_for_doctor3 = SlotSchedules(date = list_of_next_7_dates[1], slot_doctor_id = doctor.doctor_id, schedule_slot_id = slot2.slot_id, slot_patient_id = patient8.patient_id)
slot_for_doctor3.slot_sch_appointment_rel = Appointment(date_time = slot_for_doctor2.date, doctor_id = doctor.doctor_id, patient_id = patient8.patient_id)
slot_for_doctor3.slot_sch_appointment_rel.t = Treatment(status = 'Booked')

slot_for_doctor4 = SlotSchedules(date = list_of_next_7_dates[4], slot_doctor_id = doctor.doctor_id, schedule_slot_id = slot1.slot_id, slot_patient_id = patient6.patient_id)
slot_for_doctor4.slot_sch_appointment_rel = Appointment(date_time = slot_for_doctor3.date, doctor_id = doctor.doctor_id, patient_id = patient6.patient_id)
slot_for_doctor4.slot_sch_appointment_rel.t = Treatment(status = 'Booked')

slot_for_doctor5 = SlotSchedules(date = list_of_next_7_dates[5], slot_doctor_id = doctor.doctor_id, schedule_slot_id = slot2.slot_id)

db.session.add(slot_for_doctor0)
db.session.add(slot_for_doctor1)
db.session.add(slot_for_doctor2)
db.session.add(slot_for_doctor3)
db.session.add(slot_for_doctor4)
db.session.add(slot_for_doctor5)

db.session.commit()