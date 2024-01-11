from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO
from dotenv import load_dotenv
import os


socketio = SocketIO(cors_allowed_origins="*")

load_dotenv()

app = Flask(__name__)
app.json_provider_class.sort_keys = False
CORS(app)



app.config['SQLALCHEMY_DATABASE_URI'] = os.environ["SQLALCHEMY_DATABASE_URI"]
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SECRET_KEY'] = os.environ["SECRET"]
db = SQLAlchemy(app)
socketio.init_app(app)


from application import routes
