#Zadanie 6. Dane są dwie tablice mogące pomieścić taką samą liczbę elementów: T1[N][N] i T2[M], 
# gdzie M=N*N. W każdym wierszu tablicy T1 znajdują się uporządkowane rosnąco (w obrębie wiersza) liczby naturalne. 
# Proszę napisać funkcję przepisującą wszystkie singletony (liczby występujące dokładnie raz) z tablicy T1 do T2, tak aby
#  liczby w tablicy T2 były uporządkowane rosnąco. Pozostałe elementy tablicy T2 powinny zawierać zera
import random


def print_tab(tab):
  for line in tab:
    print(line)


def sortowanie(t1):
  for i in range(len(t1)):
    t1[i].sort()


def sigletony(t1, t2):
  count = 0

  for i in range(len(t1)):
    for j in range(len(t1)):
      flaga = True
      for k in range(len(t1)):
        for g in range(len(t1)):
          if t1[i][j] == t1[k][g] and (k != i and g != j):
            flaga = False
      if flaga:
        t2[count] = t1[i][j]
        count += 1


n = int(input("podaj zakres:"))
t1 = [[random.randint(1, 1000) for _ in range(n)] for _ in range(n)]
t2 = [0 for _ in range(n * n)]
print_tab(t1)
sortowanie(t1)
print_tab(t1)
sigletony(t1, t2)
print(sorted(t2))
