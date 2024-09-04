#Zadanie 10. Rekurencyjne obliczanie wyznacznika z macierzy (treść oczywista)

import random

def pri(T):
    for line in T:
        print(line)

def det(T, poziom, n, j=0):
    if j == n - 1:
        for i in range(n):
            if i not in poziom:
                return T[i][j]
    
    suma = 0
    for i in range(n):
        if i not in poziom:
            suma += T[i][j] * (-1)**(i + j) * det(T, poziom + [i], n, j + 1)
    
    return suma

n = 3
T = [[random.randint(1, 10) for _ in range(n)] for _ in range(n)]
T2 = [[3, 10, 10], [3, 10, 1], [2, 1, 4]]

print("Losowa macierz T:")
pri(T)
print("\nWyznacznik macierzy T:", det(T, [], n))

print("\nMacierz T2:")
pri(T2)

print("\nWyznacznik macierzy T2:", det(T2, [], n))