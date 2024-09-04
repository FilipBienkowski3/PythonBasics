#Zadanie 4. Dana jest tablica zawierająca liczby wymierne.
#  Proszę napisać funkcję, która policzy występujące w tablicy
#  ciągi arytmetyczne (LA) i geometryczne (LG) o długości większej
#  niż 2. Funkcja powinna zwrócić wartość 1 gdy LA > LG, wartość -1
#  gdy LA < LG oraz 0 gdy LA = LG.
def LAiLG(tab):
  if len(tab) <= 2:
    print("Za krótka tablica")
    return 0
  maxlenga = 2
  maxlengg = 2
  lenga = 2
  lengg = 2
  k = 1
  r = tab[k] - tab[k - 1]
  q = tab[k] / tab[k - 1]

  for i in range(2, len(tab)):
    if r == tab[i] - tab[i - 1]:
      lenga += 1
    else:
      r = tab[i] - tab[i - 1]
      maxlenga = max(maxlenga, lenga)
      lenga = 2
    if q == tab[i] / tab[i - 1]:
      lengg += 1
    else:
      q = tab[i] / tab[i - 1]
      maxlengg = max(maxlengg, lengg)
      lengg = 2
  maxlengg = max(maxlengg, lengg)
  maxlenga = max(maxlenga, lenga)
  if maxlenga > maxlengg:
    return 1
  if maxlenga < maxlengg:
    return -1
  else:
    return 0


tab = [1,2,5,25,125]
print(LAiLG(tab))
