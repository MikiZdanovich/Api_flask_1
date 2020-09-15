from flask_restplus import Namespace, fields


class EmployeeDto:
    employee_api = Namespace('Employee', description='Employee related operations')
    employee = employee_api.model('Employee', {
        'name': fields.String(required=True, description='Employee name'),
        'salary': fields.Integer(required=True, description='Employee salary'),
        'company': fields.String(required=True, description='Employee company'),
        'years_of_experience': fields.Integer(description='Employee years_of_experience'),
        'lunchtime': fields.DateTime(description='Employee lunchtime')
    })


class ManagementDto:
    management_api = Namespace('Management', description='Management related operations')
    management = management_api.model('Management', {
        'name': fields.String(required=True, description='Management name'),
        'salary': fields.Integer(required=True, description='Management salary'),
        'company': fields.String(required=True, description='Management company'),
        'reception_hours': fields.Integer(description='Management reception_hours')
    })


class CommonDto:
    common_api = Namespace('Worker', description='Workers related operations')
    common_employee = common_api.model('Worker', {
        'name': fields.String(required=True, description='Worker name')})
