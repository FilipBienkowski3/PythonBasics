#Zadanie 4. Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Proszę napisać funkcję, która
#zwraca wiersz i kolumnę dowolnego elementu, dla którego iloraz sumy elementów w kolumnie w którym leży
#element do sumy elementów wiersza w którym leży element jest największa.
import random


def print_tab(tab):
  for line in tab:
    print(line)


def najwiekszyiloczyn(tab):
  maxcolumna = 0
  maxwiersz = 0
  iloczyn = 1

  for i in range(len(tab)):
    for j in range(len(tab)):
      sumacolumna = 0
      sumawiersz = 0
      n = tab[i][j]
      for k in range(len(tab)):
        sumawiersz += tab[i][k]
      for g in range(len(tab)):
        sumacolumna += tab[g][j]
      if iloczyn < sumawiersz * sumacolumna:
        iloczyn = sumawiersz * sumacolumna
        tmp = n
        maxcolumna = j
        maxwiersz = i
  return (tmp, maxcolumna, maxwiersz)


n = 2
tab = [[random.randint(1, 50) for _ in range(n)] for _ in range(n)]
print_tab(tab)
print(najwiekszyiloczyn(tab))
