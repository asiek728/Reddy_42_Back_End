from application.hereditary_conditions.model import HereditaryCondition
from application.patients.model import Patient

def test_create_hereditary_condition():
    hereditary_condition1 = HereditaryCondition("email", "Albinism")

    assert hereditary_condition1.email == 'email'
    assert hereditary_condition1.hereditary_condition_name == 'Albinism'

    hereditary_json = hereditary_condition1.json
    expected_json = {
        'id': hereditary_condition1.id,
        'email': 'email',
        'hereditary_condition_name': 'Albinism',
    }
    assert hereditary_json == expected_json



#pipenv run coverage
    

from application import db, app
app.app_context().push()

def test_get_hereditary_conditions_by_email():

    db.session.rollback()
    db.drop_all()
    db.create_all()

    patient1 = Patient(first_name="first_name1", last_name="last_name1", email="email1@email.com", password="password1", nhs_number="False", date_of_birth="2022-3-20", sex="M", ethnicity="White")
    patient2 = Patient(first_name="first_name2", last_name="last_name2", email="email2@email.com", password="password2", nhs_number="False", date_of_birth="2022-3-20", sex="F", ethnicity="White")

    hereditary_condition1 = HereditaryCondition("email1@email.com", "Condition1")
    hereditary_condition2 = HereditaryCondition("email1@email.com", "Condition2")

    db.session.add(patient1)
    db.session.add(patient2)
    db.session.add(hereditary_condition1)
    db.session.add(hereditary_condition2)
    db.session.commit()

    existing = HereditaryCondition.get_hereditary_conditions_by_email("email1@email.com")

    assert len(existing) == 2
    assert existing[0].hereditary_condition_name == "Condition1"
    assert existing[1].hereditary_condition_name == "Condition2"

    nonExisting = HereditaryCondition.get_hereditary_conditions_by_email("nonexistent@example.com")

    assert len(nonExisting) == 0

    db.session.rollback()

