# 5. Proszę napisać funkcję, która rozdziela elementy listy odsyłaczowej do
# 10 list, według ostatniej cyfry pola val. W drugim kroku powstałe listy
# należy połączyć w jedną listę odsyłaczową, która jest posortowana
# niemalejąco według ostatniej cyfry pola val.
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def print_all(p):
    while p is not None:
        print(p.val, end=" -> ")
        p = p.next
    print("None")


def split(ll):
    curr = ll
    part = [Node(None) for _ in range(10)]
    lasts = [n for n in part]

    while curr is not None:
        nex = curr.next
        i = curr.val % 10
        lasts[i].next = curr
        lasts[i] = lasts[i].next
        lasts[i].next = None
        curr = nex

    res = Node(None)
    curr = res

    for i in range(10):
        if part[i].next:
            curr.next = part[i].next
            while curr.next:
                curr = curr.next

    return res.next


a = Node(3)
b = Node(14)
c = Node(24)
d = Node(35)
e = Node(18)
f = Node(46)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

print("Original list:")
print_all(a)

sorted_list = split(a)

print("\nList after split and merge:")
print_all(sorted_list)
