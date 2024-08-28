#Zadanie 1. Proszę napisać program wypisujący elementy ciągu Fibonacciego mniejsze od miliona.
a = 0
b = 1
print(a)
while b <= 1000000:
  print(b)
  a, b = b, a + b
