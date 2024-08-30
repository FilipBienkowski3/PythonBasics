#Zadanie 6. Napisać program wczytujący liczbę naturalną z klawiatury i rozkładający ją na iloczyn 2 liczb o najmniejszej różnicy. Np. 30 = 5 ∗ 6, 120 = 10 ∗ 12.
from math import sqrt

liczba = int(input("podaj liczbe:"))
maxi = int(sqrt(liczba))
tmp, x1, x2 = 10000, 0, 0
for i in range(1, maxi + 1):
  if liczba % i == 0:
    x = int(liczba / i)
    if abs(x - i) <= tmp:
      tmp = abs(x - i)
      x1 = x
      x2 = i
      print(x1, x2)
print("najmneijsza roznica to", tmp, "dla", x1, x2)
