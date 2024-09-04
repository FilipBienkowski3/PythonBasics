#petla problem
#Zadanie 18. W szachownicy o wymiarach 8x8 każdemu z pól przypisano liczbę naturalną. Na ruchy króla nałożono dwa ograniczenia: król może przesunąć się na jedno z 8 sąsiednich pól jeżeli ostatnia cyfra liczby na polu na którym stoi jest mniejsza od pierwszej cyfry liczby pola docelowego, oraz w drodze do obranego celu (np. narożnika) król nie może wykonać ruchu, który powoduje oddalenie go od celu. Dana jest globalna tablica T[8][8] wypełniona liczbami naturalnymi reprezentująca szachownicę. Lewy górny narożnik ma współrzędne w=0 i k=0. Proszę napisać funkcję sprawdzającą czy król może dostać się z pola w,k do prawego dolnego narożnika.
#Zadanie 19. Zadanie jak powyżej. Funkcja sprawdzająca czy król może dostać się z pola w,k do któregokolwiek z narożników.
#idzie tylko jedna strona
#Zadanie 20. Zadanie jak powyżej. Funkcja powinna dostarczyć drogę króla w postaci tablicy zawierającej kierunki (liczby od 0 do 7) poszczególnych ruchów króla do wybranego celu.

import random
import copy

T = [[random.randint(1, 1000) for _ in range(8)] for _ in range(8)]
t = [[0] * 8 for i in range(8)]


def is_on_board(x, y, n):
  return x < n and y < n


def can_move_to(from_x, from_y, x, y):
  global T
  return from_x <= x and from_y <= y and get_last(
    T[from_y][from_x]) < get_first(T[y][x])


def get_first(n):
  while n // 10 > 0:
    n = n // 10
  return n % 10


def get_last(n):
  return n % 10


def can_get_to(x, y, kroki):
  krok = copy.deepcopy(kroki)
  if (x == 7 and y == 7) or (x == 7 and y == 0) or (x == 0 and y == 7):
    print(krok)
    return True

  for i, j in [(1, 1), (0, 1), (1, 0)]:
    if is_on_board(x + i, y + j, 8) and can_move_to(x, y, x + i, y + j):
      if can_get_to(x + i, y + j, krok + (x + i, y + j)): #TUNIERETURN
        return True
  return False
stop=False
def pri(t):
  for line in t:
    print(line)


T[0][0] = 11
T[0][1] = 22
T[1][1] = 33
for i in range(0, len(T)):
  for j in range(0, len(T)):
    T[j][i] = j + 10 * j + 11 + 11
T[5][5] = 11

pri(T)
kroki = (0, 0)
can_get_to(0, 0, kroki)
