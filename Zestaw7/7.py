# 7. Proszę napisać funkcję usuwającą ostatni element listy. Do funkcji
# należy przekazać wskazanie na pierwszy element listy.


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


def remove_last(first):
  if first == None:
    return
  if first.next == None:
    return
  element_pierwszy = first
  while first.next.next is not None:
    first = first.next
  first.next = None
  return element_pierwszy


#guardian
def remove_last2(first):
  guard = Node()
  guard.next = first
  if first is None:
    return
  if first.next == None:
    guard.next = first.next
    return guard
  while guard.next.next is not None:
    guard = guard.next
  guard.next = None
  return first


tab = [1, 2]
list = to_list(tab)
print_all(list)
print(".....")
print_all(remove_last(list))
