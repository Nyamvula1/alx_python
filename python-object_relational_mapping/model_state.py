import sys
from model_state import Base, State

from sqlalchemy import (create_engine)

class state(Base):
    #The State class inherits from Base and is linked to the MySQL table 'states'. It has two class attributes, id and name, representing columns in the database.
    __tablename__ = 'states'
    id = column(int(11) NOT NULL AUTO_INCREMENT)
    name = name = column(varchar(128) NOT NULL)
