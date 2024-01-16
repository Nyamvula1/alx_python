#This code retrieves all records from the 'states' table, 
# orders them by the 'id' column, and then prints only those states where the 
# second character of the second column starts with "N".
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    
    #Execute an SQL query to select all columns (*) 
    # from the 'states' table and order the results by the 'id' column.
    c.execute("SELECT * FROM `states` ORDER BY `id`")
    
    #Fetch all the results of the query and use a list comprehension 
    # to print each state where the second character of the second 
    # column (state[1][0]) is equal to "N".
    [print(state) for state in c.fetchall() if state[1][0] == "N"]