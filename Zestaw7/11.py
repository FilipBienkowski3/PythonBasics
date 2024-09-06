# 11. Lista zawiera niepowtarzające się elementy. Proszę napisać funkcję do
# której przekazujemy wskaźnik na początek oraz wartość klucza. Jeżeli
# element o takim kluczu występuje w liście należy go usunąć z listy. Jeżeli
# elementu o zadanym kluczu brak w liście należy element o takim kluczu
# wstawić do listy.



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




def delate_or_add(first, value):
  guardian = Node()
  guardian.next = first
  first = guardian

  while guardian.next is not None:
    if guardian.next.val == value:
      guardian.next = guardian.next.next
      return first.next

    guardian = guardian.next
  el = Node(value)
  guardian.next = el
  el.next = None
  return first.next


tab = [1, 2, 3]
list = to_list(tab)
#print_all(list)
print(".....")
print_all(delate_or_add(list, 1))
