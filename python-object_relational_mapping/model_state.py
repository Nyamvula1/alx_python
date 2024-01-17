'''Module to be imported'''

import sqlalchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    '''State class'''
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name =  Column(String(128), nullable=False)





# '''module to be imported'''
# from sqlalchemy from sqlalchemy import Column, Integer, String
# from sqlalchemy.ext.declarative import declarative_base

# Base = declarative_base()
# '''state class'''
# class state(Base):
#     '''The State class'''
    
#     __tablename__ = 'states'
#     id = Column(Integer, primary_key=True)
#     name =  Column(String(128), nullable= False)
