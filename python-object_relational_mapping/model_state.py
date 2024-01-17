import sys
from model_state import Base, State

from sqlalchemy import (create_engine)

class state(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = name = Column(String(128), nullable=False)
