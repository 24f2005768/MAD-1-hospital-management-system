# MAD-1-project
A Flask app for hospitals, doctors and patients to easily manage appointments and treatments.

Issues:
1. Change in model: doctor - appointments relationship, removed `uselist = False` because (doctor-appointment) is not one-to-one. A doctor can have many appointments, hence it is a one-to-many relationship.

2. Change in model: doctor - added doctor_gender to show default picture of a doctor according to their gender; SlotSchedules - added status to set the status of an appointment as cancelled if doctor removes availability for an upcoming day. Earlier there was no way to cancel an upcoming appointment.

3. Change in model: SlotSchedules - There was no relationship linking Appointment and SlotSchedules or Treatment and SlotSchedules which created a difficulty in retriving and updating the correct treatment details. After adding one-to-one relationship between Appointment and SlotSchedules, retriving and feeding data is much more convinient.

4. Addition of New Tables: There was no way to be notified if a doctor or a patient cancelled an appointment, or a patient or a doctor was blacklisted, or request the admin about update of attributes which are not in control in patients or doctors. So, after adding 4 new tables (AvailibilityNotifications, PatientDoctorNotifications, AdminPatientNotifications, AdminDoctorNotifications), it is possible to recieve and send messages. A new table (ProfilePictures) was also added to store the information about the display pictures throughout the website.

5. Change in Model: SlotSchedules and Treatment had one overlapping column (status). A database should remain atomic and the same column in two different columns might create some problem in update, or might result in conflicting data. So, only the table Treatments have status now to maintain atomicity.