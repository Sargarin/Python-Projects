import sqlite3
import DBgenCode, FillDbWithData
import Threads


def connect(name):
    try:
        conn = sqlite3.connect(name)
    except:
        print("Error")
        conn.close()
    else:
        print("Connection succesful: ", name)
    return conn


def createDB(conn):
    dbGen = DBgenCode.DbGenFunction()
    cur = conn.cursor()
    for e in dbGen:
        cur.execute(e)
    conn.commit()


if __name__ == "__main__":

    conn = connect("DB.db")
    createDB(conn)
    FillDbWithData.fillDbWithDataAndRepeat(conn)

    Threads.CreateThreads.case(20)

