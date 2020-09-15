from sqlalchemy import Integer, String, Column, Date
from sqlalchemy.ext.declarative import declarative_base
from backend.database.database import metadata as mymeta

Base = declarative_base(metadata=mymeta)


class BaseWorker(Base):
    __tablename__ = 'base_table'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(64), index=True, unique=False)
    salary = Column(Integer, index=True, unique=False)
    company = Column(String(64), unique=False)

    def __repr__(self):
        return '<User %r>' % (self.name)
