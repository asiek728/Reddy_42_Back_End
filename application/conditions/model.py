from application import db, app

app.app_context().push()

class Condition(db.Model):

    __tablename__ = "conditions"

    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'))
    condition_name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date,  default=(2003, 3, 25))

    def __init__(self, patient_id, condition_name, description, start_date, end_date):
        self.patient_id = patient_id
        self.condition_name = condition_name
        self.description = description
        self.start_date = start_date
        self.end_date = end_date

    @property
    def json(self):
        return {
            "id": self.id,
            "patient_id": self.patient_id,
            "condition_name": self.condition_name,
            "description": self.description,
            "start_date": self.start_date,
            "end_date": self.end_date
        }
