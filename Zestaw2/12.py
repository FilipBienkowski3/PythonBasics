#Zadanie 12. Napisz program wczytujący liczbę naturalną z klawiatury i odpowiadający na pytanie, czy liczba ta zawiera cyfrę równą liczbie swoich cyfr.

import math

num = int(input())
leng = math.floor(math.log10(num)) + 1

while num > 0:
  if num % 10 == leng:
    print("jest")
    break
  num //= 10
else:
  print("nie ma")
