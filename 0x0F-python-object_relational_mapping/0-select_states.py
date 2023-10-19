#!/usr/bin/python3
""" The following script lists all states from
the database hbtn_0e_0_usa
"""


import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Accessing the database and getting the states
    """
    # Connecting to the database and retrieving states
    mysql_username, mysql_password, database_name = sys.argv[1],
    sys.argv[2], sys.argv[3]
    db = MySQLdb.connect(
            host="localhost", user=argv[1], passwd=argv[2],
            db=argv[3], port=3306)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states")
    rows = cursor.fetchall()

    # Printing the results
    for row in rows:
        print(row)

    # Closing the cursor and database connection
    cursor.close()
    db.close()
