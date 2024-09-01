#Zadanie 12. Proszę napisać program, który wypełnia N-elementową tablicę t pseudolosowymi liczbami
#nieparzystymi z zakresu [1..99], a następnie wyznacza i wypisuje różnicę pomiędzy długością najdłuższego
#znajdującego się w niej ciągu arytmetycznego o dodatniej różnicy, a długością najdłuższego ciągu arytmetycznego o ujemnej różnicy, przy założeniu, że kolejnymi wyrazami ciągu są elementy tablicy o kolejnych
#indeksach.
import random


def najdluzsze_r_dodatnie_i_ujemne(tablica):
  maxplus = 2
  maxminus = 2
  leng = 2
  r = tablica[1] - tablica[0]
  for i in range(2, len(tablica)):
    if r >= 0:
      if r == tablica[i] - tablica[i - 1]:
        leng += 1
      else:
        if maxplus < leng:
          maxplus = leng
        leng = 2
        r = tablica[i] - tablica[i - 1]
    elif r < 0:
      if r == tablica[i] - tablica[i - 1]:
        leng += 1
      else:
        if maxminus < leng:
          maxminus = leng
        leng = 2
        r = tablica[i] - tablica[i - 1]
  return max(maxplus, leng), max(maxminus, leng)


n = int(input())
tablica = [0 for i in range(n)]
for i in range(n):
  while True:
    x = random.randint(1, 100)
    if x % 2 != 0:
      tablica[i - 1] = x
      break
print(tablica)
print(najdluzsze_r_dodatnie_i_ujemne(tablica))