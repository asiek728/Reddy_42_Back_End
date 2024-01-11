from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

from flask_login import LoginManager

# from application import routes
# from application.patients import routes

load_dotenv()

app = Flask(__name__)
app.json_provider_class.sort_keys = False

CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ["SQLALCHEMY_DATABASE_URI"]
# app.config['SECRET_KEY'] = os.environ["SECRET_KEY"]

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)

from application.patients.routes import patients
app.register_blueprint(patients)









from application import routes

