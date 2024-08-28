#Zadanie 9. Napisać program wypisujący podzielniki liczby
def printDivisors(num):
  if num == 0:
    print("każda liczba poza 0")
    return
  i = 1
  while i**2 < num:
    if num % i == 0:
      print(i)
      print(num // i)
      print(-i)
      print(-num // i)
    i += 1
  if i**2 == num:
    print(i)
    print(-i)


print(printDivisors(9))