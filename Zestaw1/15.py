#Zadanie 15. Nieskończony iloczyn sqrt(0.5) ∗ sqrt(0.5 + 0.5 ∗ sqrt(0.5)) ∗ sqrt(0.5 + 0.5 ∗ sqrt(0.5 + 0.5 ∗ sqrt(0.5))) ∗ ... ma wartość 2/π. Napisz program korzystający z tej zależności i wyznaczający wartość π.


from math import sqrt


def funkcja(a):
  i = 2
  suma_iloczynu = a
  while i < 50:
    c = sqrt(0.5 + 0.5 * a)
    suma_iloczynu = suma_iloczynu * c
    a = c
    i += 1
  return 2 / suma_iloczynu


q = sqrt(0.5)
print(funkcja(q))
