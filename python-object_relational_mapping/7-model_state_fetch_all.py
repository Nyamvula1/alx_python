import sys
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
from model_state import State

def print_states(username, password, database):
    # Connect to the database
    engine = create_engine(f"mysql+mysqldb://{username}:{password}@localhost/{database}", pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Retrieve and print states
    states = session.query(State).all()
    for state in states:
        print(f"{state.id}: {state.name}")
    
    # Close the session
    session.close()

if __name__ == "__main__":
    # Check if enough command-line arguments are provided
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database>")
        sys.exit(1)

    # Get user input from command line arguments
    username, password, database = sys.argv[1:4]

    # Call the function to print state information
    print_states(username, password, database)










# import sys
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# from model_state import State

# if __name__ == "__main__":
#     engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
#                            .format(sys.argv[1], sys.argv[2], sys.argv[3]),
#                            pool_pre_ping=True)
#     Session = sessionmaker(bind=engine)
#     session = Session()

#     for state in session.query(State).order_by(State.id):
#         print("{}: {}".format(state.id, state.name))