#Zadanie 2. Proszę znaleźć wyrazy początkowe zamiast 1,1 o najmniejszej sumie, aby w ciągu analogicznym do ciągu Fibonacciego wystąpił wyraz równy numerowi bieżącego roku.
suma = 10000
best = (2022, 0)

for i in range(2023):
  y = 2022
  x = i
  while x > 0 and y > x:
    x, y = y - x, x
  if x + y < suma:
    suma = x + y
    best = (x, y)

print(suma, best)

a = 53
b = 4
while a < 10000:
  print(a)
  a, b = b, a + b
