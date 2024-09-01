#Zadanie 13. Proszę napisać program, który wypełnia N-elementową tablicę t trzycyfrowymi liczbami pseudolosowymi, a następnie wyznacza i wypisuje długość najdłuższego podciągu spójnego znajdującego się w tablicy dla którego w tablicy występuje również rewers tego ciągu. Na przykład dla tablicy: t= [2,9,3,1,7,11,9,6,7,7,1,3,9,12,15] odpowiedzią jest liczba 4.

tab = [2, 9, 3, 1, 7, 11, 9, 6, 7, 7, 1, 3, 9, 12, 15]
tab2 = tab[::-1]
print(tab2)
n = len(tab)
leng = 0
maxi = 1
for i in range(n):
  for j in range(n):
    while True:
      tmpi = i
      tmpj = j
      if tab[i] == tab2[j]:
        leng += 1
        if leng > maxi:
          maxi = leng
        i += 1
        j += 1
        if i == n or j == n:
          j = tmpj
          i = tmpi
          leng = 0
          break
      else:
        leng = 0
        j = tmpj
        i = tmpi
        break
print(maxi)