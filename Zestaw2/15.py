#Zadanie 15. Napisać program znajdujący wszystkie liczby N-cyfrowe dla których suma N-tych potęg cyfr liczby jest równa tej liczbie, np. 153 = 13 + 53 + 33

n = int(input("Podaj liczbe:"))
suma = 0
tmp = n
while n > 0:
  x = n % 10
  suma += (x**3)
  n //= 10
if tmp == suma:
  print(True)
else:
  print(False)
