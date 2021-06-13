"""
W celu wykonania zadania wybrałem framework python Injector,
wymagał on jedynie komendy: pip install injector oraz dodania modułu do IDE pycharm

Mimo obszernego researchu i zrozumienia idei DI oraz IOC nie byłem w stanie zrozumieć do końca w jaki sposób powinno zostać
to zastosowane w podanym zadaniu, może to przez to, że w pythonie nie ma zbyt wielu injection frameworków oraz tutoriali.
Poniższa implementacja to moja interpretacja mam nadzieje że pokaże przynajmniej logike aplikacji.



Notatka dla mnie odnośnie logiki DI:
Moduły wysokopoziomowe nie powinny zależeć od modułów niskopoziomowych. Wszystkie powinny zależeć od abstrakcji.
Abstrakcje nie powinny zależeć od szczegółów. To szczegóły powinny zależeć od abstrakcji.
"""
from injector import Module, provider, Injector, inject, singleton
import sqlite3
from PIL import Image



class RequestHandler:
    @inject
    def __init__(self, db: sqlite3.Connection):
        self._db = db

    def get(self):
        cursor = self._db.cursor()
        cursor.execute('SELECT * FROM Drzewa ORDER by id')
        return cursor.fetchall()

    def load(self):
        structure = handler.get()
        for i in range(len(structure)):
            print(f"\nID: {structure[i][0]}\n"
                  f"Nazwa drzewa: {structure[i][1]}\n"
                  f"Rok zasadzenia: {structure[i][2]}\n"
                  f"Nazwa obrazu drzewa: {structure[i][3]} (Obraz zostanie otwarty)\n"
                  f"Współrzędne GPS:\n{structure[i][4][0:11]}\n{structure[i][4][12:23]}")
            im = Image.open(structure[i][3])
            im.show()


class Configuration:
    def __init__(self, connectionString):
        self.connectionString = connectionString


def configureForTesting(binder):
    configuration = Configuration('baza.db')
    binder.bind(Configuration, to=configuration, scope=singleton)


class DatabaseModule(Module):
    @singleton
    @provider
    def provideSqliteConnection(self, configuration: Configuration) -> sqlite3.Connection:
        conn = sqlite3.connect(configuration.connectionString)
        cur = conn.cursor()
        cur.execute("DELETE FROM Drzewa ")
        cur.execute('INSERT OR REPLACE INTO Drzewa VALUES (NULL,"Dąb", "1997","dąb.jpg","014 17 25 N 015 18 35 W")')
        cur.execute('INSERT OR REPLACE INTO Drzewa VALUES (NULL,"klon", "1999","klon.jpg","016 22 25 N 023 20 21 W")')
        cur.execute('INSERT OR REPLACE INTO Drzewa VALUES (NULL,"sosna", "2001","sosna.jpg","013 21 33 N 001 22 35 W")')
        conn.commit()
        return conn



if __name__ == "__main__":
    injector = Injector([configureForTesting, DatabaseModule()])
    handler = injector.get(RequestHandler)
    structure =handler.get()
    t1 = injector.get(Configuration) is injector.get(Configuration)
    t2 = injector.get(sqlite3.Connection) is injector.get(sqlite3.Connection)
    print(t1, t2)
    structure = handler.load()
