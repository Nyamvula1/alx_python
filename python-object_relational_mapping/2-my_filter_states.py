#Import the sys module, which provides access to 
# command-line arguments and other functionalities.
import sys
import MySQLdb

if __name__ == "__main__":
    # Connect to the MySQL database using 
    # command-line arguments.
    # sys.argv[1] is the username, sys.argv[2] is the password, and sys.argv[3] 
    # is the database name. A cursor (c) is created to execute SQL queries.
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    
     # Use format to create the SQL query with case-sensitive search
    c.execute("SELECT * \
                 FROM `states` \
                WHERE BINARY `name` = '{}'".format(sys.argv[4]))
    
    # Fetch and print the results
    [print(state) for state in c.fetchall()]















#import sys
#import MySQLdb

#if len =
#if __name__ == "__main__":
    #db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    #c = db.cursor()
    #c.execute("SELECT * FROM `states` ORDER BY `id`")
    #[print(state) for state in c.fetchall() if state[1][0] == "N"]