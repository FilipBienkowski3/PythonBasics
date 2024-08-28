#Zadanie 17. Napisać program wyznaczający wartość do której zmierza iloraz dwóch kolejnych wyrazów ciągu Fibonacciego. Wyznaczyć ten iloraz dla różnych wartości początkowych wyrazów ciągu.

def golden_ratio(prec = 50):
    a, b = 1, 1
    old_ratio, ratio = 0, 1
    while abs(old_ratio - ratio) > 1e-10:
        a, b = b, a + b
        old_ratio, ratio = ratio, b / a
    return ratio

print(golden_ratio())