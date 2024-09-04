#Zadanie 7. Dany jest zestaw odważników T[N]. Napisać funkcję,
#  która sprawdza czy jest możliwe odważenie określonej masy. 
# Odważniki można umieszczać tylko na jednej szalce.
def zadanie(T, i, r):
  n = len(T)
  if r == 0:
    return True
  if r < 0 or i > n - 1:
    return False
  return zadanie(T, i + 1, r) or zadanie(T, i + 1, r - T[i])


T = [1, 2, 3, 4, 5]
print(zadanie(T, 0, 23))
