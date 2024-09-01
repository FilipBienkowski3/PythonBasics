#Zadanie 15. Dana jest duża tablica t. Proszę napisać funkcję, która zwraca informację czy w tablicy
#zachodzi następujący warunek: „wszystkie elementy, których indeks jest elementem ciągu Fibonacciego są
#liczbami złożonymi, a wśród pozostałych przynajmniej jedna jest liczbą pierwszą”
import math

def is_prime(num):
    if num <= 1:
        return False
    if num == 2 or num == 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False

    for div in range(5, int(math.sqrt(num)) + 1, 6):
        if num % div == 0 or num % (div + 2) == 0:
            return False

    return True

def fibonacci_indices(n):
    fib_indices = []
    a, b = 1, 1
    while a < n:
        fib_indices.append(a)
        a, b = b, a + b
    return fib_indices

def fibonoci_i_pierwsza(tablica):
    n = len(tablica)
    fib_indices = fibonacci_indices(n)
    found_prime_outside_fib = False
    
    for i in range(n):
        if i in fib_indices:
            if is_prime(tablica[i]):
                return False
        else:
            if is_prime(tablica[i]):
                found_prime_outside_fib = True
    
    return found_prime_outside_fib

tablica = list(map(int, input("Podaj liczby w tablicy: ").split()))
print(fibonoci_i_pierwsza(tablica))