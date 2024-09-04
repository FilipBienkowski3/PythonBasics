# Zadanie 22. Dana jest tablica T[N] zawierająca liczby naturalne. Po tablicy możemy przemieszczać się
# według następującej zasady: z pola o indeksie i możemy przeskoczyć na pole o indeksie i+k jeżeli k jest
# czynnikiem pierwszym liczby t[i] mniejszym od t[i]. Proszę napisać funkcję, która zwraca informację czy jest
# możliwe przejście z pola o indeksie 0 na pole o indeksie N-1. Funkcja powinna zwrócić liczbę wykonanych
# skoków lub wartość -1 jeżeli powyższe przejście nie jest możliwe.

def check(t):
    leng = len(t)
    mark = [leng+2] * leng
    mark[0] = 0

    for i in range(0, leng):
        if mark[i] > leng:
            continue

        for div in range(2, int(t[i]**0.5)+2):
            if t[i] % div == 0:
                mark[i+div] = min(mark[i]+1, mark[i+div])

                while t[i] % div == 0:
                    t[i] //= div

    print(mark)
    return mark[-1] if mark[-1] <= leng else -1

arr = [6,5,1,2,4,3]
print(check(arr))