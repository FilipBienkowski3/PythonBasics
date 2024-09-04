#Zadanie 11. Dwie liczby naturalne są „przyjaciółkami jeżeli zbiory 
# cyfr z których zbudowane są liczby są identyczne. Na przykład: 123
#  i 321, 211 i 122, 35 3553. Dana jest tablica T[N][N] wypełniona 
# liczbami naturalnymi. Proszę napisać funkcję, która dla tablicy T
#  zwraca ile elementów tablicy sąsiaduje wyłącznie z przyjaciółkami

def are_friends(num1, num2):
    return sorted(str(num1)) == sorted(str(num2))

def przyjaciolki(tab):
    n = len(tab)
    count = 0
    
    for i in range(n):
        for j in range(n):
            neighbors = []
            if i > 0:
                neighbors.append(tab[i-1][j])
            if i < n-1:
                neighbors.append(tab[i+1][j])
            if j > 0:
                neighbors.append(tab[i][j-1])
            if j < n-1:
                neighbors.append(tab[i][j+1])

            if all(are_friends(tab[i][j], neighbor) for neighbor in neighbors):
                count += 1
    
    return count

tab = [
    [12, 21, 22, 32],
    [12, 45, 89, 67],
    [12, 21, 22, 32],
    [322, 45, 89, 67]
]

print(przyjaciolki(tab)) 