#Zadanie 8. Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. 
# Proszę napisać funkcję, która w poszukuje w tablicy najdłuższego ciągu 
# geometrycznego leżącego ukośnie w kierunku prawo-dół, liczącego co najmniej 
# 3 elementy. Do funkcji należy przekazać tablicę. Funkcja powinna zwrócić 
# informacje czy udało się znaleźć taki ciąg oraz długość tego ciągu.
def ciaggeo(t1):
  n = len(t1)
  i, j = n - 1, 0
  max = 2
  while i >= 0:
    licznik = (n - 1) - (i + 1)
    tmpi = i
    j = 0
    if licznik > 0:
      q = t1[tmpi][j] / t1[tmpi + 1][j + 1]
    dlugosc = 2
    while licznik > 0:
      tmpi += 1
      j += 1
      if q == t1[tmpi][j] / t1[tmpi + 1][j + 1]:
        dlugosc += 1
        if dlugosc > max:
          max = dlugosc
      else:
        if dlugosc > max:
          max = dlugosc
        dlugosc = 2
        q = t1[tmpi][j] / t1[tmpi + 1][j + 1]
      licznik -= 1

    i -= 1
  j = 1
  while j != n:
    i = 0
    licznik = (n - 1) - (j + 1)
    tmpj = j
    if licznik > 0:
      q = t1[i][tmpj] / t1[i + 1][tmpj + 1]
    dlugosc = 2
    while licznik > 0:
      tmpj += 1
      i += 1
      if q == t1[i][tmpj] / t1[i + 1][tmpj + 1]:
        dlugosc += 1
        if dlugosc > max:
          max = dlugosc
      else:
        if dlugosc > max:
          max = dlugosc
        dlugosc = 2
        q = t1[tmpi][j] / t1[tmpi + 1][j + 1]
      licznik -= 1
    j += 1
  return max


t1 = [[1, 2, 4, 8, 1], 
      [1, 2, 2, 8, 16], 
      [1, 2, 2, 8, 1], 
      [1, 1, 1, 8, 16],
      [1, 2, 4, 8, 16]]

print(ciaggeo(t1))