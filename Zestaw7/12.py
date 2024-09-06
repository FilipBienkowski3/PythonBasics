# 12. Zbiór mnogościowy zawierający napisy jest reprezentowany w postaci
# jednokierunkowej listy. Napisy w łańcuchu są uporządkowane
# leksykograficznie. Proszę napisać stosowne definicje typów oraz funkcję
# dodającą napis do zbioru. Do funkcji należy przekazać wskaźnik do listy
# oraz wstawiany napis, funkcja powinna zwrócić wartość logiczną wskazującą,
# czy w wyniku operacji moc zbioru uległa zmianie.
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
    if p is not None:
        print(p.val)
        print_all(p.next)


def insert(l, string):

    if l is None or l.val is None:
        new_node = Node(string)
        return new_node, True

    g = Node(None)
    g.next = l
    current = g

    while current.next is not None and current.next.val < string:
        current = current.next

    if current.next is not None and current.next.val == string:
        return g.next, False


    new_node = Node(string)
    new_node.next = current.next
    current.next = new_node
    return g.next, True


tab = ["aaba", "bbbb", "bbcccc", "cccc"]

list_of_strings = to_list(tab)

list_of_strings, changed = insert(list_of_strings, "bbbbaaaa")
print("Czy zbiór się zmienił:", changed)
print_all(list_of_strings)

list_of_strings, changed = insert(list_of_strings, "ccc")
print("Czy zbiór się zmienił:", changed)
print_all(list_of_strings)

list_of_strings, changed = insert(list_of_strings, "dccccccc")
print("Czy zbiór się zmienił:", changed)
print_all(list_of_strings)

list_of_strings, changed = insert(list_of_strings, "ac")
print("Czy zbiór się zmienił:", changed)
print_all(list_of_strings)

list_of_strings, changed = insert(list_of_strings, "a")
print("Czy zbiór się zmienił:", changed)
print_all(list_of_strings)