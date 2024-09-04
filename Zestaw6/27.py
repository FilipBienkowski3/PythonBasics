#Zadanie 27. Kwadrat jest opisywany czwórką liczb całkowitych (x1, x2, y1, y2),
#  gdzie x1, x2, y1, y2 oznaczają proste ograniczające kwadrat x1 < x2, y1 < y2.
#  Dana jest tablica T zawierająca opisy N kwadratów. Proszę napisać funkcję, 
# która zwraca wartość logiczną True, jeśli danej tablicy można znaleźć 13 nienachodzących na siebie kwadratów,
#  których suma pól jest równa 2012 i False w przeciwnym przypadku.
def not_cross(x1, x2, y1, y2, our_squares):
    for square in our_squares:
        sq_x1, sq_x2, sq_y1, sq_y2 = square
        if not (x2 <= sq_x1 or x1 >= sq_x2 or y2 <= sq_y1 or y1 >= sq_y2):
            return False
    return True


def area(x1, x2, y1, y2):
    return (x2 - x1) * (y2 - y1)


def zad27(T, index, current_area, to_find, already_chosen):
    if current_area == 2012 and to_find == 0:
        return True
    if index >= len(T) or to_find <= 0:
        return False

    x1, x2, y1, y2 = T[index]
    square_area = area(x1, x2, y1, y2)

    if zad27(T, index + 1, current_area, to_find, already_chosen):
        return True

    if not_cross(x1, x2, y1, y2, already_chosen):
        already_chosen.append((x1, x2, y1, y2))
        if zad27(T, index + 1, current_area + square_area, to_find - 1, already_chosen):
            return True
        already_chosen.pop()

    return False


T = [
    (1, 4, 1, 4),
    (5, 7, 1, 3),
    (8, 12, 5, 9),
]

already_chosen = []
print(zad27(T, 0, 0, 13, already_chosen))