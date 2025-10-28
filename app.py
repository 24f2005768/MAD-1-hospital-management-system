from flask import Flask
from application.database import db
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project_database.sqlite3'
image_folder = os.path.join('static', 'images')
app.config['UPLOAD_FOLDER'] = image_folder

app.app_context().push()
db.init_app(app)

from application.models import *
from application.controllers import * 


if __name__ == '__main__':
    app.run(debug = True)