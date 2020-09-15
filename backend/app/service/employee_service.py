from backend.app.model.employee import _Employee
from backend.database.database import Session


def save_new_employee(data):
    new_employee = _Employee(

        name=data['name'],
        salary=int(data['salary']),
        company=data['company'],
        years_of_experience=int(data['years_of_experience']),
        lunchtime=data['lunchtime']
    )
    session = Session()
    session.add(new_employee)
    session.commit()
    response_object = {
        'status': 'success',
        'message': 'Employee successfully added'
    }
    return response_object, 200





def edit_employee(data):
    session = Session()
    updated_employee = session.query(_Employee).get(data['id'])
    updated_employee.data['update'] = data['updated']
    session.add(updated_employee)
    session.commit()
    response_object = {
        'status': 'success',
        'message': 'Employee successfully updated'
    }
    return response_object, 200
