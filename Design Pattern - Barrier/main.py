'''

Napisać program, w którym n osób zmierza jakąś komunikacją (losowy czas na dojazd) do restauracji.
Zamówienie można złożyć dopiero po przyjeździe wszystkich osób. Następuje konsumpcja (znów losowy czas) i odejście od stołu, gdy wszyscy skończą.

'''
import random
import time
import threading

# Przygotowanie bariery
n = 3
barrier = threading.Barrier(n)


# Zadanie wykonywane przez wątki
class Day:
    def wait(self, x):
        time.sleep(x)

    def begin(self):
        print("Ruszam")
        time = random.randrange(1, 10, 1)
        self.wait(time)
        print(f"Dotarłem do restauracji w {time} sekund\n")

    def eat(self):
        print("Zaczynam posiłek\n")
        time = random.randrange(1, 5, 1)
        self.wait(time)
        print(f"Skończyłem posiłek w {time} sekund\n")


class Thread(threading.Thread):
    def __init__(self, thread_ID):
        threading.Thread.__init__(self)
        self.thread_ID = thread_ID

    def run(self):
        day = Day()
        day.begin()
        barrier.wait()
        day.eat()
        barrier.wait()


if __name__ == "__main__":
    t1 = Thread(1)
    t2 = Thread(2)
    t3 = Thread(3)
    t1.start()
    t2.start()
    t3.start()
