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

    state_name = sys.argv[4]

    query = """SELECT c.id, c.name, s.name
            FROM cities c
            INNER JOIN states s ON c.state_id = s.id
            WHERE BINARY s.name = '{0}'""".format(state_name)
    c = db.cursor()
    c.execute(query)
    rows = c.fetchall()

    i = 0
    for row in rows:
        print("{0}".format(row[1]), end="")
        i = i + 1
        if i != len(rows):
            print(", ", end="")
    print("")
