#!/usr/bin/python3

# import the MySQLdb module for connecting to MySQL database
import MySQLdb

# import the sys module for accessing command-line arguments
import sys

if __name__ == '__main__':
    # check if the number of command-line arguments is correct
    if len(sys.argv) != 4:
        print("Usage: {} <mysql username> <mysql password> <database name>".format(sys.argv[0]))
        sys.exit(1)

    # assign the command-line arguments to variables
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # create a connection object using the MySQLdb.connect() method
    # and pass the connection details as parameters
    conn = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=username,
        passwd=password,
        db=database)

    # create a cursor object using the connection object's cursor() method
    cur = conn.cursor()

    # define the query to be executed
    query = (
        "SELECT cities.id, cities.name, states.name "
        "FROM cities "
        "JOIN states ON cities.state_id = states.id "
        "ORDER BY cities.id ASC")

    # execute the query using the cursor's execute() method
    cur.execute(query)

    # iterate over the result set and print each row
    for row in cur.fetchall():
        print(row)

    # close the cursor and connection objects
    cur.close()
    conn.close()

