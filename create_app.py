from app import *

# if database file is deleted, create instance by using this file and create admin
db.create_all()

user = User(user_name = 'Admin', user_password = '12345', user_role = 'Admin')
user.admin_relationship = Admin(admin_name = 'Kriti', admin_password = '12345')
db.session.add(user)
db.session.commit()