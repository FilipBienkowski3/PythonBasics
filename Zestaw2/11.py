#Zadanie 11. Napisz program wczytujący liczbę naturalną z klawiatury i odpowiadający na pytanie, czy jej cyfry stanowią ciąg rosnący.


def increasing_number(num):
    a = num % 10
    print(a)
    num //= 10
    print(num)
    while num > 0:
        if a <= num % 10:
            return False
        a = num % 10
        print(a)
        num //= 10
        print(num)
    return True


n = int(input())
print(increasing_number(n))