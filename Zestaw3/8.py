#Zadanie 8. Dana jest N-elementowa tablica t zawierająca liczby naturalne. W tablicy możemy przeskoczyć
#z pola o indeksie k o n pól w prawo jeżeli wartość n jest czynnikiem pierwszym liczby t[k]. Napisać funkcję
#sprawdzającą czy jest możliwe przejście z pierwszego pola tablicy na ostatnie pole.

import random
from math import sqrt

def is_prime(n):
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i <= sqrt(n):
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def rozklad(n):
    number_moves = []
    i = 2
    while n > 1:
        if n % i == 0:
            if is_prime(i):
                number_moves.append(i)
            n //= i
        else:
            i += 1
    return number_moves

def can_reach_end(tab):
    n = len(tab)
    visited = [False] * n
    queue = [0]

    while queue:
        pos = queue.pop(0)
        if pos == n - 1:
            return True
        if visited[pos]:
            continue

        visited[pos] = True


        for move in rozklad(tab[pos]):
            new_pos = pos + move
            if new_pos < n and not visited[new_pos]:
                queue.append(new_pos)

    return False

n = int(input("Podaj rozmiar tablicy: "))
tab = [random.randint(2, 20) for _ in range(n)]
print("Tablica:", tab)

if can_reach_end(tab):
    print("Można przejść z pierwszego pola na ostatnie.")
else:
    print("Nie można przejść z pierwszego pola na ostatnie.")