#zadanie 1 Napisać funkcję zamieniającą i wypisującą liczbę naturalną na system o podstawie 2-16.


def zamiana_na_binarne(n, i):
  new_n = []
  chars = [int(i) for i in range(10) ] + [chr(i) for i in range(ord("A"), ord("F") + 1)]
  while n > 0:
    new_n.append(chars[n % i])
    n //= i
  new_n.reverse()
  return new_n


n = int(input("podaj liczbe:"))
for i in range(2, 16 + 1):
  print("base", i, ":", zamiana_na_binarne(n, i))