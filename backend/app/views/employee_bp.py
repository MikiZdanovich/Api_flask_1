from flask import Blueprint
from flask_restplus import Api

from backend.app.controller.employee_controller import api as employee_ns
from backend.app.controller.common_worker_controller import api as common_ns



blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='FLASK RESTPLUS API BOILER-PLATE WITH JWT',

          description='a boilerplate for flask restplus web service'
          )
api.add_namespace(common_ns, path='/employees')
api.add_namespace(employee_ns, path='/add_new_employee/<type>')
