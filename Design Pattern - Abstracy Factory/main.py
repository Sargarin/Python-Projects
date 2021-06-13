import AbstractFactory
import Factory

"""
Napisać program z użyciem wzorca fabryka abstrakcyjna rozwiązujący poniższy problem.

Dane są 2 liczby całkowite: m, n, m<=n, m,n>=0 oraz zmienna logiczna sort. Wygenerować w optymalny sposób losowy, 
m-elementowy podciąg ciągu 1,2,3,...n, taki, aby żadna liczba w tym podciągu się nie powtarzała. Jeżeli sort ma wartość true, 
to ciąg wynikowy powinien być posortowany. Ciąg wynikowy zwrócić w tablicy.

Przykład: m=2, n=5, przykładowy wynik: 3,5

Problem można rozwiązać 3 algorytmami, ale ich liczba może się zmienić w przyszłości. Każdy z algorytmów lepiej nadaje 
się do konkretnego zestawu liczb m i n oraz zmiennej logicznej sort (samodzielnie określić, jaki algorytm najlepiej nadaje 
się do rozwiązania problemu dla danych wartości m, n, sort).
"""

if __name__ == "__main__":
    m = 2
    n = 5
    FactoryNotSorted = Factory.ConcreteFactoryNotSorted
    FactorySorted = Factory.ConcreteFactorySorted
    algA = FactoryNotSorted.createAlgorithmA(FactoryNotSorted)
    algB = FactorySorted.createAlgorithmB(FactorySorted)
    algC = FactoryNotSorted.createAlgorithmC(FactoryNotSorted)

    arrA1 = algA.function(m, n)
    print(arrA1)
    arrA2 = algA.function(m, n, sort=True)
    print(arrA1)
    arrB = algB.function(m, n)
    print(arrB)
    arrC1 = algC.function(m, n)
    print(arrC1)
    arrC2 = algC.function(m, n, sort=True)
    print(arrC2)
