import pytest
from application import app, db
from application.conditions.model import Condition
from application.patients.model import Patient
from application.hereditary_conditions.model import HereditaryCondition
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
        new_patient = Patient(first_name="first_name", last_name="last_name", email="email", password="password", nhs_number="nhs_number", date_of_birth="date_of_birth", sex="sex", ethnicity="ethnicity")

        # Inject it into the database
        db.session.add(new_patient)
        db.session.commit()

    return client

