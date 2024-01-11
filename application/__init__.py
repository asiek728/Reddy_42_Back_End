from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from flask_socketio import SocketIO
import os

from flask_login import LoginManager

# from application import routes
# from application.patients import routes

load_dotenv()

app = Flask(__name__)
app.json_provider_class.sort_keys = False
allowed_origins = ["http://localhost:5173", "http://localhost:5174", "http://localhost:5175"]
CORS(app, origins=allowed_origins)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ["SQLALCHEMY_DATABASE_URI"]
# app.config['SECRET_KEY'] = os.environ["SECRET_KEY"]
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

socketio = SocketIO(app, cors_allowed_origins=allowed_origins)

from application import routes
