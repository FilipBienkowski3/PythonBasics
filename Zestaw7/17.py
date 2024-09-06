# 17. Proszę napisać funkcję, która otrzymując jako parametr wskazujący na
# początek listy dwukierunkowej, usuwa z niej wszystkie elementy, w których
# wartość klucza w zapisie binarnym ma nieparzystą ilość jedynek.
#jak false to biezemy jak true to wurzucamy
#funkcja jesli zwroci false to ma zostac w liscie
class Node:

  def __init__(self, val=None, next=None):
    self.val = val
    self.next = next




def usunelem(first):
  guard = Node()
  guard.next = first
  while guard.next is not None:
    if nieparzysta_liczba_jedynek_w_binarnym(guard.next.val):
      guard.next = guard.next.next
    else:
      guard = guard.next
  return first.next


def nieparzysta_liczba_jedynek_w_binarnym(n):
  sum = 0
  while n > 0:
    if n % 2 != 0:
      sum += 1
    n = n // 2
  return sum % 2 != 0



def print_all(p):
  while p is not None:
    print(p.val)
    p = p.next



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


g = Node(0)

add(g, 21)  #true
add(g, 26)  #true
add(g, 27)  #false
add(g, 212)  #false


print_all(g.next)
print("-")

print_all(usunelem(g))
print("-")

