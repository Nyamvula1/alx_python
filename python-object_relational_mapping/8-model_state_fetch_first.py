from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == "__main__":
    def print_first_state(username = argv[1], password = argv[2], database= argv[3]):
        engine = create_engine(f"mysql+mysqldb://{username}:{password}@localhost/{database}", pool_pre_ping=True)

        Session = sessionmaker(bind=engine)
        session = Session()

        state = session.query(State).order_by(State.id).first()
        
        if state: 
            print("{}: {}".format(state.id, state.name))
        else:
            print("Nothing")   
        session.close()
    print_first_state()