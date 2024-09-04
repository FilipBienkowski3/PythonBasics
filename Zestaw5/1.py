# #Zadanie 1. Liczby wymierne są reprezentowane przez krotkę (l,m).
#  Gdzie: l - liczba całkowita oznaczająca licznik, m - liczba naturalna 
# oznaczająca mianownik. Proszę napisać podstawowe operacje na ułamkach, 
# m.in. 1dodawanie, 2odejmowanie, 3mnożenie, 4dzielenie, 5potęgowanie, 6skracanie, 7wypisywanie i 8wczytywanie.



def add(a, b):
    ans = (a[0]*b[1] + a[1]*b[0], a[1]*b[1])
    return ans


def subtract(a, b):
    ans = (a[0]*b[1] - a[1]*b[0], a[1]*b[1])
    return ans


def mult(a, b):
    ans = (a[0] * b[0], a[1]*b[1])
    return ans


def div(a, b):
    ans = (a[0] * b[1], a[1]*b[0])
    return ans


def exp(a, b):
    ans = (a[0]**b[0])**(1/b[1]), (a[1]**b[0])**(1/b[1])
    return ans

def pr(a):
    print(a[0], "/", a[1], sep="")

krotka = ((1, 3), (1, 4))
print(add(krotka[0],krotka[1]))