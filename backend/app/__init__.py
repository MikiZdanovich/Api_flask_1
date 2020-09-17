import os
from flask import Flask
from flask_restful import Api

from backend.app.employees.resources import EmployeeList, Employee
from backend.database.database import configure_engine, metadata
from backend.app.config import config_by_name


def create_app(config_name):
    # engine = configure_engine(os.getenv('DATABASE_URL'))
    engine = configure_engine('postgresql://user:password@localhost:5432/db_1')
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    api = Api(app)
    api.add_resource(EmployeeList, '/employees')
    api.add_resource(Employee, '/employees/<id>')
    metadata.bind = engine
    return app
