from application.patients.model import Patient

def test_create_patient():
    new_patient = Patient(first_name="first_name", last_name="last_name", email="email@email.com", password="password", nhs_number="False", date_of_birth="2024-5-12", sex="M", ethnicity="White")

    assert new_patient.first_name == "first_name"
    assert new_patient.last_name == "last_name"
    assert new_patient.email == "email@email.com"
    assert new_patient.password == "password"
    assert new_patient.nhs_number == "False"
    assert new_patient.date_of_birth == "2024-5-12"
    assert new_patient.sex == "M"
    assert new_patient.ethnicity == "White"


