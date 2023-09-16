#!/usr/bin/python3
"""a script that lists all states from the database hbtn_0e_0_usa:"""


import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <mysql_username> <mysql_password>
                <database_name>")
        sys.exit(1)

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    try:
        db = MySQLdb.connect(host="localhost", port=3306, user=mysql_username,
                passwd=mysql_password, db=database_name)
        cursor = db.cursor()

        cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id")

        states = cursor.fetchall()
        for state in states:
            print(state)

        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print("MySQL Error:", e)
        sys.exit(1)
