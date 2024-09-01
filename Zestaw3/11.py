#Zadanie 11. Napisać funkcję, która dla N-elementowej tablicy t wypełnionej liczbami naturalnym wyznacza długość najdłuższego, spójnego podciągu geometrycznego.


def leng_of_longest_geom_subsequence(tablica):
  if len(tablica) <= 2:
    return len(tablica)
  maxl = 2
  leng = 2
  q = tablica[1] / tablica[0]
  for i in range(2, len(tablica)):
    if q == tablica[i] / tablica[i - 1]:
      leng += 1
    else:
      if maxl < leng:
        maxl = leng
      leng = 2
      q = tablica[i] / tablica[i - 1]
  return max(maxl, leng)


tablica = tuple(map(int, input().split()))
print(tablica)
print(leng_of_longest_geom_subsequence(tablica))