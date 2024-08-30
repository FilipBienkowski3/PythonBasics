#Zadanie 9. Napisać program, który oblicza pole figury pod wykresem funkcji y = 1/x w przedziale od 1
# do k, metodą prostokątów.

def func(x):
    return 1/x

def calc_area(k, step = 0.0001):
    area = 0
    x = 1
    while x < k:
        area += step*func(x)
        x += step

    return area

k = int(input())
print(calc_area(k))