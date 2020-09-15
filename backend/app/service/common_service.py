from backend.database.database import Session
from backend.app.model.base_worker_model import BaseWorker



def get_all_employee():
    session = Session()
    response = session.query(BaseWorker).all()
    return response