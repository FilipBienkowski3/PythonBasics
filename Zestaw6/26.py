#Zadanie 26. Do budowy liczby naturalnej reprezentowanej w systemie dwójkowym możemy użyć A cyfr1 oraz B cyfr 0, gdzie A, B > 0. Proszę napisać funkcję, która dla zadanych parametrów A i B zwraca ilośćwszystkich możliwych do zbudowania liczb, takich że pierwsza cyfra w systemie dwójkowym (najstarszybit) jest równa 1, a zbudowana liczba jest złożona. Na przykład dla A=2, B=3 ilość liczb wynosi 3, są to10010(2), 10100(2), 11000(2)
import math


def leng(n):
  return math.floor(math.log10(n)) + 1


def zamiana_na_binarne(n, pow=0):
  copy = n
  suma = 0
  while pow != leng(copy):
    suma += (n % 10) * 2**pow
    pow += 1
    n = n // 10
  return suma


def is_prime(x):
  if x == 2 or x == 3:
    return True
  if x % 2 == 0 or x % 3 == 0 or x <= 1:
    return False
  i = 5
  while i < int(math.sqrt(x)) + 1:
    if x % i == 0:
      return False
    i += 2
    if x % i == 0:
      return False
  return True


def rek(A, B, x=0):
  if A == 0 and B == 0:
    if is_prime(zamiana_na_binarne(x)):
      return 1
    else:
      return 0
  a = 0
  b = 0
  if A > 0:
    a = rek(A - 1, B, x + 1 * 2**(A + B - 1))
  if B > 0:
    b = rek(A, B - 1, x + 0 * 2**(A + B - 1))
  return a + b


print(rek(2, 3))