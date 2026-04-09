#!/usr/bin/python3
"""Filter states by user input"""

import MySQLdb
import sys


if __name__ == "__main__":
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cur = conn.cursor()
    query = "SELECT * FROM states WHERE BINARY name = '{}' " \
            "ORDER BY states.id ASC".format(sys.argv[4])
    cur.execute(query)

    for row in cur.fetchall():
        print(row)

    cur.close()
    conn.close()
