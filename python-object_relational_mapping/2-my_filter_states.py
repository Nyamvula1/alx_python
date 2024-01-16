import sys
import MySQLdb

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * \
                 FROM `states` \
                WHERE BINARY `name` = '{}'".format(sys.argv[4]))
    [print(state) for state in c.fetchall()]



# Check if the required command line arguments are provided
#if len(sys.argv) != 5:
    #print("Usage: python script.py <username> <password> <database> <state_name>")
    #sys.exit(1)

# Get user input from command line arguments
#username, password, database, state_name = sys.argv[1:5]

# Connect to the MySQL database
#db = MySQLdb.connect(user=username, passwd=password, db=database)
#c = db.cursor()

# Use format to create the SQL query with user input
#query = "SELECT * FROM `states` WHERE LOWER (`name`) = LOWER('{}') ORDER BY `id`".format(state_name)
#c.execute(query)

# Fetch and print the results
#for state in c.fetchall():
    #print(state)

# Close the database connection
#db.close()







#import sys
#import MySQLdb

#if len =
#if __name__ == "__main__":
    #db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    #c = db.cursor()
    #c.execute("SELECT * FROM `states` ORDER BY `id`")
    #[print(state) for state in c.fetchall() if state[1][0] == "N"]