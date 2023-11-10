#!/usr/bin/python3
""" Nameless module for running SQL """


if __name__ == "__main__":
    import MySQLdb

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user="root",
        password="",
        database="hbtn_0e_0_usa"
    )

    c = db.cursor()
    c.execute("""SELECT * FROM states""")
    rows = c.fetchall()

    for row in rows:
        print("({0}, {1})".format(row[0], row[1]))

        # print("(%s, " % row[0], end = "")
        # print("%s)" % row[1])
