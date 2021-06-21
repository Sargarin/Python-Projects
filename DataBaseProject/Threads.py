import random
import time
import threading
import sqlite3

n = 2
barrier = threading.Barrier(n)


def connect(name):
    try:
        conn = sqlite3.connect(name)
    except:
        print("Error")
        conn.close()
    return conn


class dbTasks:
    def __init__(self, curr):
        self.curr = curr

    def findCurrentId(self, tableId, tableName):
        y = self.curr.execute(f"SELECT {tableId} FROM {tableName} ORDER BY {tableId} DESC LIMIT 1")
        for e in y:
            z = e[0]
        return z

    def deleteFromTable(self):
        x = random.randint(1, 6)
        if x == 1:
            tableName = "ammo_type"
            tableId = "ammo_type_id"
            z = self.findCurrentId(tableId, tableName)
            q = random.randint(1, z)
            self.curr.execute(f"DELETE FROM {tableName} WHERE {tableId} = {q}")

        if x == 2:
            tableName = "front_grips"
            tableId = "front_grips_id"
            z = self.findCurrentId(tableId, tableName)
            q = random.randint(1, z)
            self.curr.execute(f"DELETE FROM {tableName} WHERE {tableId} = {q}")

        if x == 3:
            tableName = "gun_category"
            tableId = "category_id"
            z = self.findCurrentId(tableId, tableName)
            q = random.randint(1, z)
            self.curr.execute(f"DELETE FROM {tableName} WHERE {tableId} = {q}")

        if x == 4:
            tableName = "guns"
            tableId = "gun_id"
            z = self.findCurrentId(tableId, tableName)
            q = random.randint(1, z)
            self.curr.execute(f"DELETE FROM {tableName} WHERE {tableId} = {q}")

        if x == 5:
            tableName = "muzzle_devices"
            tableId = "muzzle_id"
            z = self.findCurrentId(tableId, tableName)
            q = random.randint(1, z)
            self.curr.execute(f"DELETE FROM {tableName} WHERE {tableId} = {q}")

        if x == 6:
            tableName = "producent"
            tableId = "producent_id"
            z = self.findCurrentId(tableId, tableName)
            q = random.randint(1, z)
            self.curr.execute(f"DELETE FROM {tableName} WHERE {tableId} = {q}")

    def addToTable(self):
        x = random.randint(1, 6)
        if x == 1:
            tableName = "ammo_type"
            tableId = "ammo_type_id"
            colName = "ammo_type_type"
            data = 'testData'
            z = self.findCurrentId(tableId, tableName)
            self.curr.execute(f"INSERT OR REPLACE INTO {tableName}({tableId},{colName}) VALUES({z + 1},'{data}')")
        if x == 2:
            tableName = "front_grips"
            tableId = "front_grips_id"
            colName = "front_grips_name"
            data = 'testData'
            z = self.findCurrentId(tableId, tableName)
            self.curr.execute(f"INSERT OR REPLACE INTO {tableName}({tableId},{colName}) VALUES({z + 1},'{data}')")
        if x == 3:
            tableName = "gun_category"
            tableId = "category_id"
            colName = "category_name"
            data = 'testData'
            z = self.findCurrentId(tableId, tableName)
            self.curr.execute(f"INSERT OR REPLACE INTO {tableName}({tableId},{colName}) VALUES({z + 1},'{data}')")
        if x == 4:
            tableName = "guns"
            tableId = "gun_id"
            data = 'testData'
            colName1 = "gun_name"
            colName2 = "gun_category_category_id"
            colName3 = "producent_producent_id"
            colName4 = "ammo_type_ammo_type_id"
            z = self.findCurrentId(tableId, tableName)
            self.curr.execute(
                f"INSERT OR REPLACE INTO {tableName}({tableId},{colName1},{colName2},{colName3},{colName4}) VALUES({z + 1},'{data}','{data}','{data}','{data}')")
        if x == 5:
            tableName = "muzzle_devices"
            tableId = "muzzle_id"
            data = 'testData'
            colName = "muzzle_devices_name"
            z = self.findCurrentId(tableId, tableName)
            self.curr.execute(f"INSERT OR REPLACE INTO {tableName}({tableId},{colName}) VALUES({z + 1},'{data}')")
        if x == 6:
            tableName = "producent"
            tableId = "producent_id"
            data = 'testData'
            colName = "producent_country"
            z = self.findCurrentId(tableId, tableName)
            self.curr.execute(f"INSERT OR REPLACE INTO {tableName}({tableId},{colName}) VALUES({z + 1},'{data}')")

    def updateTable(self):
        x = random.randint(1, 6)
        if x == 1:
            tableName = "ammo_type"
            tableId = "ammo_type_id"
            colToUpdate = "ammo_type_type"
            data = "testData"
            z = self.findCurrentId(tableId, tableName)
            q = random.randint(1, z)
            self.curr.execute(f"UPDATE {tableName} SET {colToUpdate} = '{data}' WHERE {tableId} = {q};")

        if x == 2:
            tableName = "front_grips"
            tableId = "front_grips_id"
            colToUpdate = "front_grips_name"
            data = "testData"
            z = self.findCurrentId(tableId, tableName)
            q = random.randint(1, z)
            self.curr.execute(f"UPDATE {tableName} SET {colToUpdate} = '{data}' WHERE {tableId} = {q};")
        if x == 3:
            tableName = "gun_category"
            tableId = "category_id"
            colToUpdate = "category_name"
            data = "testData"
            z = self.findCurrentId(tableId, tableName)
            q = random.randint(1, z)
            self.curr.execute(f"UPDATE {tableName} SET {colToUpdate} = '{data}' WHERE {tableId} = {q};")
        if x == 4:
            tableName = "guns"
            tableId = "gun_id"
            colToUpdate = "gun_name"
            data = "testData"
            z = self.findCurrentId(tableId, tableName)
            q = random.randint(1, z)
            self.curr.execute(f"UPDATE {tableName} SET {colToUpdate} = '{data}' WHERE {tableId} = {q};")
        if x == 5:
            tableName = "muzzle_devices"
            tableId = "muzzle_id"
            colToUpdate = "muzzle_devices_name"
            data = "testData"
            z = self.findCurrentId(tableId, tableName)
            q = random.randint(1, z)
            self.curr.execute(f"UPDATE {tableName} SET {colToUpdate} = '{data}' WHERE {tableId} = {q};")
        if x == 6:
            tableName = "producent"
            tableId = "producent_id"
            colToUpdate = "producent_country"
            data = "testData"
            z = self.findCurrentId(tableId, tableName)
            q = random.randint(1, z)
            self.curr.execute(f"UPDATE {tableName} SET {colToUpdate} = '{data}' WHERE {tableId} = {q};")


