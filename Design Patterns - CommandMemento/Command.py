from __future__ import annotations
from abc import ABC, abstractmethod
import sqlite3


class Command(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass


class SimpleCommand(Command):
    def execute(self) -> None:
        print("Pracuje nad bazą danych")


class ComplexCommand(Command):
    def __init__(self, receiver: Receiver, conn, fromKeyboard, NewtableName=None, valueName=None, howMuchData=None,
                 addDataToTableName=None, readTable=None, tableNameDeleteRecord=None, RowIDToDelete=None,tableToDelete=None) -> None:
        self._receiver = receiver
        self._conn = conn
        self._fromKeyboard = fromKeyboard
        self.NewtableName = NewtableName
        self._valueName = valueName
        self._howMuchData = howMuchData
        self._addDataToTableName = addDataToTableName
        self._readTable = readTable
        self._tableNameDeleteRecord = tableNameDeleteRecord
        self._RowIDToDelete = RowIDToDelete
        self._tableToDelete = tableToDelete

    def execute(self) -> None:
        if self._fromKeyboard == 'A':
            self._receiver.createTable(self._conn, self.NewtableName, self._valueName)
        elif self._fromKeyboard == 'B':
            self._receiver.putDataIntoTable(self._conn, self._howMuchData, self._addDataToTableName)
        elif self._fromKeyboard == 'C':
            self._receiver.printDataFromTable(self._conn, self._readTable)
        elif self._fromKeyboard == 'D':
            self._receiver.deleteRecord(self._conn, self._tableNameDeleteRecord, self._RowIDToDelete)
        elif self._fromKeyboard == 'E':
            self._receiver.deleteTable(self._conn,self._tableToDelete)
        elif self._fromKeyboard == 'F':
            self._receiver.closeDataBase(self._conn)


class Receiver:

    def createTable(self, conn, NewtableName, valueName) -> None:
        cur = conn.cursor()
        try:
            cur.execute(f"CREATE TABLE IF NOT EXISTS {NewtableName} (id INTEGER PRIMARY KEY, {valueName} STRING)")
        except:
            print("Error")
        else:
            print("utworzono tabele ", NewtableName)
            conn.commit()

    def putDataIntoTable(self, conn, howMuchData, addDataToTable) -> None:
        cur = conn.cursor()
        for i in range(0, int(howMuchData)):
            print("Podaj wartość: ")
            value = input()
            try:
                cur.execute(f"INSERT INTO {addDataToTable} VALUES(NULL,{value})")
            except:
                print("Error")
            else:
                print("rekord wstawiony poprawnie")
                conn.commit()

    def printDataFromTable(self, conn, tableName) -> None:
        cur = conn.cursor()
        print("pobieram dane z tabeli ", tableName)
        try:
            table = cur.execute(f"SELECT * FROM {tableName}")
        except:
            print("Error")
        else:
            for row in table:
                print(row)

    def closeDataBase(self, conn) -> None:
        print("Zamykam baze danych")
        conn.commit()
        conn.close()

    def deleteRecord(self, conn, tableNameDeleteRecord, RowIDToDelete) -> None:
        cur = conn.cursor()
        print(f"usuwam rekord {RowIDToDelete} z tabeli {tableNameDeleteRecord}")
        try:
            cur.execute(f"DELETE FROM {tableNameDeleteRecord} WHERE id = {RowIDToDelete}")
        except:
            print("Error")
        else:
            print("Rekord usunięty poprawnie")
            conn.commit()

    def deleteTable(self, conn, tableToDelete, ) -> None:
        cur = conn.cursor()
        print(f"usuwam tabele {tableToDelete}")
        try:
            cur.execute(f"DROP TABLE {tableToDelete};")
        except:
            print("Error")
        else:
            print("Tabela usunięta poprawnie")
            conn.commit()


class Invoker:
    _on_start = None
    _on_finish = None

    def set_on_start(self, command: Command):
        self._on_start = command

    def set_on_finish(self, command: Command):
        self._on_finish = command

    def do_something_important(self) -> None:

        if isinstance(self._on_start, Command):
            self._on_start.execute()

        if isinstance(self._on_finish, Command):
            self._on_finish.execute()
