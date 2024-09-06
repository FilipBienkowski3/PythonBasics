# 21. Kolejne elementy listy o zwiększającej się wartości pola val nazywamy
# podlistą rosnącą. Proszę napisać funkcję, która usuwa z listy wejściowej
# najdłuższą podlistę rosnącą. Warunkiem usunięcia jest istnienie w liście
# dokładnie jednej najdłuższej podlisty rosnącej.
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def remove_longest(root):
    preroot = Node(None)
    preroot.next = root

    len_longest = 0
    start_longest = None
    stop_longest = None

    start = preroot
    current_len = 1

    prev = root
    curr = root.next

    while curr is not None:
        if prev.val < curr.val:
            current_len += 1
        else:
            if current_len > len_longest:
                len_longest = current_len
                start_longest = start
                stop_longest = curr
            elif current_len == len_longest:
                len_longest = 0
                start_longest = None
                stop_longest = None

            current_len = 1
            start = prev

        prev = curr
        curr = curr.next

    if current_len > len_longest:
        len_longest = current_len
        start_longest = start
        stop_longest = curr
    elif current_len == len_longest:
        len_longest = 0
        start_longest = None
        stop_longest = None

    if len_longest > 1 and start_longest is not None:
        start_longest.next = stop_longest

    return len_longest if len_longest > 1 else 0


def to_list(tab):
    if len(tab) == 0:
        return None
    root = Node(tab[0])
    curr = root
    for i in range(1, len(tab)):
        curr.next = Node(tab[i])
        curr = curr.next
    return root

def print_list(root):
    while root is not None:
        print(root.val, end=' -> ')
        root = root.next
    print('None')


tab = [1, 2, 3, 1, 2, 3, 2]
list = to_list(tab)
print("Przed usunięciem najdłuższej rosnącej podlisty:")
print_list(list)
result = remove_longest(list)
print(f"Usunięto podlistę o długości: {result}")

