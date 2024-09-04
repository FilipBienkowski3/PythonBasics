# Zadanie 28. Dany jest zbiór N liczb naturalnych umieszczony w tablicy T[N]. Proszę napisać funkcję,
# która zwraca informację, czy jest możliwy podział zbioru N liczb na trzy podzbiory, tak aby w każdym
# podzbiorze, łączna liczba jedynek użyta do zapisu elementów tego podzbioru w systemie dwójkowym była
# jednakowa. Na przykład: [2, 3, 5, 7, 15] → true, bo podzbiory {2,7} {3,5} {15} wymagają użycia 4 jedynek,
# [5, 7, 15] → f alse, podział nie istnieje.
def zamiana_na_binarne(n, i=2):
  suma = 0
  new_n = []
  chars = [int(i) for i in range(10)
           ] + [chr(i) for i in range(ord("A"),
                                      ord("F") + 1)]
  while n > 0:
    new_n.append(chars[n % i])
    n //= i
  new_n.reverse()
  for el in new_n:
    if el == 1:
      suma += 1
  return suma


def rek(T, index=0, P1=0, P2=0, P3=0, s1=0, s2=0, s3=0):
  if index == len(T):
    if P1 == P2 == P3 and s1 > 0 and s2 > 0 and s3 > 0:
      return True
    return False
  else:
    if rek(T, index + 1, P1 + zamiana_na_binarne(T[index]), P2, P3, s1 + 1, s2,
           s3):
      return True
    if rek(T, index + 1, P1, P2 + zamiana_na_binarne(T[index]), P3, s1, s2 + 1,
           s3):
      return True
    if rek(T, index + 1, P1, P2, P3 + zamiana_na_binarne(T[index]), s1, s2,
           s3 + 1):
      return True

  return False


T = [5, 7, 15]
print(rek(T))
