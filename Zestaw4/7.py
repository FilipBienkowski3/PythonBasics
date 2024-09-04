#Zadanie 7. Dane są dwie tablice mogące pomieścić taką samą liczbę elementów: T1[N][N] 
# i T2[M], gdzie M=N*N. W każdym wierszu tablicy T1 znajdują się uporządkowane niemalejąco
#  (w obrębie wiersza) liczby naturalne. Proszę napisać funkcję przepisującą wszystkie liczby
#  z tablicy T1 do T2, tak aby liczby w tablicy T2 były uporządkowane niemalejąco.
import random


def print_tab(tab):
  for line in tab:
    print(line)


def sortowanie(t1):
  for i in range(len(t1)):
    t1[i].sort()


def nw(t1, t2):
    count = 0
    min = 1000
    q, w = 0, 0
    while count!=len(t2):
      for k in range(len(t1)):
        for g in range(len(t1)):
          if min >= t1[k][g] and t1[k][g] > 0:
            min = t1[k][g]
            t2[count] = min
            q, w = k, g
      t1[q][w] = 0
      min = 1000
      count += 1
      q, w = 0, 0


n = int(input("podaj zakres:"))
t1 = [[random.randint(1, 1000) for _ in range(n)] for _ in range(n)]
t2 = [0 for _ in range(n * n)]

sortowanie(t1)
print_tab(t1)
nw(t1, t2)
print(t2)
