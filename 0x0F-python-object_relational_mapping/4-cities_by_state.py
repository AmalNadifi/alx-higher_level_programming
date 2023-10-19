#!/usr/bin/python3
""" The following script:
* lists  all cities from the database hbtn_0e_4_usa
"""


import MySQLdb
import sys

if __name__ == '__main__':
    """
    Accessing the database and getting the cities
    """
    # Connecting to the database and retrieving cities
    db = MySQLdb.connect(
            host="localhost", user=sys.argv[1], passwd=sys.argv[2],
            db=sys.argv[3], port=3306)
    cursor = db.cursor()
    cursor.execute(
        "SELECT cities.id, cities.name, states.name FROM cities \
        JOIN states ON cities.state_id = states.id \
        ORDER BY cities.id ASC")
    rows = cursor.fetchall()

    # Printing the results
    for row in rows:
        print(row)

    # Closing the cursor and database connection
    cursor.close()
    db.close()
