# 31. Proszę napisać funkcję, która rozdziela listę na dwie listy. Pierwsza
# powinna zawierać klucze parzyste dodatnie, drugi klucze nieparzyste ujemne,
# pozostałe elementy należy usunąć z pamięci. Do funkcji należy przekazać
# wskaźniki na listę z danymi oraz wskaźniki na listy wynikowe. Funkcja
# powinna zwrócić liczbę usuniętych elementów.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


def print_all(p):
    while p is not None:
        print(p.val, end=" -> ")
        p = p.next
    print("None")


def create_from_list(L):
    g = Node(None)
    p = g
    for elem in L:
        p.next = Node(elem)
        p = p.next
    return g.next


def rozdziel(p, a, b):
    cnt = 0
    p = Node(None, p)

    a_tail = a
    b_tail = b

    while p.next is not None:
        q = p.next
        p.next = p.next.next

        if q.val % 2 == 0 and q.val > 0:
            a_tail.next = q
            a_tail = a_tail.next
        elif q.val % 2 == 1 and q.val < 0:
            b_tail.next = q
            b_tail = b_tail.next
        else:

            cnt += 1

    a_tail.next = None
    b_tail.next = None

    return cnt


p = create_from_list([7, 8, 6, -1, -2, 4, -3, 0])
a = Node(None)
b = Node(None)

liczba_usunietych = rozdziel(p, a, b)


print("Liczba usuniętych elementów:", liczba_usunietych)
print("Lista parzystych dodatnich (a):")
print_all(a.next)
print("Lista nieparzystych ujemnych (b):")
print_all(b.next)
