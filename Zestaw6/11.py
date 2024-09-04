#Zadanie 11. Dana jest tablica T[N]. Proszę napisać program zliczający liczbę “enek” o określonym iloczynie.
def liczn(t, s, n, p=0):
  suma = 0
  if n == 1:
    for i in range(p, len(t)):
      if t[i] == s:
        return 1

  else:
    for i in range(p, len(t)):
      if s % t[i] == 0:
        suma+= liczn(t, s // t[i], n - 1, i + 1)
  return suma


t = [2, 2,2, 2,6,1]
print(liczn(t, 6, 2))