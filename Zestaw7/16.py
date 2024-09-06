# 16. Proszę napisać funkcję, która otrzymując jako parametr wskazujący na
# początek listy jednokierunkowej, przenosi na początek listy te z nich,
# które mają parzystą ilość piątek w zapisie ósemkowym.
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


def system_osemkowy(n):
  count_5 = 0
  while n > 0:
    x = n % 8
    if x == 5:
      count_5 += 1
    n = n // 8
  return count_5 % 2 == 0


def na_poczatek(first):
  guardian = Node()
  guardian.next = first
  H2 = Node()
  r = H2
  q = guardian
  while q.next is not None:
    if system_osemkowy(q.next.val):
      r.next = q.next
      r = r.next
      q.next = q.next.next
      r.next = None
    else:
      q = q.next
  r.next = guardian.next
  return H2.next


tab = [35, 345, 631, 647, 327, 864]
list = to_list(tab)
print_all(list)
print(".....")
print_all(na_poczatek(list))
