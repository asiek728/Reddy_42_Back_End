from marshmallow import fields, Schema

class UserSchema(Schema):
    id = fields.String()
    first_name = fields.String()
    last_name = fields.String()
    email = fields.String()
    # password = fields.String()
    nhs_number = fields.String()
    date_of_birth = fields.String()
    sex = fields.String()
    ethnicity = fields.String()
