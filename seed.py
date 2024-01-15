from application import db
from application.patients.model import Patient, TokenBlocklist
from application.conditions.model import Condition

# from application.models import Condition, Patient

# db.metadata.drop_all(bind=None, tables=[Condition.__table__, Patient.__table__])
# Condition.__table__.drop(db.engine)
# Patient.__table__.drop(db.engine)
# print("Dropping Database")


db.create_all()
print("Creating Database")

print("Seeding Database")
patient1 = Patient(first_name="david", last_name="Fraser", email="email10@email.com", password="encrypted", nhs_number="True", date_of_birth="2022-3-20", sex="m", ethnicity="white")
patient2 = Patient(first_name="Joanna", last_name="looool", email="email11@email.com", password="encrypted", nhs_number="True", date_of_birth="2022-3-20", sex="f", ethnicity="white")
patient3 = Patient(first_name="yo mama", last_name="yo daddy", email="email12@email.com", password="encrypted", nhs_number="True", date_of_birth="2022-3-20", sex="f", ethnicity="white")
patient4 = Patient(first_name="alex", last_name="Warden", email="email13@email.com", password="encrypted", nhs_number="True", date_of_birth="2022-3-20", sex="m", ethnicity="white")
patient5 = Patient(first_name="leslie", last_name="jordan", email="email14@email.com", password="encrypted", nhs_number="True", date_of_birth="2022-3-20", sex="f", ethnicity="white")

condition1 = Condition(patient_id=1, condition_name="dying", description="too much swag", start_date="2000-6-21", end_date="2024-5-12")
condition2 = Condition(patient_id=3, condition_name="dying", description="too much swag", start_date="2000-6-21", end_date="2024-5-12")
condition3 = Condition(patient_id=3, condition_name="dying", description="too much swag", start_date="2000-6-21", end_date="2024-5-12")
condition4 = Condition(patient_id=4, condition_name="dying", description="too much swag", start_date="2000-6-21", end_date="2024-5-12")




db.session.add_all([patient1, patient2, patient3, patient4, patient5, condition1, condition2, condition3, condition4])
    # id = db.Column(db.Integer, primary_key=True)
    # patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'))
    # condition = db.Column(db.String(100), nullable=False)
    # description = db.Column(db.String(100), nullable=False)
    # start_date = db.Column(db.Date, nullable=False)
    # end_date = db.Column(db.Date)
db.session.commit()

