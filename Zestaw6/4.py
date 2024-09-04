#Zadanie 4. Problem skoczka szachowego. Proszę napisać funkcję, która wypełnia pola szachownicy o ;wymiarach NxN ruchem skoczka szachowego.
def knights_walk(T, w=0, k=0, n=1):
  T[w][k] = n

  if n == len(T)**2:
    return True
  jumps = [(-2, 1), (-1, 2), (2, 1), (1, 2), (2, -1), (1, -2), (-1, -2),
           (-2, 1)]
  for jump in jumps:
    next_w = w + jump[0]
    next_k = k + jump[1]
    if contains(T, next_w, next_k) and T[next_w][next_k] == 0:
      if knights_walk(T, next_w, next_k, n + 1):
        return True
  T[w][k] = 0
  return False


def contains(T, w, k):
  if 0 <= w < len(T) and 0 <= k < len(T):
    return True
  return False


T2 = [[0 for i in range(6)] for i in range(6)]
print(knights_walk(T2))
for row in T2:
  print(row)
