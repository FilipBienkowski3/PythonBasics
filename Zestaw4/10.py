#Zadanie 10. Napisać funkcję która dla tablicy T[N][N], wypełnionej liczbami całkowitymi, zwraca wartość True w przypadku, gdy w każdym wierszu i każdej kolumnie występuje co najmniej jedno 0 oraz wartość False w przeciwnym przypadku.
import random


def pri(tab):
  for line in tab:
    print(line)


def wszedzie0(tab):
  for line in tab:
    is0 = False
    for element in line:
      if element == 0:
        is0 = True
        break
    if not is0:
      return False


#u gory 0 w ierszu na dole 0 w kolumnie
  for j in range(len(tab)):
    flaga = False
    for i in range(len(tab)):
      if tab[i][j] == 0:
        flaga = True
        break
    if not flaga:
      return False
  return True

n = int(input("podaj zakres:"))
tab = [[random.randint(0, 2) for _ in range(n)] for _ in range(n)]
pri(tab)
print(wszedzie0(tab))
