from application import db, app
from uuid import uuid4
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

app.app_context().push()

def generate_uuid():
    return uuid4()

# Define the association table
patient_family = db.Table(
    'patient_association', db.Model.metadata,
    db.Column('patient_email', db.String(100), db.ForeignKey('patient.email')),
    db.Column('related_patient_email', db.String(100), db.ForeignKey('patient.email'))
)

class Patient(db.Model):
    # __tablename__ = "patients"
    
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(500), nullable=False)
    nhs_number = db.Column(db.String(100))
    date_of_birth = db.Column(db.Date, nullable=False, default=(2003, 3, 25)) #YMD format date_of_birth=date(2003,3,25)
    sex = db.Column(db.String(1), nullable=False)
    ethnicity = db.Column(db.String(100))
    
    # foreign keys
    conditions = db.relationship('Condition',backref='patient', lazy=True, cascade="all, delete")
    hereditary_conditions = db.relationship('HereditaryCondition',backref='patient', lazy=True, cascade="all, delete")

    # Define the many-to-many relationship
    related_patients = db.relationship(
        'Patient',
        secondary=patient_family,
        primaryjoin=(email == patient_family.c.patient_email),
        secondaryjoin=(email == patient_family.c.related_patient_email),
        backref='related_to'
)
    
    def __init__(self, first_name, last_name, email, password, nhs_number, date_of_birth, sex, ethnicity):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.nhs_number = nhs_number
        self.date_of_birth = date_of_birth
        self.sex = sex
        self.ethnicity = ethnicity
    
    # def __repr__(self):
    #     return f"My name is {self.first_name} {self.last_name} i was born {self.date_of_birth} and my email is {self.email}"
    
###################################################################
    ## AUTH
    def __repr__(self):
        return f"<User {self.first_name}>"

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)
    
    @classmethod
    def get_user_by_email(cls, email):
        return cls.query.filter_by(email=email).first()
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
######################################################################
    
    @property
    def json(self):
        hereditary_conditions = []
        for condition in self.hereditary_conditions:
            hereditary_conditions.append({"id": condition.id,"hereditary_condition_name": condition.hereditary_condition_name})
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "password": self.password,
            "nhs_number": self.nhs_number,
            "date_of_birth": self.date_of_birth,
            "sex": self.sex,
            "ethnicity": self.ethnicity,
            "hereditary_conditions": hereditary_conditions or ""
        }
    
#####################################################################

class TokenBlocklist(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    jti = db.Column(db.String(), nullable=True)
    create_at = db.Column(db.DateTime(), default=datetime.utcnow)

    def __repr__(self):
        return f"<Token {self.jti}>"
    
    def save(self):
        db.session.add(self)
        db.session.commit()


###################################################################
