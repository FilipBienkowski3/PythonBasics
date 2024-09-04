# Zadanie 32. Dana jest tablica T[N] zawierająca liczby naturalne. Proszę napisać funkcję, która odpowiada
# na pytanie, czy spośród (niekoniecznie wszystkich) elementów tablicy można utworzyć dwa podzbiory o
# jednakowej sumie elementów, tak aby suma mocy obu podzbiorów wynosiła k. Do funkcji należy przekazać
# wyłącznie tablicę T oraz liczbę naturalną k, funkcja powinna zwrócić wartość typu bool.
def rek(T, k, index=0, P1=0, P2=0, s1=0, s2=0):
  if index == len(T):
    if P1 + P2 == k and s1 > 0 and s2 > 0:
      return True
    return False
  else:
    if rek(T, k, index + 1, P1, P2, s1, s2):
      return True
    if rek(T, k, index + 1, P1 + T[index], P2, s1 + 1, s2):
      return True
    if rek(T, k, index + 1, P1, P2 + T[index], s1, s2 + 1):
      return True
  return False


T = [2, 3,2]
print(rek(T, 4))
