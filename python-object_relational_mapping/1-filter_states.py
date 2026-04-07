#!/usr/bin/python3
"""Lists states starting with N"""

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
    cur.execute(
        "SELECT * FROM states WHERE name LIKE BINARY 'N%' "
        "ORDER BY states.id ASC"
    )

    for row in cur.fetchall():
        print(row)

    cur.close()
    conn.close()
