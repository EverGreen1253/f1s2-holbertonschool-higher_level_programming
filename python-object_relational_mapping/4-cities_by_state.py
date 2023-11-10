#!/usr/bin/python3
""" Nameless module for running SQL """


if __name__ == "__main__":
    import MySQLdb
    import sys

    for av in sys.argv:
        if av.count(";") > 0:
            exit()

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        password=sys.argv[2],
        database=sys.argv[3]
    )

    query = """SELECT c.id, c.name, s.name
            FROM cities c
            INNER JOIN states s ON c.state_id = s.id"""
    c = db.cursor()
    c.execute(query)
    rows = c.fetchall()

    for row in rows:
        print("({0}, '{1}')".format(row[0], row[1]))
