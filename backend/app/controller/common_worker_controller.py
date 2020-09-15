from flask import request
from flask_restplus import Resource

from backend.app.service.common_service import get_all_employee
from backend.app.util.dto import CommonDto

api = CommonDto.common_api
common_employees = CommonDto.common_employee


@api.route('/Employee')
class EmployeeList(Resource):
    @api.doc('list_of_registered_Employee')
    @api.marshal_list_with(common_employees)
    def get(self):
        """List all registered users"""
        return get_all_employee()
