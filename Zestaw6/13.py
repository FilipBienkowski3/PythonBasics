#Zadanie 13. Napisać program wypisujący wszystkie możliwe podziały liczby naturalnej na sumę składników. Na przykład dla liczby 4 są to: 1+3, 1+1+2, 1+1+1+1, 2+2.

licznik = 0


def podzial(n, liczby):
  global licznik
  if n == 0:
    print(liczby)
    licznik += 1
  else:
    for i in range(n + 1, 0, -1):
      flaga = True
      for el in liczby:
        if el < i:
          flaga = False
      if flaga:
        podzial(n - i, liczby + [i])


podzial(6, [])
print(licznik)
