#!/usr/bin/python3
"""
Script listing all states with a name starting with N (upper N)
from 'hbtn_0e_0_usa'.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """Function that connects to MySQL server."""

    db_conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                              passwd=argv[2], db=argv[3])

    cur = db_conn.cursor()

    cur.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' \
                 ORDER BY states.id ASC")
    query_rows = cur.fetchall()

    for row in query_rows:
        print(row)
