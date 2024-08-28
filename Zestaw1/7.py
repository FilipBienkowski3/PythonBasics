#Zadanie 7. Napisz program wczytujący liczbę naturalną z klawiatury i odpowiadający na pytanie, czy liczba ta jest iloczynem dowolnych dwóch kolejnych wyrazów ciągu Fibonacciego.
def isFibProduct(num):
  a, b = 1, 1
  while a * b < num:
    a, b = b, a + b
  if a * b == num:
    return True
  else:
    return False


print(isFibProduct(int(input())))
