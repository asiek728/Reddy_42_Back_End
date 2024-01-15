from application.models import Patient, Condition

def test_new_patient():
    patient = Patient("Oliver", "man", "oliver@email.com", "password", True, "2001-3-4", "m", "white")
    
    assert patient.first_name == 'Oliver'
    assert patient.last_name == 'man'
    assert patient.email == "oliver@email.com"
    assert patient.password == "password"
    assert patient.nhs_number == True
    assert patient.date_of_birth == "2001-3-4"
    assert patient.sex == "m"
    assert patient.ethnicity == "white"

def test_new_condition():
    condition = Condition(3, "soar throat", "burning sensation in the throat", "2001-3-4", "2001-3-4")

    assert condition.patient_id == 3
    assert condition.condition_name == "soar throat"
    assert condition.description == "burning sensation in the throat"
    assert condition.start_date == "2001-3-4"
    assert condition.end_date == "2001-3-4"

    
    
    
    