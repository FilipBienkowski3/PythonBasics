# 13. Proszę napisać funkcję, otrzymującą jako parametr wskaźnik na pierwszy
# element listy o wartościach typu int, usuwającą wszystkie elementy, których
# wartość jest mniejsza od wartości bezpośrednio poprzedzających je
# elementów.
#zakladamy ze liste ktora przekazujemy nie ma wartownika
#15>2>14>7>none
class Node:

  def __init__(self, val, next=None):
    self.val = val
    self.next = next


def print_all(p):
  if p is not None:
    print(p.val)
    print_all(p.next)


def delate(p):
  if p.next is not None:
    delate(p.next)
    if p.next.val < p.val:
      p.next = p.next.next


a = Node(15)
b = Node(2)
c = Node(14)
d = Node(7)

a.next = b
b.next = c
c.next = d
print_all(a)
print("-")
delate(a)
print_all(a)
