# 28. Dwie listy zawierają niepowtarzające się (w obrębie listy) liczby
# naturalne. W pierwszej liście liczby są posortowane rosnąco, a w drugiej
# nie. Proszę napisać funkcję usuwającą z obu list liczby występujące w obu
# listach. Do funkcji należy przekazać wskazania na obie listy, funkcja
# powinna zwrócić łączną liczbę usuniętych elementów.

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
        print(p.val, end=" -> ")
        p = p.next
    print("None")


def delate(first1, first2):
    dummy1 = Node(None)
    dummy1.next = first1
    dummy2 = Node(None)
    dummy2.next = first2

    curr2 = dummy2.next
    prev2 = dummy2
    cnt = 0

    while curr2 is not None:
        curr1 = dummy1.next
        prev1 = dummy1
        found = False
        while curr1 is not None:
            if curr1.val == curr2.val:
                cnt += 2
                print(f"Usuwanie: {curr1.val}")
                usun(prev1, curr1)
                usun(prev2, curr2)
                curr2 = prev2.next
                found = True
                break
            prev1 = curr1
            curr1 = curr1.next

        if not found:
            prev2 = curr2
            curr2 = curr2.next

    return cnt


def usun(prev, curr):
    prev.next = curr.next


tab1 = [1, 2, 3, 5, 8]
tab2 = [3, 1, 4, 6, 2]
list1 = to_list(tab1)
list2 = to_list(tab2)

print("Lista 1 przed usunięciem:")
print_all(list1)
print("Lista 2 przed usunięciem:")
print_all(list2)

print(".....")
usunięte_elementy = delate(list1, list2)

print(f"Liczba usuniętych elementów: {usunięte_elementy}")
