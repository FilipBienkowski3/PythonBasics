# Zadanie 1. Dana jest tablica T[N][N]. Proszę napisać funkcję wypełniającą tablicę kolejnymi liczbami
# naturalnymi po spirali.
def print_tab(tab):
  for line in tab:
    print(line)


def spirala(count, tab, n):
  maxi = n**2
  x, y = 0, 0
  while count <= maxi:
    while x < n - 1 and tab[y][x + 1] == 0:
      tab[y][x] = count
      x += 1
      count += 1

    while y < n - 1 and tab[y + 1][x] == 0:
      tab[y][x] = count
      y += 1
      count += 1

    while x > 0 and tab[y][x - 1] == 0:
      tab[y][x] = count
      x -= 1
      count += 1
    while y > 0 and tab[y - 1][x] == 0:
      tab[y][x] = count
      y -= 1
      count += 1

    if count == maxi:
      tab[y][x] = count
      count += 1

  return tab


n = 5
count = 1
tab = [[0] * n for _ in range(n)]

print_tab(spirala(count, tab, n))