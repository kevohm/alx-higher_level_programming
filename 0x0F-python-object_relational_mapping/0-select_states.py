#!/usr/bin/python3
"""
This module runs a script to fetch all states table
in the database provided
"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    u = argv[1]
    p = argv[2]
    d = argv[3]
    db = MySQLdb.connect(host='localhost', port=3306, user=u, passwd=p, db=d)
    cur = db.cursor()
    cur.execute("SELECT * FROM states")
    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()
    db.close()
