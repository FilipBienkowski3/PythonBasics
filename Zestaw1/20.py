#Zadanie 20. Dane są ciągi: An+1 = √ An ∗ Bn oraz Bn+1 = (An + Bn)/2.0. Ciągi te są zbieżne do wspólnej granicy nazywanej średnią arytmetyczno-geometryczną. Napisać program wyznaczający średniąnarytmetyczno-geometryczną dwóch liczb.
from math import sqrt

def fun(a, b):
    eps = 10e-6
    while abs(a - b) > eps:
        a, b = sqrt(a * b), (a + b) / 2
    return (a + b) / 2

print(fun(4, 12))
