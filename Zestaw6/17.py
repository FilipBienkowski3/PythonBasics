#Zadanie 17. Dane są dwie liczby naturalne z których budujemy 
# trzecią liczbę. W budowanej liczbie muszą wystąpić wszystkie
#  cyfry występujące w liczbach wejściowych. Wzajemna kolejność
#  cyfr każdej z liczb wejściowych musi być zachowana. Na przykład
#  mając liczby 123 i 75 możemy zbudować liczby 12375, 17523, 75123,
#  17253, itd. Proszę napisać funkcję która wyznaczy ile liczb pierwszych
#  można zbudować z dwóch zadanych liczb.
import math


def is_prime(num):
  if num < 2:
    return False
  if num == 2 or num == 3:
    return True
  if num % 2 == 0 or num % 3 == 0:
    return False

  for i in range(6, int(num**0.5) + 2, 6):
    if num % (i - 1) == 0 or num % (i + 1) == 0:
      return False

  return True


def rek(n1, n2, num=0, power=1):
  global primes
  if n1 == 0 and n2 == 0:
    print(num)
    if is_prime(num):
      primes += 1
    return
  if n1 > 0:
    rek(n1 // 10, n2, (n1 % 10) * power + num, power * 10)
  if n2 > 0:
    rek(n1, n2 // 10, (n2 % 10) * power + num, power * 10)


primes = 0
rek(32, 112)
print(primes)
