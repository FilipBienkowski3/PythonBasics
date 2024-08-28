# Zadanie 12. Proszę napisać program wyznaczający największy wspólny dzielnik 3 zadanych liczb
def nwd(a,b):
    while b != 0:
        b, a = a%b, b
    return a


def nwd3(a, b, c):
    return nwd(nwd(a, b), c)


print(nwd3(60, 30,105))