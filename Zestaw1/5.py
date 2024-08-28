#Zadanie 5. Proszę napisać program wyznaczający pierwiastek kwadratowy ze wzoru Newtona.
def newton_raphson(num, ep=1e-8):
  a, b = 1, num
  while abs(a - b) > ep:
    a = (a + b) / 2
    b = num / a
  return a


print(newton_raphson(16))
