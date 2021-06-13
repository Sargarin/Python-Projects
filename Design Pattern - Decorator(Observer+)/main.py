from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class keyBoardSingleton:
    __instance = None

    def __new__(cls, pressedKey):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
        cls.__instance.pressedKey = pressedKey
        return cls.__instance

    def __call__(self, pressedKey, *args, **kwargs):
        print("pressed key:", pressedKey)


class Subject(ABC):
    def __init__(self):
        self._state = None

    @abstractmethod
    def attach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def notify(self) -> None:
        pass


class ConcreteSubject(Subject):
    _state: int = None
    _observers: List[Observer] = []

    def attach(self, observer: Observer, key) -> None:
        print("Subject: Attached an observer. with a key : ", key)
        self._observers.append(observer)
        observer.addKey(key)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify(self) -> None:
        print("Subject: Notifying observers...")
        for observer in self._observers:
            observer.update(self)

    def pressAKey(self) -> None:
        print("press a key to check observers")
        state = input()
        self._state = state
        print(f"Subject: My state has just changed to: {self._state}")
        self.notify()
        return state

class Observer(ABC):
    key = None

    @abstractmethod
    def update(self, subject: Subject) -> None:
        pass

    def addKey(self, key):
        self.key = key

def my_decorator(func):
    def wrapper_update(*args, **kwargs):
        value  = func(*args, **kwargs)
        if value =="a":
            return print("!")
        elif value =="b":
            return print("?")
        else:
            return value
    return wrapper_update

class ConcreteObserver(Observer):
    @my_decorator
    def update(self, subject: Subject) -> any:
        if subject._state == self.key:
            message: str = "ConcreteObserver: " + self.key + " Reacted to the event"
            print(message,end = '')
            return self.key

if __name__ == "__main__":
    keyBoard = keyBoardSingleton(None)
    subject = ConcreteSubject()

    observer_a = ConcreteObserver()
    subject.attach(observer_a, 'a')

    observer_b = ConcreteObserver()
    subject.attach(observer_b, 'b')

    observer_c = ConcreteObserver()
    subject.attach(observer_c, 'c')

    observer_d = ConcreteObserver()
    subject.attach(observer_d, 'd')

    observer_e = ConcreteObserver()
    subject.attach(observer_e, 'e')

# while(1) powstało w ramach testów
while (1):
    keyBoard(subject.pressAKey())
