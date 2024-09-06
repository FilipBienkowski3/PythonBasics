# 30. Dane są dwie niepuste listy, z których każda zawiera niepowtarzające
# się elementy. Elementy w pierwszej liście są uporządkowane rosnąco, w
# drugiej elementy występują w przypadkowej kolejności. Proszę napisać
# funkcję, która z dwóch takich list stworzy jedną, w której uporządkowane
# elementy będą stanowić sumę mnogościową elementów z list wejściowych.
# Do funkcji należy przekazać wskazania na obie listy, funkcja powinna
# zwrócić wskazanie na listę wynikową. Na przykład dla list:
# 2 -> 3 -> 5 ->7-> 11
# 8 -> 2 -> 7 -> 4
# powinna pozostać lista:
# 2 -> 3 -> 4 -> 5 ->7-> 8 -> 11
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



def sortuj(first1, first2):
  g1 = Node()
  g2 = Node()
  g1.next = first1
  g2.next = first2
  while g2.next is not None:
    val = g2.next.val
    g1 = first1
    while g1.next != None and g1.next.val < val:
      g1 = g1.next
    if g1.next == None:
      g1.next = Node(val)
    elif g1.next.val == val:
      Q = 5
    else:
      q = Node(val)
      q.next = g1.next
      g1.next = q
    g2 = g2.next
  return first1.next


tab1 = [2, 3, 5, 7, 11]
tab2 = [8, 2, 9,5, 7]
list1 = to_list(tab1)
list2 = to_list(tab2)

print_all(list1)
print(".....")
print_all(list2)
print(".....")
print_all(sortuj(list1, list2))
