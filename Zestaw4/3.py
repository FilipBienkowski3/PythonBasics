#Zadanie 3. Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Proszę napisać funkcję, która
#odpowiada na pytanie, czy istnieje wiersz w tablicy w którym każda z liczb zawiera przynajmniej jedna cyfrę
#parzystą.
import random


def pri(tab):
  for i in tab:
    print(i)


def jednacyfraparzysta(tab):
  for i in range(len(tab)):
    suma = 0
    for j in range(len(tab)):
      n = tab[i][j]
      while n > 0:
        if (n % 10) % 2 == 0:
          suma += 1
          break
        n //= 10
    if suma == len(tab):
      return True
  return False


n = 2
tab = [[random.randint(1, 10) for i in range(n)] for i in range(n)]
pri(tab)
print(jednacyfraparzysta(tab))
