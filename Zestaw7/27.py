# 27. Proszę napisać funkcję scalającą dwie posortowane listy w jedną
# posortowaną listę. Do funkcji należy przekazać wskazania na pierwsze
# elementy obu list, funkcja powinna zwrócić wskazanie do scalonej listy.
# - funkcja iteracyjna,
# - funkcja rekurencyjna
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
    while p is not None:
        print(p.val, end=' -> ')
        p = p.next
    print("None")


def dodaj(first1, first2):
    dummy = Node()
    tail = dummy

    while first1 is not None and first2 is not None:
        if first1.val <= first2.val:
            tail.next = first1
            first1 = first1.next
        else:
            tail.next = first2
            first2 = first2.next
        tail = tail.next

    if first1 is not None:
        tail.next = first1
    else:
        tail.next = first2

    return dummy.next


tab1 = [1, 2, 4, 7, 8]
tab2 = [1, 2, 3, 5, 9]

list1 = to_list(tab1)
list2 = to_list(tab2)

print("Lista 1:")
print_all(list1)
print("Lista 2:")
print_all(list2)

merged_list = dodaj(list1, list2)

print("Scalona lista:")
print_all(merged_list)