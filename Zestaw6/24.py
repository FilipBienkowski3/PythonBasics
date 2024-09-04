# Zadanie 24. Tablica T = [(x1, y1),(x1, y1), ...] zawiera położenia N punktów o współrzędnych opisanych
# wartościami typu float. Proszę napisać funkcję, która zwróci najmniejszą odległość między środkami ciężkości
# 2 niepustych podzbiorów tego zbioru.
def srodek(T, i, mini):
  if i == len(T):
    return float('inf')
  for k in range(0, len(T)):
    for j in range(k + 1, len(T)):
      if k != i and j != i and j != k:
        tmp1 = ((abs(((T[i][0] + T[k][0]) / 2) - (T[i][0] + T[j][0]) / 2))**2 +
                (abs(((T[i][1] + T[k][1]) / 2) -
                     (T[i][1] + T[j][1]) / 2))**(2))**(0.5)

        if tmp1 < mini:
          mini = tmp1

  return min(mini, srodek(T, i + 1, mini))


T = [(1, 2), (3, 4), (5, 6)]
print(T[0][0])
print(srodek(T, 0, float('inf')))
