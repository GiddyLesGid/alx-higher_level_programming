#!/usr/bin/python3
"""
Script that lists all cities of a given state using the database hbtn_0e_4_usa.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name,
        charset="utf8"
    )

    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities JOIN states ON cities.state_id = states.id WHERE states.name = %s ORDER BY cities.id", (state_name,))

    rows = cur.fetchall()
    cities = [row[0] for row in rows]

    print(", ".join(cities))

    cur.close()
    db.close()

