#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa
"""
from sys import argv
import MySQLdb

if __name__ = __main__:
    if len(argv) != 4:
        print('Usage: 0-select_states username password database')
        exit(-1)

    db = MySQLdb.connect('localhost', argv[1], argv[2], argv[3], port=3306)

    arrow = db.cursor()
    arrow.execute('SELECT * FROM states ORDER BY id ASC')
    states = arrow.fetchall()

    for state in states:
        print(state)
    db.close()
