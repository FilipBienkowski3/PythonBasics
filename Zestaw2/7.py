#Zadanie 7. Napisz program wczytujący liczbę naturalną z klawiatury i odpowiadający na pytanie, czy liczba ta jest wielokrotnością dowolnego wyrazu ciągu danego wzorem An = n ∗ n + n + 1.
def ciag(n, liczba):
  A = n * n + n + 1
  return liczba % A == 0


liczba = int(input("podaj liczbe:"))
for i in range(1, liczba + 1):
  wynik = ciag(i, liczba)
  if wynik:
    print(liczba, "jesstwielokrotnoscia ciagu o n rownym", i)
    break
else:
  print("nie ma takiej liczby")
