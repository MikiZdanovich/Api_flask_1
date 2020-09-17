# from sqlalchemy import Integer,  Column, ForeignKey
# from sqlalchemy.orm import relationship
# from sqlalchemy.ext.declarative import declarative_base
# from backend.database.database import metadata as mymeta
#
#
# Base = declarative_base(metadata=mymeta)
#
#
# class SalaryModel(Base):
#     __tablename__ = 'salary'
#
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     salary = Column(Integer, index=True, unique=False)
#     employees_id = Column(Integer, ForeignKey('employees.id'))
#     employees = relationship('BaseWorker', back_populates='salary')
#
#
