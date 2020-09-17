from sqlalchemy import Integer, Date, Column
from backend.app.model.models import BaseWorker


class EmployeeModel(BaseWorker):
    years_of_experience = Column(Integer, default=0, unique=False)
    lunchtime = Column(Date, nullable=True, unique=False)

