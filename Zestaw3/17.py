#Zadanie 17. Dane są dwie N-elementowe tablice t1 i t2 zawierające liczby naturalne. Z wartości w obu
#tablicach możemy tworzyć sumy. „Poprawna” suma to taka, która zawiera co najmniej jeden element (z
#tablicy t1 lub t2) o każdym indeksie. Na przykład dla tablic: t1 = [1,3,2,4] i t2 = [9,7,4,8] poprawnymi
#sumami są na przykład 1+3+2+4, 9+7+4+8, 1+7+3+8, 1+9+7+2+4+8. Proszę napisać funkcje generującą
#i wypisująca wszystkie poprawne sumy, które są liczbami pierwszymi. Do funkcji należy przekazać dwie
#tablice, funkcja powinna zwrócić liczbę znalezionych i wypisanych sum.import math
import math

def is_prime(num):
    if num <= 1:
        return False
    if num == 2 or num == 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    
    for i in range(5, int(math.sqrt(num)) + 1, 6):
        if num % i == 0 or num % (i + 2) == 0:
            return False

    return True


def decimal_to_base(num, base, leng):
    num_base = [0] * leng

    for i in range(len(num_base) - 1, -1, -1):
        num_base[i] = num % base
        num //= base
    
    return num_base


def create_sum(t1, t2, mask_num: int) -> int:
    s = 0
    mask = decimal_to_base(mask_num, 3, len(t1))
    
    for i in range(len(t1)):
        if mask[i] == 0:
            s += t1[i]
        elif mask[i] == 1:
            s += t2[i]
        elif mask[i] == 2:
            s += t1[i] + t2[i]

    return s


def ex17(t1, t2) -> int:
    counter: int = 0

    for mask in range(3 ** len(t1)):
        s = create_sum(t1, t2, mask)
        if is_prime(s):
            print(s)
            counter += 1

    return counter


t1 = [1, 3, 2, 4]
t2 = [9, 7, 4, 8]
print("Liczba znalezionych sum:", ex17(t1, t2))