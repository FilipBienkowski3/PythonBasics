#Zadanie 1. Proszę napisać funkcję, która jako argument przyjmuje liczbę całkowitą
#  i wypisuje wszystkie co najmniej dwucyfrowe liczby pierwsze, powstałe poprzez wykreślenie z liczby pierwotnej co najmniej jednej cyfry.
#inne ich
def prime(n):
  if n < 2:
    return False
  for i in range(2, int(n**(0.5)) + 1):
    if n % i == 0:
      return False
  return True


def rek(n, result=0, pos=0):
  if n == 0:
    if result>9 and prime(result) :
      print(result)
    return
  rek(n // 10, result, pos)
  rek(n // 10, result + ((n % 10) * 10**pos), pos + 1)
print(rek(31134))

