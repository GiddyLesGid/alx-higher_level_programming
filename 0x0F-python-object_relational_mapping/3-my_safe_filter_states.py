#!/usr/bin/python3
"""
Script that takes in arguments and displays all values in the states table of
hbtn_0e_0_usa where name matches the argument. This version is safe from MySQL
injections.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Connect to MySQL database
    conn = MySQLdb.connect(host="localhost",
                           user=sys.argv[1],
                           passwd=sys.argv[2],
                           db=sys.argv[3],
                           port=3306,
                           charset="utf8")

    # Create cursor object and execute query with parameterized input
    cur = conn.cursor()
    query = "SELECT * FROM states WHERE name=%s ORDER BY id ASC"
    cur.execute(query, (sys.argv[4],))

    # Print query results
    for row in cur.fetchall():
        print(row)

    # Close cursor and database connection
    cur.close()
    conn.close()

