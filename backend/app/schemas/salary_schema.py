from marshmallow import Schema, fields


class BaseSalarySchema(Schema):
    id = fields.Integer(dump_only=True)
    salary = fields.Integer(required=True)
