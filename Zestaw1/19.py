#Zadanie 19. Napisać program wyznaczający wartość liczby e korzystając z zależności: e = 1/0! + 1/1! + 1/2! + 1/3! + ..
def calc(prec=50):
  fac = 1
  c = 0
  for i in range(1, prec):
    c += 1 / fac
    fac *= i
  return c


print(calc())
