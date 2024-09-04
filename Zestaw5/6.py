#Zadanie 6. Liczby zespolone są reprezentowane przez krotkę (re, im).
#  Gdzie: re - część rzeczywista liczby,im - część urojona liczby.
#  Proszę napisać podstawowe operacje na liczbach zespolonych, m.in.
#  dodawanie,odejmowanie, mnożenie, dzielenie, potęgowanie, wypisywanie i wczytywanie.
import math

def input_complex():
    re = int(input("Część rzeczywista: "))
    im = int(input("Część urojona: "))
    return re, im

def output_complex(c):
    re, im = c
    if im < 0:
        return f"{re} - {-im}i"
    else:
        return f"{re} + {im}i"

def add_complex(c1, c2):
    return c1[0] + c2[0], c1[1] + c2[1]

def subtract_complex(c1, c2):
    return c1[0] - c2[0], c1[1] - c2[1]

def multiply_complex(c1, c2):
    re = c1[0] * c2[0] - c1[1] * c2[1]
    im = c1[0] * c2[1] + c1[1] * c2[0]
    return re, im

def divide_complex(c1, c2):
    denom = c2[0]**2 + c2[1]**2
    re = (c1[0] * c2[0] + c1[1] * c2[1]) / denom
    im = (c1[1] * c2[0] - c1[0] * c2[1]) / denom
    return re, im

def modulus(c):
    return math.sqrt(c[0]**2 + c[1]**2)

def argument(c):
    return math.atan2(c[1], c[0])


c1 = input_complex()
c2 = input_complex()

print(f"c1: {output_complex(c1)}")
print(f"c2: {output_complex(c2)}")

print(f"Dodawanie: {output_complex(add_complex(c1, c2))}")
print(f"Odejmowanie: {output_complex(subtract_complex(c1, c2))}")
print(f"Mnożenie: {output_complex(multiply_complex(c1, c2))}")
print(f"Dzielenie: {output_complex(divide_complex(c1, c2))}")

print(f"Moduł c1: {modulus(c1)}")
print(f"Kąt (w radianach) c1: {argument(c1)}")