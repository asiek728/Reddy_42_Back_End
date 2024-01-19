import pytest
from application import app, db
from application.conditions.model import Condition
from application.patients.model import Patient
from application.hereditary_conditions.model import HereditaryCondition
import images
import base64

# Fixture 
@pytest.fixture
def client():
    
    # Create a test client to which we can make requests
    client = app.test_client()
    
    with app.app_context():
        db.session.rollback()
        db.drop_all()
        
    # Create a test database with some test data
    with app.app_context():
        # Create the database
        db.create_all()
        # Create fake data
        new_patient = Patient(first_name="first_name", last_name="last_name", email="email", password="password", nhs_number="nhs_number", date_of_birth="2022-3-20", sex="F", ethnicity="ethnicity")

        new_patient2 = Patient(first_name="first_name", last_name="last_name", email="email@email.com", password="password", nhs_number="nhs_number", date_of_birth="2022-3-20", sex="F", ethnicity="ethnicity")

        binary_image_data = base64.b64decode(images.base64_image_data)

        condition1 = Condition(patient_email="email@email.com", condition_name="broken leg", description="reckless jumping off the curb", start_date="2023-6-21", end_date="2024-5-12", image= binary_image_data )

        hereditary_condition1 = HereditaryCondition(email="email@email.com", hereditary_condition_name="Albinism")



        # Inject it into the database
        db.session.add(new_patient)
        db.session.add(new_patient2)
        db.session.add(condition1)
        db.session.add(hereditary_condition1)

        db.session.commit()

    return client

