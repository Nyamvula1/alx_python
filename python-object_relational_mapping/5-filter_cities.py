import sys
import MySQLdb

if __name__ == "__main__":
    # Connect to the MySQL database
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()

    # Execute an SQL query to select cities and states, ordered by city id
    query = ("""SELECT cities.name \
               FROM cities \
               INNER JOIN states ON state_id = states.id \
               WHERE states.name = %s \
               ORDER BY cities.id""")
               
    c.execute(query, (sys.argv[4],))
    cities = c.fetchall()
    print(", ".join(city[0] for city in cities))

    # Close the cursor and database connection
    c.close()
    db.close()
    # Print the results as a comma-separated string
    # states = c.fetchall()
    # #join is used in joining the values in the list
    # for i, state in enumerate (states):
    #     if i == len(states)-1:
    #         print(", ".join(states[0], end = '' ))
    #     else:
    #         print("".join(state[0], end=','))
    
    
    # c.close()
