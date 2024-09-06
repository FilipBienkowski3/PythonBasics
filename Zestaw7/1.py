# 1. Zaimplementuj zbiór mnogościowy liczb naturalnych korzystając ze
# struktury listy odsyłaczowej.
# - czy element należy do zbioru
# - wstawienie elementu do zbioru
# - usunięcie elementu ze zbioru


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
def print_all_r(p):
  if p is not None:
    print(p.val)
    print_all(p.next)


#dodanie
def add(p, new_val):
  if p.next is None:
    q = Node(new_val)
    p.next = q
  if p.next is not None:
    if p.next.val == new_val:
      return
    elif p.next.val > new_val:
      q = Node(new_val)
      q.next = p.next
      p.next = q
    else:
      add(p.next, new_val)


#czy jest val
def is_present(g, val):
  if g.next is None:
    return False
  else:
    if g.next.val == val:
      return True
    elif g.next.val > val:
      return False
    else:
      return is_present(g.next, val)


#usuwanie
def delate(g, val):
  if g.next is None:
    return
  if g.next.val == val:
    g.next = g.next.next
  elif g.next.val < val:
    delate(g.next, val)


g = Node(0)

add(g, 2)
add(g, 2)
add(g, 1)
add(g, 9)
print_all(g)
print("-")
print_all(g.next)

print(is_present(g, 2))
print(is_present(g, 3))
print(is_present(g, 15))
delate(g, 2)
print_all(g.next)
########
