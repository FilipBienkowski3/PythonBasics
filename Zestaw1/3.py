#Zadanie 3. Proszę napisać program sprawdzający czy istnieje spójny podciąg ciągu Fibonacciego o zadanej sumie.
num = int(input("Podaj liczbe: "))

f1, f2 = 1, 1
fib_suma = 0
while fib_suma < num:
  fib_suma += f1
  f1, f2 = f2, f1 + f2

f1, f2 = 1, 1
while fib_suma > num:
  fib_suma -= f1
  f1, f2 = f2, f1 + f2

print(fib_suma == num)
