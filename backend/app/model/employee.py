from sqlalchemy import Integer, Date, Column
from backend.app.model.base_worker_model import BaseWorker


class _Employee(BaseWorker):
    years_of_experience = Column(Integer, default=0, unique=False)
    lunchtime = Column(Date, nullable=True, unique=False)

