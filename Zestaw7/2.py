# 2. Zastosowanie listy odsyłaczowej do implementacji
# tablicy rzadkiej. Proszę napisać trzy funkcje:
# – inicjalizującą tablicę,
# – zwracającą wartość elementu o indeksie n,
# – podstawiającą wartość value pod indeks n.
class Node:
    def __init__(self, idx, val, next=None):
        self.idx = idx
        self.val = val
        self.next = next

def print_all(p):
    while p is not None:
        print(f"Index: {p.idx}, Value: {p.val}")
        p = p.next

def init_list(tab):
    head = None
    tail = None
    for val, idx in tab:
        new_node = Node(idx, val)
        if head is None:
            head = new_node
            tail = new_node
        else:
            tail.next = new_node
            tail = new_node
    return head

def search_value(idx, p):
    if p is None:
        return None
    if p.idx == idx:
        return p.val
    return search_value(idx, p.next)

def insert_value(idx, value, p):
    if p is None:
        return Node(idx, value)
    if p.idx == idx:
        p.val = value
    else:
        p.next = insert_value(idx, value, p.next)
    return p

def print_list(p):
    while p is not None:
        print(f"Index: {p.idx}, Value: {p.val}")
        p = p.next

tab = [(1, 2), (5, 0), (12, 15)]
list = init_list(tab)

print("Initial List:")
print_list(list)

print("\nSearch value at index 5:")
print(search_value(5, list))

print("\nInserting value at index 7:")
list = insert_value(7, 42, list)

print("\nUpdated List:")
print_list(list)