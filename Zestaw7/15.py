# 15. Proszę napisać funkcję, która otrzymując jako parametr wskazujący na
# początek listy jednokierunkowej, usuwa z niej wszystkie elementy, w których
# wartość klucza w zapisie trójkowym ma większą ilość jedynek niż dwójek.
class Node:

  def __init__(self, val=None):
    self.val = val
    self.next = None


def system_trójkowy(n):
  count_1 = 0
  count_2 = 0
  while n > 0:
    x = n % 3
    if x == 1:
      count_1 += 1
    if x == 2:
      count_2 += 1
    n = n // 3
  return count_1 > count_2


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


def trialne(first):
  guardian = Node()
  guardian.next = first
  pierwszy = guardian
  while guardian.next is not None and guardian.next.next is not None:
    if system_trójkowy(guardian.next.val):
      guardian.next = guardian.next.next
    else:
      guardian = guardian.next
  return pierwszy.next


def trialne2(first):
  guardian = Node()
  guardian.next = first
  prev = guardian
  curr = guardian.next
  while curr.next is not None:
    if system_trójkowy(curr.val):
      prev.next = curr.next
      curr = curr.next
    else:
      curr = curr.next
      prev = prev.next
  return guardian.next


tab = [12, 122, 214]
list = to_list(tab)
print_all(list)
print(".....")
print_all(trialne2(list))
