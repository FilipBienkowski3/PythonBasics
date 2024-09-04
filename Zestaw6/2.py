
#Zadanie 2. ”Waga” liczby jest określona jako ilość różnych czynników pierwszych liczby. Na przykład waga(1)=0, waga(2)=1, waga(6)=2, waga(30)=3, waga(64)=1. Dana jest tablica T[N] zawierająca liczby naturalne. Proszę napisać funkcję, która sprawdza czy można elementy tablicy podzielić na 3 podzbiory o równych wagach. Do funkcji należy przekazać wyłącznie tablicę, funkcja powinna zwrócić wartość typu Bool.
def waga(n):
  suma = 0
  t = [0 for i in range(n + 1)]
  k = 2
  while n != 1:
    while n % k == 0:
      n //= k
      if t[k] == 0:
        suma += 1
        t[k] = k
    k += 1
  return suma


def zad2(T, n1=0, n2=0, n3=0, i=0):

  if i == len(T):
    if n1 == n2 and n2 == n3:
      return True
    else:
      return False
  num = T[i]
  suma = waga(num)
  return zad2(T, n1 + suma, n2, n3, i + 1) or zad2(T, n1, n2 + suma, n3, i + 1) or zad2(T, n1, n2, n3 + suma, i + 1)


T = [i for i in range(1, 7)]

print(zad2(T))
