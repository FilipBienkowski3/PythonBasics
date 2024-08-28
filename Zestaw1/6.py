#Zadanie 6. Proszę napisać program rozwiązujący równanie x ^x = 2020 metodą bisekcji

def f(x):
  return x**x - 2020


def solve(ep=0.0000001):
  C, D = 0, 100
  while abs(C - D) > ep:
    x = (C + D) / 2
    if f(x) == 0:
      return x
    if f(C) * f(x) < 0:
      D = x
    elif f(x) * f(D) < 0:
      C = x
  return (C + D) / 2


print(solve())
