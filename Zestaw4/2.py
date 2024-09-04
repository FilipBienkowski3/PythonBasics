#Zadanie 2. Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Proszę napisać funkcję, #która
#odpowiada na pytanie, czy w każdym wierszu tablicy występuje co najmniej jedna liczba złożona wyłącznie
#z nieparzystych cyfr.
def pri(tab):
  for i in tab:
    print(i)


def nieparzystajedna(tab):
  for i in range(len(tab)):
    flaga = False
    for j in range(len(tab)):
      n = tab[i][j]
      suma = 0
      while n > 0:
        if (n % 10) % 2 != 0:
          suma += 1
        n //= 10
      if suma == len(str(tab[i][j])):
        flaga = True
        continue
    if not flaga:
      return False
  return True


n = 3
tab = [[0 for i in range(n)] for i in range(n)]
count = 1
for i in range(len(tab)):
  for j in range(len(tab)):
    tab[i][j] = count
    count += 1
pri(tab)
print(nieparzystajedna(tab))
