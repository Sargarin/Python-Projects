import sqlite3
import Command
import Memento


def connect(name):
    try:
        conn = sqlite3.connect(name)
    except:
        print("Error")
        conn.close()
    else:
        print("Wykonano połączenie z bazą: ", name)
    return conn


if __name__ == "__main__":
    print("Wpisz nazwe bazy danych na której chcesz operować")
    name: str = input()

    conn = connect(name)
    invoker = Command.Invoker()
    receiver = Command.Receiver()

    caretaker = Memento.caretaker()
    originator = Memento.originator("baza.db")

    caretaker.save(originator)

    work = True
    while work == True:

        print(
            "Zacznijmy prace z bazą danych, co chcesz zrobić:"
            "\nA Utworzyć nową tabele"
            "\nB Umieścić rekordy w tabeli"
            "\nC Wypisać zawartośc tabeli"
            "\nD Usunąć rekord z tabeli"
            "\nE Usunąć tabele"
            "\nF Zakończyć prace nad tabelą"
            "\nG Cofnij ostatnio wykonane polecenie")

        fromKeayboard = input()

        if (fromKeayboard == 'A'):
            print("Podaj nazwe tabeli jaką chcesz utworzyć: ")
            tableName: str = input()
            print("Podaj nazwe wartości która ma być przypisywana w tabeli do ID: ")
            valueName: str = input()
            invoker.set_on_start(Command.SimpleCommand())
            invoker.set_on_finish(Command.ComplexCommand(receiver, conn, fromKeayboard, tableName, valueName))
            invoker.do_something_important()

        elif (fromKeayboard == 'B'):
            print("Podaj nazwe tabeli do której chcesz dodać dane: ")
            addDataToTableName = input()
            print("podaj liczbę ilości danych jakie chcesz umieścić: ")
            howMuchData: int = input()

            originator.putDataIntoTable(conn,howMuchData,addDataToTableName)

            """
            invoker.set_on_start(Command.SimpleCommand())
            invoker.set_on_finish(
                Command.ComplexCommand(receiver, conn, fromKeayboard, howMuchData=howMuchData,
                                       addDataToTableName=addDataToTableName))
            invoker.do_something_important()
            """
        elif (fromKeayboard == 'C'):
            print("Podaj nazwe tabeli do wyświetlenia: ")
            readTable = input()
            invoker.set_on_start(Command.SimpleCommand())
            invoker.set_on_finish(
                Command.ComplexCommand(receiver, conn, fromKeayboard, readTable=readTable))
            invoker.do_something_important()

        elif (fromKeayboard == 'D'):
            print("Podaj nazwe tabeli z której rekord chcesz usunąć: ")
            tableNameDeleteRecord = input()
            print("Podaj ID rekordu do usunięcia")
            rowToDelete = input()
            invoker.set_on_start(Command.SimpleCommand())
            invoker.set_on_finish(
                Command.ComplexCommand(receiver, conn, fromKeayboard, tableNameDeleteRecord=tableNameDeleteRecord,
                                       RowIDToDelete=rowToDelete))
            invoker.do_something_important()

        elif (fromKeayboard == 'E'):
            print("Podaj nazwe tabeli do usunięcia: ")
            tableToDelete = input()
            invoker.set_on_start(Command.SimpleCommand())
            invoker.set_on_finish(Command.ComplexCommand(receiver, conn, fromKeayboard, tableToDelete=tableToDelete))
            invoker.do_something_important()

        elif (fromKeayboard == 'F'):
            invoker.set_on_start(Command.SimpleCommand())
            invoker.set_on_finish(Command.ComplexCommand(receiver, conn, fromKeayboard))
            invoker.do_something_important()
            work = False

        elif (fromKeayboard == 'G'):
            Memento.caretaker.undo(caretaker, originator)

