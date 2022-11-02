import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

basedir = os.path.abspath(os.path.dirname(__file__))
db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
        app = Flask(__name__)
        app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///' + os.path.join(basedir, DB_NAME)
        print(app.config['SQLALCHEMY_DATABASE_URI'])
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

        db.init_app(app)

        from .view1 import view1

        app.register_blueprint(view1, url_prefix = '/')

        from .models import Doctor, Appointment

        with app.app_context():
                db.create_all()

        return app

