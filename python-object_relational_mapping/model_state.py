from sqlalchemy from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class state(Base):
    #The State class inherits from Base and is linked to the MySQL table 'states'. It has two class attributes, id and name, representing columns in the database.
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name =  Column(String(128), nullable= False)
