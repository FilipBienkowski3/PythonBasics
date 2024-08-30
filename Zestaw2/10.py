#Zadanie 10. Napisz program wczytujący liczbę naturalną z klawiatury i odpowiadający na pytanie, czy liczba ta jest wielokrotnością dowolnego wyrazu ciągu danego wzorem An = 3 ∗ An−1 + 1, a pierwszy wyraz jest równy 2.
A = 2
n = int(input("podaj liczbe: "))
if n % A == 0:
  print("jest wieloktotnoscią", A, "jest to 1 wyraz ciagu")

i = 2
falsz = False
while i < 1000:
  A = A * 3 + 1
  if n % A == 0:
    print("jest wieloktotnoscią", A, "jest to ", i, "wyraz ciagu")
    falsz = True
    break
  else:
    i += 1
if not falsz:
  print("NIE JEST WIELOKTORNOSCIA ZADNEGO ELEMENTU CIAGU")
