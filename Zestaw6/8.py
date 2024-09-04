#Zadanie 8. Poprzednie zadanie, ale odważniki można umieszczać na obu szalkach.
def zadanie(T, i, r):
  n = len(T)
  if r == 0:
    return True
  if i == n:
    return False
  return zadanie(T, i + 1, r) or zadanie(T, i + 1, r - T[i]) or zadanie(
    T, i + 1, r + T[i])


T = [15, 3]
print(zadanie(T, 0, 12))
