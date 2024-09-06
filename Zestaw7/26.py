# 26. Proszę napisać funkcję, która sprawdza czy jedna lista zawiera się w
# drugiej. Do funkcji należy przekazać wskazania na pierwsze elementy obu
# list, funkcja powinna zwrócić wartość logiczną.


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


def compare(head1, head2):
  guard1 = Node()
  guard2 = Node()
  guard1.next = head1
  guard2.next = head2
  while guard1.next is not None:
    p = guard1
    q = guard2
    while True:
      if q.next is None:
        return True
      if p.next is not None and p.next.val == q.next.val:
        p = p.next
        q = q.next
      else:
        break
    guard1 = guard1.next
  return False



tab1 = [5, 1, 2, 1, 2, 2, 3, 4]
tab2 = [1,2]
list1 = to_list(tab1)
list2 = to_list(tab2)

print_all(list1)
print(".....")
print_all(list2)
print(".....")
print(compare(list1, list2))
