# 9. Dana jest niepusta lista reprezentująca liczbę naturalną. Kolejne
# elementy listy przechowują kolejne cyfry. Proszę napisać funkcję
# zwiększającą taką liczbę o 1.


class Node:

  def __init__(self, val=None):
    self.val = val
    self.next = None


def reverse(p):
  if p.next is None:
    return p
  else:
    prev = reverse(p.next)
    q = prev
    while q.next != None:
      q = q.next
    q.next = p
    p.next = None
    return prev


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


def add1(first):
  guardian = Node()
  guardian.next = first
  first = guardian
  if guardian.next.val != 9:
    guardian.next.val += 1
    return reverse(first.next)
  while guardian.next is not None and guardian.next.val == 9:
    guardian.next.val = 0
    guardian = guardian.next
  if guardian.next is None:
    last = Node(1)
    guardian.next = last
    last.next = None
  else:
    guardian.next.val += 1
  return reverse(first.next)


tab = [3, 9]
list = to_list(tab)
print_all(list)
print(".....")
print_all(add1((reverse(list))))
