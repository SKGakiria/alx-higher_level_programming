#!/usr/bin/python3
"""
Script takes in an argument and displays all values in the states
table of 'hbtn_0e_0_usa' where name matches the argument. This time
the script is safe from MySQL injections!
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """Function that connects to MySQL server."""

    db_conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                              passwd=argv[2], db=argv[3])

    cur = db_conn.cursor()

    cur.execute("SELECT * FROM states WHERE name LIKE BINARY %(name)s \
            ORDER BY states.id ASC", {'name': argv[4]})
    query_rows = cur.fetchall()

    for row in query_rows:
        print(row)
