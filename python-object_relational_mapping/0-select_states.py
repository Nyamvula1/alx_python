# Lists all states from the database hbtn_0e_0_usa.
import MySQLdb
from sys import argv
if __name__ == "__main__":
    mysql_username = argv[1]
    mysql_pass = argv[2]
    db_name = argv[3]

    my_conn = MySQLdb.connect(host = 'localhost', passwd = mysql_pass, port=3306, user = mysql_username, db = db_name)
    c = my_conn.cursor()
    c.execute("SELECT * FROM `states`")
    [print(state) for state in my_conn.fetchall()]