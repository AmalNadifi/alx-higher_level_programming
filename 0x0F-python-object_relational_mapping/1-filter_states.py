#!/usr/bin/python3
""" The following script lists all states from
the database hbtn_0e_0_usa
"""


import MySQLdb
import sys

if __name__ == '__main__':
    """
    Accessing the database and getting the states
    """
    # Connecting to the database and retrieving states
    db = MySQLdb.connect(
            host="localhost", user=sys.argv[1], passwd=sys.argv[2],
            db=sys.argv[3], port=3306)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states where name \
            LIKE BINARY 'N%' ORDER BY states.id ASC")
    rows = cursor.fetchall()

    # Printing the results
    for row in rows:
        print(row)

    # Closing the cursor and database connection
    cursor.close()
    db.close()
