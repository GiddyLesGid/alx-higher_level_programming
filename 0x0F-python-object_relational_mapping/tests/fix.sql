#!/usr/bin/env python3

import MySQLdb

if __name__ == '__main__':
    conn = MySQLdb.connect(
        host='root',
        port=3306,
        user='your_username',
        passwd='your_password',
        db='hbtn_0e_4_usa')

    cur = conn.cursor()

    # First, create a temporary table to store unique rows
    cur.execute('CREATE TEMPORARY TABLE temp_cities '
                'LIKE cities')

    # Insert unique rows into the temporary table
    cur.execute('INSERT INTO temp_cities '
                'SELECT DISTINCT * FROM cities')

    # Drop the original table
    cur.execute('DROP TABLE cities')

    # Rename the temporary table to the original table name
    cur.execute('ALTER TABLE temp_cities '
                'RENAME TO cities')

    cur.close()
    conn.close()

