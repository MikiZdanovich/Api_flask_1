from sqlalchemy import Integer, String, Column, Time, Date,  ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from backend.database.database import metadata as mymeta

Base = declarative_base(metadata=mymeta)


class BaseWorker(Base):
    __tablename__ = 'employees'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(64), index=True, unique=False)
    company = Column(String(64), unique=False)
    reception_hours = Column(Time, nullable=True, unique=False)
    years_of_experience = Column(Integer, default=0, unique=False)
    lunchtime = Column(Date, nullable=True, unique=False)
    salary_id = Column(Integer, ForeignKey("salary.id"))
    salary = relationship('SalaryModel',back_populates='employees')

    def __repr__(self):
        return '<User %r>' % (self.name)


class SalaryModel(Base):
    __tablename__ = 'salary'

    id = Column(Integer, primary_key=True, autoincrement=True)
    salary = Column(Integer, index=True, unique=False)
    employees = relationship('BaseWorker', uselist=False, back_populates='salary')

