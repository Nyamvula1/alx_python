import sys
import MySQLdb

if __name__ == "__main__":
    # Connect to the MySQL database
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()

    # Use query to select records where the second column matches the provided state name
    query = "SELECT * FROM `states` WHERE name = %s"
    c.execute(query, (sys.argv[4],))
    #Define a parameterized SQL query to select all 
    # records from the states table where the name 
    # column matches the provided state name. 
    # The %s is a placeholder for the parameter.
    # The execute method is then used to execute the query,
    # and the second argument is a tuple 
    # containing the value to be substituted for the %s placeholder.

    # Fetch and print the results
    [print(state) for state in c.fetchall()]

    # Close the database connection
    db.close()