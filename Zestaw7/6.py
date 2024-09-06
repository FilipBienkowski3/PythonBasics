# 6. Proszę napisać funkcję wstawiającą na koniec listy nowy element. Do
# funkcji należy przekazać wskazanie na pierwszy element listy oraz wstawianą
# wartość.
class Node:

  def __init__(self, val):
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



def dodaj(first, value):
  if first is None:
    return Node(value)

  p = first
  element = Node(value)

  while p.next is not None:
    p = p.next

  p.next = element
  element.next = None
  return first


tab = [1, 2, 3, 4, 5]
list = to_list(tab)
print_all(list)
print(".....")
print_all(dodaj(list, 2))
