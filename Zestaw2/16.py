# Zadanie 16. Liczba Smitha to taka, której suma cyfr jest równa sumie cyfr wszystkich liczb występujących
# w jej rozkładzie na czynniki pierwsze. Na przykład: 85 = 5∗17, 8+5 = 5+1+7. Napisać program wypisujący
# liczby Smitha mniejsze od 1000000.

from math import sqrt

def czy_pierwsza(n):
    if n==2 or n==3: return True
    if n <= 1 or n % 2 == 0 or n % 3 == 0: return False
    else:
        i = 5
        while i < sqrt( n ) + 1:
            if n % i == 0: return False
            i += 2
            if n % i == 0: return False
            i += 4
    return True

def suma_cyfr(n):
    suma = 0
    while n > 0:
        suma += n % 10
        n = n // 10
    return suma

def suma_rozkladu(n):
    suma = 0
    i = 2
    if czy_pierwsza(n): return suma_cyfr(n) + 1
    else:
        while n != 1:
            while n % i == 0:
                k = suma_cyfr( i )
                suma += k
                n //= i
            i += 1

    return suma

liczba = int( input() )

if suma_rozkladu( liczba ) == suma_cyfr( liczba ): print("Tak")
else: print("Nie")