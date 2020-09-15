from flask import request
from flask_restplus import Resource


from backend.app.service.employee_service import save_new_employee
from backend.app.util.dto import ManagementDto

api = ManagementDto.management_api
_management = ManagementDto.management

@api.route('/Employees')
class EmployeeList(Resource):

    @api.response(201, 'User successfully created.')
    @api.doc('create a new user')
    @api.expect(_management, validate=True)
    def post(self):
        """Creates a new User """
        data = request.json
        return save_new_employee(data=data)

