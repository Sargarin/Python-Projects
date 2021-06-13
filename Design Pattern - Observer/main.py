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
    @abstractmethod
    def update(self, subject: Subject) -> None:
        pass


class ConcreteObserverA(Observer):
    def update(self, subject: Subject) -> None:
        if subject._state == 'a':
            print("ConcreteObserverA: Reacted to the event")


class ConcreteObserverB(Observer):
    def update(self, subject: Subject) -> None:
        if subject._state == 'b':
            print("ConcreteObserverB: Reacted to the event")


class ConcreteObserverC(Observer):
    def update(self, subject: Subject) -> None:
        if subject._state == 'c':
            print("ConcreteObserverC: Reacted to the event")


class ConcreteObserverD(Observer):
    def update(self, subject: Subject) -> None:
        if subject._state == 'd':
            print("ConcreteObserverD: Reacted to the event")


class ConcreteObserverE(Observer):
    def update(self, subject: Subject) -> None:
        if subject._state == 'e':
            print("ConcreteObserverE: Reacted to the event")


if __name__ == "__main__":

    keyBoard = keyBoardSingleton(None)
    subject = ConcreteSubject()

    observer_a = ConcreteObserverA()
    subject.attach(observer_a, 'a')

    observer_b = ConcreteObserverB()
    subject.attach(observer_b, 'b')

    observer_c = ConcreteObserverC()
    subject.attach(observer_c, 'c')

    observer_d = ConcreteObserverD()
    subject.attach(observer_d, 'd')

    observer_e = ConcreteObserverE()
    subject.attach(observer_e, 'e')
    # while(1) powstało w ramach testów
    while (1):
        keyBoard(subject.pressAKey())
