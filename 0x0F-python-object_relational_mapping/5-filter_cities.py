#!/usr/bin/python3
""" The following script:
* takes in the name of a state as an argument
* and lists all cities of that state, using the database hbtn_0e_4_usa
"""


import MySQLdb
import sys

if __name__ == '__main__':
    """
    Accessing the database and getting the cities of the given state
    """
    # Connecting to the database and retrieving cities
    db = MySQLdb.connect(
            host="localhost", user=sys.argv[1], passwd=sys.argv[2],
            db=sys.argv[3], port=3306)
    cursor = db.cursor()
    cursor.execute("""
    SELECT
    cities.name
    FROM
    cities
    INNER JOIN
    states
    ON
    states.id=cities.state_id
    WHERE
    states.name LIKE BINARY %(state_name)s
    ORDER BY
    cities.id ASC
    """, {'state_name': sys.argv[4]})
    rows = cursor.fetchall()

    # Printing the results
    temp = list(row[0] for row in rows)
    print(*temp, sep=", ")

    # Closing the cursor and database connection
    cursor.close()
    db.close()
