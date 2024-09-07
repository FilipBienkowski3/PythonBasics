#zadanie 1 Napisać funkcję zamieniającą i wypisującą liczbę naturalną na system o podstawie 2-16.

import math
def zamiana_na_binarne(n, i):
  new_n = []
  chars = [int(i) for i in range(10) ] + [chr(i) for i in range(ord("A"), ord("F") + 1)]
  while n > 0:
    new_n.append(chars[n % i])
    n //= i
  new_n.reverse()
  return new_n


def leng(x):
  return math.floor(math.log10(x))+1
def zamiana_na_binarne2(n, pow=0):
  copy = n
  suma = 0
  while pow != leng(copy):
    suma += (n % 10) * 2**pow
    pow += 1
    n = n // 10
  return suma
print(zamiana_na_binarne(23,12))
print(zamiana_na_binarne2(10111))