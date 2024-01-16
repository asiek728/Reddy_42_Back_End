from application import db, app
from application.patients.model import Patient
import base64

app.app_context().push()

class Condition(db.Model):

    # __tablename__ = "conditions"

    id = db.Column(db.Integer, primary_key=True)
    patient_email = db.Column(db.String(100), db.ForeignKey('patient.email'))
    condition_name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date,  default=(2003, 3, 25))
    image = db.Column(db.LargeBinary)


    def __init__(self, patient_email, condition_name, description, start_date, end_date, image):
        self.patient_email = patient_email
        self.condition_name = condition_name
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
        self.image = image
#$#############################################
    @classmethod
    def get_conditions_by_email(cls, email):
        return cls.query.filter_by(email=email).all()
    

    
#$#############################################
    @property
    def json(self):
        image_data_base64 = base64.b64encode(self.image).decode('utf-8') if self.image else None

        return {
            "id": self.id,
            "patient_email": self.patient_email,
            "condition_name": self.condition_name,
            "description": self.description,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "image_data_base64": image_data_base64
        }
