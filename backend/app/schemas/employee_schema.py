from marshmallow import Schema, fields, validate


class BaseEmployeeSchema(Schema):
    id = fields.Integer()
    name = fields.String(required=True, validate=validate.Length(min=1))
    company = fields.String()
    years_of_experience = fields.Integer()
    lunchtime = fields.Date()
    reception_hours = fields.Time()

