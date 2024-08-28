#Zadanie 18. Zmodyfikować wzór Newtona aby program z zadania 5 obliczał pierwiastek stopnia 3.
def newton_cube(num):
  a, c = 1, num
  while abs(c - a) > 1e-10:
    a = (a * 2 + c) / 3
    c = num / a / a
  return a


print(newton_cube(int(input())))
