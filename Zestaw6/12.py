#Zadanie 11. Dana jest tablica T[N]. Proszę napisać program zliczający liczbę “enek” o określonym iloczynie.
#Zadanie 12. Proszę zmodyfikować poprzedni program aby wypisywał znalezione n-ki.


def liczn(l, s, n, liczby, p=0):
  global licznik
  if n == 1:
    for i in range(p, len(l)):
      if l[i] == s:
        if l[i] not in liczby:
          liczby += [l[i]]
          licznik += 1
          print(liczby)
          return
  else:
    for i in range(p, len(l)):
      if s % l[i] == 0:
        if l[i] not in liczby:
          liczn(l, s // l[i], n - 1, liczby + [l[i]], i + 1)


t = [6, 2, 4, 2, 3,2]
licznik = 0
liczn(t, 24, 3, [])
print(licznik)