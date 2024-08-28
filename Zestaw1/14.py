#Zadanie 14. Napisać program obliczający wartości cos(x) z rozwinięcia w szereg Maclaurina.
from math import factorial


def szereg_Maclaurina(x, dok = 5):
    s = 0
    for i in range(dok):
        s += ((-1)**i)*(x**(2*i))/factorial(2*i)
    return s


print(szereg_Maclaurina(0))