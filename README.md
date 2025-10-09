# MAD-1-project
A Flask app for hospitals, doctors and patients to easily manage appointments and treatments.

Issues:
1. Change in model: doctor - appointments relationship, removed `uselist = False` because (doctor-appointment) is not one-to-one. A doctor can have many appointments, hence it is a oe-to-many relationship.