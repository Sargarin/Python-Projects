class memento:
    def __init__(self, file):
        self.file = file

class originator:
    def __init__(self, file):
        self.file = file

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

    def save(self):
        return memento(self.file)

    def undo(self, memento):
        self.file = memento.file

class caretaker:

    def save(self, origniator):

        self.obj = origniator.save()

    def undo(self, origniator):

        origniator.undo(self.obj)

