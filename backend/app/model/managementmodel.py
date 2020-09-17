from sqlalchemy import Time, Column
from backend.app.model.models import BaseWorker


class ManagementModel(BaseWorker):
    reception_hours = Column(Time, nullable=True, unique=False)
