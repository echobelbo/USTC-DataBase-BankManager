import MySQLdb
from MySQLdb._exceptions import OperationalError


def db_login(user, passwd, server_addr, dbname):
    try:
        db = MySQLdb.connect(server_addr, user, passwd, dbname, charset="utf8")
    except OperationalError:
        db = None

    return db


def db_showtable(db):
    cursor = db.cursor()

    cursor.execute("show tables")
    tabs = cursor.fetchall()

    res = list()

    for tab in tabs:
        cursor.execute("select count(*) from " + tab[0])
        row_cnt = cursor.fetchone()

        res.append((tab[0], row_cnt[0]))

    cursor.close()

    return res


def db_search(db, table, conditions=''):
    cursor = db.cursor()
    print("select * from " + str(table) + ' ' + str(conditions))
    cursor.execute("select * from " + str(table) + ' ' + str(conditions))
    tabs = cursor.fetchall()
    return tabs


def db_close(db):
    if db is not None:
        db.close()


if __name__ == "__main__":
    db = db_login("lyp1234", "1234", "127.0.0.1", "test")

    tabs = db_showtable(db)

    db_close(db)
