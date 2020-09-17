from flask import request
from flask_restful import Resource
from marshmallow import ValidationError
from backend.app.schemas import employee_schema, salary_schema
from backend.app.model.models import SalaryModel, BaseWorker
from backend.database.database import Session


class EmployeeList(Resource):
    def get(self):
        """List all registered users"""
        session = Session()
        list_employees = session.query(BaseWorker,SalaryModel).join(SalaryModel)
        empl_result = employee_schema.dump(list_employees, many=True)
        return empl_result

    def post(self):
        'create new worker'
        session = Session()
        json_data = request.json
        # salary_data = salary_schema.load({'salary':json_data.pop('salary')})
        salary_data = json_data.pop('salary')
        data = employee_schema.load(json_data)
        new_worker_salary = SalaryModel(salary=salary_data)
        session.add(new_worker_salary)
        session.commit()
        # new_worker_salary_id = session.query(SalaryModel).get(new_worker_salary.id)
        new_worker = BaseWorker(salary_id=new_worker_salary.id, **data)
        session.add(new_worker)
        session.commit()
        response = {'User': f'{data["name"]}', 'message': 'successfully added'}
        return response


class Employee(Resource):
    'update employee'

    def get(self, id):
        "get emloyee by id"
        pass

    def put(self, id):
        'update employee'
        pass

    def delete(self, id):
        pass


class Salary(Resource):
    "salary operations"

    def post(self):
       pass