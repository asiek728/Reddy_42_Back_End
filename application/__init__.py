from flask import Flask, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from datetime import timedelta

from dotenv import load_dotenv
from flask_socketio import SocketIO
import os
load_dotenv()

app = Flask(__name__)
app.json_provider_class.sort_keys = False
allowed_origins = ["http://localhost:5173", "http://localhost:5174", "http://localhost:5175"]

CORS(app)


app.config['SQLALCHEMY_DATABASE_URI'] = os.environ["SQLALCHEMY_DATABASE_URI"]
app.config['SECRET_KEY'] = os.environ["SECRET_KEY"]
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024 

app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)
app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(days=30)

db = SQLAlchemy(app)

from application.patients.model import Patient, TokenBlocklist

jwt = JWTManager(app) 

@jwt.user_lookup_loader
def user_lookup_callback(_jwt_headers, jwt_data):
    identity = jwt_data["sub"]

    return Patient.query.filter_by(email=identity).one_or_none()


@jwt.additional_claims_loader
def make_additional_claims(identity):
    if identity == "NHS@email.com":
        return {"is_staff": True}
    return {"is_staff": False}



@jwt.expired_token_loader
def expired_token_callback(jwt_header, jwt_data):
    return jsonify({"message": "Token has expired", "error": "token_expired"}), 401


@jwt.invalid_token_loader
def invalid_token_callback(error):
    return (
        jsonify(
            {"message": "Signature verification failed", "error": "invalid_token"}
        ),
        401,
    )


@jwt.unauthorized_loader
def missing_token_callback(error):
    return (
        jsonify(
            {
                "message": "Request doesnt contain valid token",
                "error": "authorization_header",
            }
        ),
        401,
    )


@jwt.token_in_blocklist_loader
def token_in_blocklist_callback(jwt_header,jwt_data):
    jti = jwt_data['jti']

    token = db.session.query(TokenBlocklist).filter(TokenBlocklist.jti == jti).scalar()

    return token is not None

from application import routes

socketio = SocketIO(app, cors_allowed_origins=allowed_origins)

from application.socketio_events import init_socketio_events
init_socketio_events(socketio)

