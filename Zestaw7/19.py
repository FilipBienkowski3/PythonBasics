# 19. Elementy w liście są uporządkowane według wartości klucza. Proszę
# napisać funkcję usuwającą z listy elementy o nieunikalnym kluczu. Do
# funkcji przekazujemy wskazanie na pierwszy element listy,
# funkcja powinna zwrócić liczbę usuniętych elementów.


class Node:

  def __init__(self, val=None):
    self.val = val
    self.next = None


def to_list(tab):
  g = Node(None)
  p = g

  for elem in tab:
    p.next = Node(elem)
    p = p.next

  return g.next


def print_all(p):
  if p is not None:
    print(p.val)
    print_all(p.next)




def usun(first):
  guard = Node()
  guard.next = first
  first = guard
  p = guard
  while p.next is not None:
    Flaga = False
    curr_val = p.next.val
    while p.next.next is not None and p.next.next.val == curr_val:
      p.next = p.next.next
      Flaga = True

    if Flaga:
      p.next = p.next.next
    else:
      p = p.next
  return guard.next


tab = [1, 1, 1, 2, 3, 4, 4]
list = to_list(tab)
print_all(list)
print(".....")
print_all(usun(list))