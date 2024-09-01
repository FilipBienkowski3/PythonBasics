# Zadanie 4.
# Napisać program obliczający i wypisujący stałą e z rozwinięcia w szereg e = 1/0! + 1/1! +
# 1/2! + 1/3! + ... z dokładnością N cyfr dziesiętnych (N jest rzędu 1000).

from decimal import Decimal, getcontext

def calc_e(precision):
    getcontext().prec = precision + 2
    e = Decimal(1)
    fact = Decimal(1)

    for i in range(1, precision * 10):
        fact *= i
        e += Decimal(1) / fact
    
    return str(e)[:precision + 2]

n = int(input("Podaj ilość cyfr po przecinku: "))
print(calc_e(n))