#Zadanie 7. Napisać program wypełniający N-elementową tablicę t liczbami naturalnymi 1-1000 i sprawdzający czy istnieje element tablicy zawierający wyłącznie cyfry nieparzyste.
import random


def czy_wszystkie_cyfry_nieparzyste(i):
  while i > 0:
    if (i % 10) % 2 == 0:
      return False
      break
    i //= 10
  return True


n = int(input())
tablica = [random.randint(1, 1000) for i in range(n)]
print(tablica)
for i in tablica:
  if czy_wszystkie_cyfry_nieparzyste(i):
    print(True)
    break
else:
  print(False)