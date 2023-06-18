#!/usr/bin/python3
"""
Script listing all cities from the database 'hbtn_0e_4_usa'.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """Function that connects to MySQL server."""

    db_conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                              passwd=argv[2], db=argv[3])

    cur = db_conn.cursor()

    cur.execute("SELECT cities.id, cities.name, states.name \
                 FROM cities \
                 JOIN states \
                 ON cities.state_id = states.id \
                 ORDER BY cities.id ASC")
    query_rows = cur.fetchall()

    if query_rows is not None:
        for row in query_rows:
            print(row)
