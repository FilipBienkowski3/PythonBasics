#Zadanie 18. Dana jest N-elementowa tablica t jest wypełniona liczbami naturalnymi. Proszę napisać
#funkcję, która zwraca długość najdłuższego spójnego podciągu będącego palindromem złożonym wyłącznie
#z liczb nieparzystych. Do funkcji należy przekazać tablicę, funkcja powinna zwrócić długość znalezionego
#podciągu lub wartość 0 jeżeli taki podciąg nie istnieje.

def is_palindrome(seq):
    return seq == seq[::-1]

def longest_odd_palindrome(t):
    n = len(t)
    max_length = 0
    
    for i in range(n):
        for j in range(i, n):
            sub_array = t[i:j+1]
            if all(x % 2 != 0 for x in sub_array):
                if is_palindrome(sub_array):
                    max_length = max(max_length, len(sub_array))
    
    return max_length

tablica = list(map(int, input().split()))
result = longest_odd_palindrome(tablica)
print(result)