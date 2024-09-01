#Zadanie 9. Napisać funkcję, która dla N-elementowej tablicy t wypełnionej liczbami naturalnym wyznacza
#długość najdłuższego, spójnego podciągu rosnącego
import random


def sequ(tablica):
  if len(tablica) <= 1:
    return len(tablica)
  max = 1
  leng = 1
  for i in range(1, len(tablica)):
    if tablica[i - 1] < tablica[i]:
      leng += 1
    if leng > max:
      max = leng
      leng = 1
  return max


n = int(input())
tablica = [random.randint(1, 1000) for i in range(n)]
print(tablica)
print(sequ(tablica))
