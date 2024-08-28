# Zadanie 8. Proszę napisać program sprawdzający czy zadana liczba jest pierwszą.

#1

from math import sqrt

a = int(input("podaj liczbe : "))
for i in range(2, a):
  if a % i == 0:
    print("naturalna")
    break
else:
  print("pierwsza")

#2


def is_priime(num):
  if num == 2 or num == 3:
    return True
  if num <= 1 or num % 2 == 0 or num % 3 == 0:
    return False

  for i in range(6, int(num**0.5) + 1, 6):
    if num % (i - 1) == 0 or num % (i + 1) == 0:
      return False
  return True


print(is_priime(31))


def is_prime(x):
  if x == 2 or x == 3:
    return True
  if x % 2 == 0 or x % 3 == 0 or x <= 1:
    return False
  i = 5
  while i < int(sqrt(x)) + 1:
    if x % i == 0:
      return False
    i += 2
    if x % i == 0:
      return False
    i += 4
  return True


print(is_prime(31))