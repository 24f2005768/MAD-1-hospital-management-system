from app import *

# if database file is deleted, create instance by using this file and create admin
db.create_all()

# bcrypt.hashpw(user_password.encode('utf-8'), bcrypt.gensalt())
user = User(user_name = 'Admin', user_password = bcrypt.hashpw('12345'.encode('utf-8'), bcrypt.gensalt()), user_role = 'Admin')
user.admin_relationship = Admin(admin_name = 'Kriti', admin_password = '12345')
db.session.add(user)
db.session.commit()