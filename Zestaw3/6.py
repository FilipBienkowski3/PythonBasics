#Zadanie 6. Napisać program wypełniający N-elementową tablicę t liczbami naturalnymi 1-1000 i sprawdzający czy każdy element tablicy zawiera co najmniej jedną cyfrę nieparzystą.
import random


def jest_nieparzysty_element(i):
  while i > 0:
    if (i % 10) % 2 != 0:
      return True
    i //= 10
  return False


n = int(input())

rand_tab = [random.randint(1, 1000) for i in range(n)]
print(rand_tab)

for i in rand_tab:
  if not (jest_nieparzysty_element(i)):
    print(False)
    break
print(True)