from __future__ import annotations
from abc import ABC
import time

class Handler(ABC):
    def setNext(self):
        pass

    def handle(self):
        pass


class algKwadratowyHandler(Handler):
    nextHandler = Handler

    def setNext(self, handler: Handler):
        self.nextHandler = handler
        return self.nextHandler

    def handle(self, request):
        if self.nextHandler != None:
            start = time.time()
            now = 0

            maxsofar = 0
            for i in range(0, len(vektor) - 1):
                now = time.time()
                sum = 0
                for j in range(i, len(vektor) - 1):
                    sum = sum + vektor[j]
                    maxsofar = max(maxsofar, sum)
                    #Jeżeli czas pracy przekroczy 1s przechodzimy do kolejnej metody
                    if (now - start > 1):
                        break
            print("Handler Kwadratowy, ukończył prace w czasie: ", now - start)
            print("wartość maksymalna podwektora: ", maxsofar)

            return self.nextHandler.handle(request)
        else:
            return None


class algLiniowyHandler(Handler):
    nextHandler = Handler

    def setNext(self, handler: Handler):
        self.nextHandler = handler
        return self.nextHandler

    def handle(self, request):
        if self.nextHandler != None:
            start = time.time()
            now = 0
            maxsofar = 0
            maxhere = 0
            for i in range(0, len(vektor) - 1):
                now = time.time()
                maxhere = max(maxhere + vektor[i], 0)
                maxsofar = max(maxsofar, maxhere)
            print("Handler Liniowy, ukończył prace  w czasie: ", now - start)
            print("wartość maksymalna podwektora: ", maxsofar)
            return self.nextHandler.handle(request)
        else:
            return None


if __name__ == "__main__":
    #wczytywany wektor : (-1000,1000,20000)
    vektor = []
    with open('vektor.txt', 'r') as f:
        string = f.read()
        new = [int(s) for s in string.split(',')]

    vektor = new
    h1 = algKwadratowyHandler()
    h2 = algLiniowyHandler()
    h1.setNext(h2)
    h1.handle(vektor)
