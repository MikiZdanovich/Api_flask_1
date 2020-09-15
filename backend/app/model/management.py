from sqlalchemy import Date, Column
from backend.app.model.base_worker_model import BaseWorker


class _Manager(BaseWorker):
    reception_hours = Column(Date, nullable=True, unique=False)
