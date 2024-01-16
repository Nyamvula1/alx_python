import sys
import MySQLdb

if __name__ == "__main__":
    # Connect to the MySQL database
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()

    # Use query to select records where the second column matches the provided state name
    query = "SELECT * FROM `states` WHERE name = %s"
    c.execute(query, (sys.argv[4],))

    # Fetch and print the results
    [print(state) for state in c.fetchall()]

    # Close the database connection
    db.close()