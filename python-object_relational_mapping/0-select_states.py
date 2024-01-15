# Lists all states from the database hbtn_0e_0_usa.
import MySQLdb
from sys import argv

mysql_username = argv[1]
mysql_pass = argv[2]
db_name = argv[3]

if __name__ == "__main__":
    my_conn = MySQLdb.connect(host = 'localhost',mysql_pass = 'passwd',port=3306,mysql_username = 'user',db_name='db')
    c = my_conn.cursor()
    my_conn.execute("SELECT * FROM `states`")
    [print(state) for state in my_conn.fetchall()]