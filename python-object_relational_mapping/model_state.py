import sys
from model_state import Base, State

from sqlalchemy import (create_engine)

#The State class inherits from Base and is linked to the MySQL table 'states'. It has two class attributes, id and name, representing columns in the database.
class state(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = name = Column(String(128), nullable=False)
