#Zadanie 8. Pewnych liczb nie można przedstawić jako sumy elementów spójnych fragmentów ciągu Fibonacciego, np. 9,14,15,17,22. Proszę napisać program, który wczytuje liczbę naturalną n, wylicza i wypisuje następną taką liczbę większą od n. Można założyć, że 0 < n < 1000.
def find_the_smallest_unsumable(
    num):
  num += 1
  while True:
    f1, f2 = 1, 1
    fib_suma = 0
    while fib_suma < num:
      fib_suma += f1
      f1, f2 = f2, f1 + f2

    f1, f2 = 1, 1
    while fib_suma > num:
      fib_suma -= f1
      f1, f2 = f2, f1 + f2

    if fib_suma != num:
      return num
    num += 1


num = int(input())

print(find_the_smallest_unsumable(num))
