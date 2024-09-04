#Zadanie 9. Poprzednie zadanie. Program powinien wypisywać wybrane odważniki.

def zadanie(T, i, r, W1, W2):
  n = len(T)
  if r == 0:
    print(W1, W2)
    return
  if i == n:
    return
  zadanie(T, i + 1, r, W1, W2)
  zadanie(T, i + 1, r - T[i], W1 + [T[i]], W2)
  zadanie(T, i + 1, r + T[i], W1, W2 + [T[i]])


T = [2, 15, 3, 14]
zadanie(T, 0, 12, [], [])
