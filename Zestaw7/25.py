# 25. Dana jest lista, który zakończona jest cyklem. Napisać funkcję, która
# zwraca wskaźnik do ostatniego elementu przed cyklem.
def beforeCycleLength(pointer):
  fast = pointer
  slow = pointer
  while 1:
    fast = fast.next.next
    slow = slow.next
    if fast == slow:
      break
  counter = 0
  fast = pointer
  while fast != slow:
    fast = fast.next
    slow = slow.next
    counter += 1
  return counter


def getFirstBC(pointer):
  l = beforeCycleLength(pointer)
  l = l - 1
  if l < 0:
    return None
  temp = pointer
  while l > 0:
    l = l - 1
    temp = temp.next
  return temp
