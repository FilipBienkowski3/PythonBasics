#Zadanie 13. Liczby naturalne a,b są komplementarne jeżeli ich suma jest liczbą pierwszą. Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Proszę napisać funkcję, która zeruje elementy nie posiadające liczby komplementarnej.
import random


def pri(tab):
  for line in tab:
    print(line)


def sumatopierwsza(tab, sieve):
  for i in range(len(tab)):
    for j in range(len(tab)):
      flaga = False
      for k in range(len(tab)):
        for g in range(len(tab)):
          if (k != i and g != j):
            el = tab[i][j] + tab[k][g]
            if el in sieve:
              flaga = True
      if not flaga:
        tab[i][j] = 0

    return tab


m = 2
tab = [[random.randint(1, 100) for _ in range(m)] for _ in range(m)]
pri(tab)
n = 1000

sieve = [i for i in range(n)]
sieve[0] = False
sieve[1] = False

for i in range(2, n):
  if sieve[i] > 0:
    for j in range(2 * sieve[i], n, sieve[i]):
      sieve[j] = 0

pri(sumatopierwsza(tab, sieve))
