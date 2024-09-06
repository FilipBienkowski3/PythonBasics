# 8. Dana jest niepusta lista, proszę napisać funkcję usuwającą co drugi
# element listy. Do funkcji należy przekazać wskazanie na pierwszy element
# listy.


class Node:

  def __init__(self):
    self.val = None
    self.next = None


def usun(first):
  p = first
  while p != None and p.next != None:
    p.next = p.next.next
    p = p.next
  return first


#rekurencyjnie
def usunr(first):
  if first == None or first.next == None:
    return first
  p = first
  p.next = p.next.next
  usunr(p.next)
  return first
