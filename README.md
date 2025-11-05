# MAD-1-project
A Flask app for hospitals, doctors and patients to easily manage appointments and treatments.

Issues:
1. Change in model: doctor - appointments relationship, removed `uselist = False` because (doctor-appointment) is not one-to-one. A doctor can have many appointments, hence it is a one-to-many relationship.

2. Change in model: doctor - added doctor_gender to show default picture of a doctor according to their gender; SlotSchedules - added status to set the status of an appointment as cancelled if doctor removes availability for an upcoming day. Earlier there was no way to cancel an upcoming appointment.

3. Change in model: SlotSchedules - There was no relationship linking Appointment and SlotSchedules or Treatment and SlotSchedules which created a difficulty in retriving and updating the correct treatment details. After adding one-to-one relationship between Appointment and SlotSchedules, retriving and feeding data is much more convinient.