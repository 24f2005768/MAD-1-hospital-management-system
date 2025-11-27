from app import *
from sqlalchemy import and_, or_, desc
from datetime import date
from dateutil.relativedelta import relativedelta
from flask import url_for
import re 
from pyisemail import is_email

date_today = date.today()
list_of_next_7_dates = [(date_today + timedelta(days = i)) for i in range(8)]

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


doctors = Patient.query.filter(Patient.status == None).all()
print(doctors)