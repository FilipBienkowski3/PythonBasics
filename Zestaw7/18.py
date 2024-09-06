# 18. Proszę napisać funkcję, która pozostawia w liście wyłącznie elementy
# unikalne. Do funkcji należy przekazać wskazanie na pierwszy element listy.
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


def usun_unikalne(first):
  guardian = Node()
  guardian.next = first
  first = guardian
  p = guardian
  while p.next is not None:
    curr_val = p.next.val
    q = p.next
    while q.next is not None:
      if q.next.val == curr_val:
        q.next = q.next.next
      else:
        q = q.next
    p = p.next
  return guardian.next



def usun_unikalne2(first):
  guardian = Node()
  guardian.next = first
  first = guardian
  p = guardian
  while p.next is not None:
    Flaga = False
    curr_val = p.next.val
    q = p.next
    while q.next is not None:
      if q.next.val == curr_val:
        Flaga = True
        q.next = q.next.next
      else:
        q = q.next
    if Flaga:
      p.next = p.next.next
    else:
      p = p.next
  return guardian.next


tab = [1, 4, 3, 5, 3, 2, 3, 1]
list = to_list(tab)
print_all(list)
print(".....")
print_all(usun_unikalne2(list))
