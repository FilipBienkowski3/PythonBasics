# 24. Dana jest lista, który zakończona jest cyklem.
# Napisać funkcję, która zwraca liczbę elementów przed cyklem.
#zaczynamy z szybkim i wolnym jak sie spotkaniaja to szybki idzie na poczatek(teraz bedzie sie poruszal jak wolny) a ten stary wolny idzie sobie dalej liczimy kroki nowego i starego wolnego jak sie spotkaja to bedzie dlugosc [rzed ] cyklem
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