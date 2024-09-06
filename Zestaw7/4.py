# 4. Proszę napisać funkcję, która dla podanej listy odsyłaczowej odwraca
# kolejność jej elementów.
#zakładamy ze mamy niepusta liste
class Node:

  def __init__(self, val, next=None):
    self.val = val
    self.next = next


def print_all(p):
  while p is not None:
    print(p.val)
    p = p.next


#działanie odwracanie
# jeśli nasza lista składa sie tylko z jednego elementu to go zwróć,
# 2 w p.p odwróc liste zaczynajaca sie w nastepnym elemencie,
# 3 na koniec odwroc listy z kolejnego elementu doczep element aktualny
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


a = Node(2, None)
b = Node(1, a)
c = Node(3, b)
d = Node(7, c)
print_all(d)
x =reverse(d)
print_all(x)



  