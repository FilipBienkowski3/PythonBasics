# 14. Proszę napisać funkcję, otrzymującą jako parametr wskaźnik na pierwszy
# element listy o wartościach typu int, usuwającą wszystkie elementy, których
# wartość dzieli bez reszty wartość bezpośrednio następujących po nich
# elementów.


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


def solve(l):
  guardian = Node()
  guardian.next = l
  pierwszy = guardian
  while guardian.next != None and guardian.next.next != None:
    curr_val = guardian.next.val
    next_val = guardian.next.next.val
    if next_val % curr_val == 0:
      guardian.next = guardian.next.next
    else:
      guardian = guardian.next
  return pierwszy.next



def solve2(l):
  guardian = l
  pierwszy = guardian
  while guardian.next != None:
    curr_val = guardian.val
    next_val = guardian.next.val
    if next_val % curr_val == 0:
      guardian.next = guardian.next.next
      continue
    else:
      guardian = guardian.next
  return pierwszy


tab = [3, 6, 6, 5, 5, 10, 9]
list = to_list(tab)
print_all(list)
print(".....")

print_all(solve2(list))
