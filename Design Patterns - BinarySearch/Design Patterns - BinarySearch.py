"""
Wyszukiwanie binarne rozwiązuje problem wyszukiwania liczby p w posortowanej, n-elementowej tablicy T poprzez śledzenie
przedziału wewnątrz tej tablicy, w którym jest (o ile w ogóle jest) poszukiwana wartość p. Początkowo, przedziałem jest
cała tablica. Przedział jest zmniejszany poprzez porównywanie elementu w jego środku z liczbą szukaną p, następnie odrzucenie
jego połowy – tej, w której nie ma szukanego elementu. Proces kończy się albo w momencie znalezienia p w tablicy T,
albo gdy przedział skurczy się do przedziału pustego.

Zaimplementować powyższy algorytm w postaci funkcji, przyjmującej jako argumenty tablicę T (o elementach całkowitych),
jej rozmiar n oraz szukaną liczbę p, a zwracającej albo pozycję liczby p w tablicy T (licząc od zera), albo –1, jeżeli liczby nie ma  w tablicy:

"""
import math


def binary_search(T, n, p):
    T.sort()
    rest = math.ceil(n/4)
    middle = math.ceil(n / 2)
    while (middle >= 0 and middle <= n):
        if (p == T[middle]):
            return middle
        elif (p > T[middle]):
            middle = math.ceil(middle + rest )
            rest = (n-middle)/2
        elif (p < T[middle]):
            if (middle != 1):
                middle = math.ceil(middle / 2)
            else:
                middle -= 1


T = [12, 0, 57, 36, 83, 24,72,99,768,55,54,53,52,51,50]

n = len(T)
p = 50

pozycja = binary_search(T, n, p)
print(pozycja)

