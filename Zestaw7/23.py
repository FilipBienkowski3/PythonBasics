# 23. Dana jest lista, który zakończona jest cyklem.
# Napisać funkcję, która zwraca liczbę elementów w cyklu.
#counter od ich pierwszego spotkania do ich drugiego i to  bedzie dlugosc cyklu
#bezawrtownika
def cycleLength(pointer):
  counter = 0
  fast = pointer
  slow = pointer
  while (1):
    fast = fast.next.next
    slow = slow.next
    if fast == slow:
      break

  fast = fast.next.next
  slow = slow.next
  counter += 1
  while fast != slow:
    counter = +1
    fast = fast.next.next
    slow = slow.next
  return counter