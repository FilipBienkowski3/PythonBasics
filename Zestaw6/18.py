#Zadanie 18. W szachownicy o wymiarach 8x8 każdemu z pól przypisano liczbę naturalną. Na ruchy króla nałożono dwa ograniczenia: król może przesunąć się na jedno z 8 sąsiednich pól jeżeli ostatnia cyfra liczby na polu na którym stoi jest mniejsza od pierwszej cyfry liczby pola docelowego, oraz w drodze do obranego celu (np. narożnika) król nie może wykonać ruchu, który powoduje oddalenie go od celu. Dana jest globalna tablica T[8][8] wypełniona liczbami naturalnymi reprezentująca szachownicę. Lewy górny narożnik ma współrzędne w=0 i k=0. Proszę napisać funkcję sprawdzającą czy król może dostać się z pola w,k do prawego dolnego narożnika.
def is_on_board(x, y, n):
  return x < n and y < n


def can_move_to(from_x, from_y, x, y):
  return from_x <= x and from_y <= y


def get_first(n):
  while n // 10 > 0:
    n = n // 10
  return n % 10


def get_last(n):
  return n % 10


def can_get_to(x, y):
  if x == 7 and y == 7:
    return True

  for i, j in [(1, 1), (1, 0), (0, 1)]:
    if can_move_to(x, y, x + i, y + j) and is_on_board(x + i, y + j,8):
      return can_get_to(x + i, y + j)
  return False