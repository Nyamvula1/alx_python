import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == "__main__":
    def print_first_state(username, password, database):
        engine = create_engine(f"mysql+mysqldb://{username}:{password}@localhost/{database}", pool_pre_ping=True)

        Session = sessionmaker(bind=engine)
        session = Session()

        state = session.query(State).order_by(State.id).first()
        if state is None:
            print("Nothing")
        else:
            print("{}: {}".format(state.id, state.name))
            
        session.close()