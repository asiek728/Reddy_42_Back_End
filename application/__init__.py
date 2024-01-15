from flask import Flask, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

from dotenv import load_dotenv
import os
load_dotenv()

#################################################
# from auth import auth_bp
# from users import user_bp

from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    jwt_required,
    get_jwt,
    current_user,
    get_jwt_identity,
)
#################################################



app = Flask(__name__)
app.json_provider_class.sort_keys = False

CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ["SQLALCHEMY_DATABASE_URI"]
app.config['SECRET_KEY'] = os.environ["SECRET_KEY"]
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)



###################################################################
#register blueprints:
# app.register_blueprint(auth_bp, url_prefix='/auth')
# app.register_blueprint(auth_bp)
# app.register_blueprint(user_bp)

from application.patients.model import Patient, TokenBlocklist

jwt = JWTManager(app)  ## check if this is the notation

@jwt.user_lookup_loader
def user_lookup_callback(_jwt_headers, jwt_data):
    identity = jwt_data["sub"]

    return Patient.query.filter_by(email=identity).one_or_none()

@jwt.additional_claims_loader
def make_additional_claims(identity):
    if identity == "alextesting2@test.com":
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
###################################################################



from application import routes

