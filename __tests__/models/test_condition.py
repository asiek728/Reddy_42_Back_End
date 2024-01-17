from application.conditions.model import Condition

def test_create_condition():
    condition = Condition("email10@email.com", "broken leg", "2reckless jumping off the curb", "2024-5-12", "2024-5-12", "/9j/4AAQSkZJRgABAQAAA" )

    assert condition.patient_email == "email10@email.com"
    assert condition.condition_name == "broken leg"
    assert condition.description == "2reckless jumping off the curb"
    assert condition.start_date == "2024-5-12"
    assert condition.end_date == "2024-5-12"
    assert condition.image == "/9j/4AAQSkZJRgABAQAAA"
