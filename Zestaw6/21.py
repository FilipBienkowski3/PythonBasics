#Zadanie 21. Tablica T[8][8] zawiera liczby naturalne. Proszę napisać funkcję,
#  która sprawdza czy można wybrać z tablicy niepusty podzbiór o zadanej sumie.
#  Warunkiem dodatkowym jest aby żadne dwa wybrane elementy nie leżały w tej samej
#  kolumnie ani wierszu. Do funkcji należy przekazać wyłącznie tablicę oraz wartość
#  sumy, funkcja powinna zwrócić wartość typu bool.

def rek(arr, re, y=0, columns=[]):
  if re == 0:
    return True
  if re < 0 or y == len(arr):
    return False
  for x in range(len(arr)):
    if x not in columns:
      if rek(arr, re - arr[y][x], y + 1, columns + [x]):
        return True
  return False

arr = [
  [1, 4],
  [12, 1],
]
print(rek(arr, 5))