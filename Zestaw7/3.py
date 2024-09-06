# 3. Proszę napisać funkcję scalającą dwie posortowane listy w jedną
# posortowaną listę. Do funkcji należy przekazać wskazania na pierwsze
# elementy obu list, funkcja powinna zwrócić wskazanie do scalonej listy.
# - funkcja iteracyjna,
# - funkcja rekurencyjna.
class Node:

  def __init__(self, val, next=None):
    self.val = val
    self.next = next


#wypisanie iteracyjne
def print_all(p):
  while p is not None:
    print(p.val)
    p = p.next


#wypisanie rekurencyjne
# def print_all(p):
#   if p is not None:
#     print(p.val)
#     print_all(p.next)


#dodanie nawet powtorek
def add(p, new_val):
  if p.next is None:
    q = Node(new_val)
    p.next = q
  else:
    if p.next.val >= new_val:
      q = Node(new_val, p.next)
      p.next = q
    else:
      add(p.next, new_val)


#łączenie 2 list (scalanie)
def merge(p, q):
  if p is None:
    return q
  if q is None:
    return p
  if p.val <= q.val:
    p.next = merge(p.next, q)
    return p
  else:
    q.next = merge(p, q.next)
    return q


p = Node(None)
add(p, 3)
add(p, 3)
print_all(p)
print("-")
q = Node(None)
add(q, 1)
add(q, 3)
add(q, 20)
g = Node(None)
g.next = merge(p.next, q.next)
print_all(g.next)