from __future__ import annotations
from abc import ABC, abstractmethod


class Strategy(ABC):
    @abstractmethod
    def execute(self):
        pass


class ConcreteStrategyBike(Strategy):
    def execute(self):
        print("i've chosen Bike")


class ConcreteStrategyPublicTransport(Strategy):
    def execute(self):
        print("i've chosen public transport")


class ConcreteStrategyTaxi(Strategy):
    def execute(self):
        print("i've chosen Taxi")


class Context():
    newStrategy = Strategy
    print("Insert amount of money: [zł]")
    money = input()
    print("Insert amount of time:[min]")
    time = input()

    def setStrategy(self, strategy: Strategy):
        self.newStrategy = strategy

    def getStrategy(self):
        return self.newStrategy

    def executeStrategy(self):
        return self.newStrategy.execute(self)


def choseStrategy(input):
    if (input == "1"):
        print("Bike, calculating:")
        if int(item.time) < 60:
            print("you don't have enough time for this transport")
        else:
            print("Chosen strategy is possible")
            item.setStrategy(ConcreteStrategyBike)
    elif (input == "2"):
        print("Public Transport,calculating")
        if int(item.money) < 3:
            print("you don't have enough money for this transport")
        if int(item.time) < 30:
            print("you don't have enough time for this transport")
        else:
            print("Chosen strategy is possible")
            item.setStrategy(ConcreteStrategyPublicTransport)
    elif (input == "3"):
        print("Taxi,calculating")
        if int(item.money) < 20:
            print("you don't have enough money for this transport")
        if int(item.time) < 15:
            print("you don't have enough time for this transport")
        else:
            print("Chosen strategy is possible")
            item.setStrategy(ConcreteStrategyTaxi)
    else:
        print("No strategy was chosen try again")


if __name__ == "__main__":
    print("Logic : ")
    item = Context()
    print("chose strategy: 1,2,3 (Bike / Public Transport / Taxi")
    strat = input()
    choseStrategy(strat)
    print("Chosen strategy will be executed if possible")
    item.executeStrategy()
