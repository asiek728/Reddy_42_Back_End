from application import db, app
from application.patients.model import Patient

app.app_context().push()

class HereditaryCondition(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), db.ForeignKey('patient.email'))
    hereditary_condition_name = db.Column(db.String(100), nullable=False)

    def __init__(self, email, hereditary_condition_name):
        self.email = email
        self.hereditary_condition_name = hereditary_condition_name


#$#############################################
    @classmethod
    def get_hereditary_conditions_by_email(cls, email):
        return cls.query.filter_by(email=email).all()
    

    
#$#############################################
    @property
    def json(self):
        return {
            "id": self.id,
            "email": self.email,
            "hereditary_condition_name": self.hereditary_condition_name
        }
