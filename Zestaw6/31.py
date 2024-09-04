#Zadanie 31. Proszę napisać funkcję, która jako parametr otrzymuje 
# liczbę naturalną i zwraca sumę iloczynów elementów wszystkich niepustych
#  podzbiorów zbioru podzielników pierwszych tej liczby. Można założyć, 
# że liczba podzielników pierwszych nie przekracza 20, zatem w pierwszym 
# etapie funkcja powinna wpisać podzielniki do tablicy pomocniczej. 
# Przykład: 60 → [2, 3, 5] → 2 + 3 + 5 + 2 ∗ 3 + 2 ∗ 5 + 3 ∗ 5 + 2 ∗ 3 ∗ 5 = 71
def get_prime_divisors(n: int):
    divisors = []
    i = 2
    while n > 1:
        if n % i == 0:
            if i not in divisors:
                divisors.append(i)
            while n % i == 0:
                n //= i
        i += 1
    return divisors

def sum_of_products(divisors, index=0, current_product=1):
    if index == len(divisors):
        return current_product if current_product != 1 else 0

    return sum_of_products(divisors, index + 1, current_product * divisors[index]) + sum_of_products(divisors, index + 1, current_product)


def sum_of_iloczynow(n: int):
    divisors = get_prime_divisors(n)
    print(divisors)
    return sum_of_products(divisors)


n = 60
print(sum_of_iloczynow(n))