class Tasks:

    def __init__(self, threadID, conn):
        self.threadID = threadID
        self.conn = conn
        self.curr = self.conn.cursor()
        self.dbTask = dbTasks(self.curr)

    def coffeBreak(self, x):
        time.sleep(x)

    def delete(self):
        print(f"Thread :{self.threadID} has started delete task\n")
        self.dbTask.deleteFromTable()
        self.conn.commit()

    def add(self):
        print(f"Thread :{self.threadID} has started add task\n")
        self.dbTask.addToTable()
        self.conn.commit()

    def update(self):
        print(f"Thread :{self.threadID} has started update task\n")
        self.dbTask.updateTable()
        self.conn.commit()

    def deleteWithCoffeBreak(self):
        print(f"Thread :{self.threadID} has started delete task with coffe break\n")
        x = random.randint(1, 2)
        self.dbTask.deleteFromTable()
        self.coffeBreak(x)
        self.conn.commit()

    def addWithCoffeBreak(self):
        print(f"Thread :{self.threadID} has started add task with coffe break\n")
        x = random.randint(1, 2)
        self.dbTask.addToTable()
        self.coffeBreak(x)
        self.conn.commit()

    def updateWithCoffeBreak(self):
        print(f"Thread :{self.threadID} has started update task with coffe break\n")
        x = random.randint(1, 2)
        self.dbTask.updateTable()
        self.coffeBreak(x)
        self.conn.commit()


class Thread(threading.Thread):
    def __init__(self, thread_ID):
        threading.Thread.__init__(self)
        self.thread_ID = thread_ID

    def run(self):
        try:
            conn = connect("DB.db")
        finally:
            print(f"Thread :{self.thread_ID} has been connected and will start work\n")

        task = Tasks(self.thread_ID, conn)
        randomTask = random.randint(1, 100)

        if randomTask <= 25:
            task.delete()

        if 25 < randomTask <= 50:
            task.add()

        if 50 < randomTask <= 75:
            task.update()

        if 75 < randomTask <= 83:
            task.deleteWithCoffeBreak()

        if 83 < randomTask <= 91:
            task.addWithCoffeBreak()

        if 91 < randomTask <= 100:
            task.updateWithCoffeBreak()


class CreateThreads(Thread):

    @staticmethod
    def case(n):
        threads = []
        for i in range(1, n+1):
            t = Thread(i)
            threads.append(t)
        for e in threads:
            e.start()
