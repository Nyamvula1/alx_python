import sys
import MySQLdb

if __name__ == "__main__":
    # Connect to the MySQL database
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()

    # Execute an SQL query to select cities and states, ordered by city id
    c.execute("""SELECT cities.name \
               FROM cities \
               INNER JOIN states ON state_id = states.id \
               WHERE states.name = %s \
               ORDER BY cities.id, (sys.argv[4])
               """)

    # Print the results as a comma-separated string
    cities = c.fetchall()
    print(", ".join(city[0] for city in cities))
