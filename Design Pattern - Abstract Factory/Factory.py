from AbstractFactory import AbstractFactory, AbstractAlgorithm
import random


class ConcreteAlgorithmA(AbstractAlgorithm):

    def function(self, m, n, sort=False):
        arr = []
        if (sort == False):
            while len(arr) != m:
                appear = False
                generated = random.randrange(1, n)
                if len(arr) > 1:
                    for i in range(0, len(arr)):
                        if (generated == arr[i]):
                            appear = True
                            break
                    if appear == False:
                        arr.append(generated)
                else:
                    arr.append(generated)
            return arr
        else:
            arr = self.function(m, n, False)
            arr = sorted(arr)
            return arr


class ConcreteAlgorithmB(AbstractAlgorithm):

    def function(self, m, n):
        arr = []
        for i in range(0, n):
            prawd = m / n
            los = random.random()
            if los < prawd:
                arr.append(i)
                m = m - 1
            n = n - 1
        return arr


class ConcreteAlgorithmC(AbstractAlgorithm):

    def function(self, m, n, sort=False):
        arr = []
        if (sort == False):

            tempArr = []
            for i in range(0, n):
                tempArr.append(i)

            for i in range(0, m):
                generated = random.randrange(1, n)
                if (generated != tempArr[i]):
                    tempArr[i] = generated
            i = 0
            while len(arr) < m:
                if tempArr[i] not in arr:
                    arr.append(tempArr[i])
                    i = i + 1
                else:
                    i = i + 1
            return arr

        else:
            arr = self.function(m, n, False)
            arr = sorted(arr)
            return arr


class ConcreteFactorySorted(AbstractFactory):
    def createAlgorithmB(self) -> AbstractAlgorithm:
        return ConcreteAlgorithmB()


class ConcreteFactoryNotSorted(AbstractFactory):
    def createAlgorithmA(self) -> AbstractAlgorithm:
        return ConcreteAlgorithmA()

    def createAlgorithmC(self) -> AbstractAlgorithm:
        return ConcreteAlgorithmC()
