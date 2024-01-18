import json

def test_localhost_route(client):
    response = client.get("/")
    assert response.status_code == 200

    response2 = client.get("/patients")
    assert response2.status_code == 200
    
    data = {
        "first_name": "first_name",
        "last_name": "last_name",
        "email": "email125@example.com",
        "password": "password",
        "nhs_number": "true",
        "date_of_birth": "2005-10-12",
        "sex": "F",
        "ethnicity": "White"
    }

    response2b = client.post("/patients", data=json.dumps(data), content_type="application/json")
    assert response2b.status_code == 201 

    data2 = {
        "patient_email": "email",
        "related_patient_email": "email@email.com",
    }

    response2c = client.post("/create_relationship", data=json.dumps(data2), content_type="application/json")
    assert response2c.status_code == 201 

    response3 = client.get("/patients/email/email")
    assert response3.status_code == 200

    response4 = client.get("/patients/email/email2")
    assert response4.status_code == 404

    response5 = client.get("/patients/email@email.com")
    assert response5.status_code == 200

    response6 = client.get("/patients/email@email.com/family")
    assert response6.status_code == 200

    response7 = client.get("/conditions/users/email@email.com")
    assert response7.status_code == 200

    response8 = client.get("/conditions/1")
    assert response8.status_code == 200

    data3 = {
        "patient_email": "email@email.com",
        "condition_name": "name",
        "description": "description",
        "start_date": "2023-6-21",
        "end_date": "2023-6-21",
        "image": "/9j/4AAQSkZJRgABAQAAA"
    }

    response8b = client.post("/conditions", data=json.dumps(data3), content_type="application/json")
    assert response8b.status_code == 201 

    data4 = {
        "patient_email": "emailwerwer@email.com"
    }
    response8c = client.post("/conditions", data=json.dumps(data4), content_type="application/json")
    assert response8c.status_code == 500

    response8d = client.get("/conditions")
    assert response8d.status_code == 200

    response9 = client.get("/hereditary_conditions")
    assert response9.status_code ==  404

    response10 = client.get("/hereditary_conditions/users/email2@email.com")
    assert response10.status_code == 404

    


#pipenv run coverage



