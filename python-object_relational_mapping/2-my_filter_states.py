#!/usr/bin/python3
""" Nameless module for running SQL """


if __name__ == "__main__":
    import MySQLdb
    import sys

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        password=sys.argv[2],
        database=sys.argv[3]
    )

    query = """SELECT * FROM states 
                WHERE `name` = '{0}' ORDER BY id ASC""".format(sys.argv[4])
    c = db.cursor()
    c.execute(query)
    rows = c.fetchall()

    for row in rows:
        print("({0}, '{1}')".format(row[0], row[1]))
