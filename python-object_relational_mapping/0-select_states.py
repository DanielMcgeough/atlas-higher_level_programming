#!/usr/bin/python3
"""
This script lists all states from the
database named 'hbtn_0e_0_usa'
"""


import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    This accesses the database to get
    the states.
    """
    db_connect = MySQLdb.connect(
        host="localhost", user=argv[1], port=3306, passwd=argv[2], dv=argv[3])
    db_cursor = db_connect.cursor()
    db_cursor.execute("SELECT * FROM states")

    rows_selected = db_cursor.fetchall()

    for row in rows_selected:
        print(row)
