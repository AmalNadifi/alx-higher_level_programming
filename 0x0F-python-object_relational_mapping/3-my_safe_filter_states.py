#!/usr/bin/python3
""" The following script:
* takes in an argument
* displays all values in the states table
of hbtn_0e_0_usa where name matches the argument.
* But this time it should be safe from MySQL injections!
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
    cursor.execute(
        "SELECT * FROM states WHERE name LIKE BINARY %(name)s \
                ORDER BY states.id ASC", {'name': sys.argv[4]})
    rows = cursor.fetchall()

    # Printing the results
    for row in rows:
        print(row)

    # Closing the cursor and database connection
    cursor.close()
    db.close()
