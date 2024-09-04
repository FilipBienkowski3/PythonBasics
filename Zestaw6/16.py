#Zadanie 16. Wyrazy budowane są z liter a..z. Dwa wyrazy ”ważą” tyle samo jeżeli: 
# mają tę samą liczbę samogłosek oraz sumy kodów ascii liter z których są zbudowane są 
# identyczne, na przykład ""ula" → 117, 108, 97 oraz "exe" → 101, 120, 101. Proszę napisać
#  funkcję wyraz(s1,s2), która sprawdza czy jest możliwe zbudowanie wyrazu z podzbioru
#  liter zawartych w s2 ważącego tyle co wyraz s1.Dodatkowo funkcja powinna wypisać znaleziony wyraz.
def liczba_samoglosek(s):
    counter = 0
    n = len( s )
    for i in range( n ):
        if czy_samogloska( s[i] ): counter += 1
    #end for
    return counter


def czy_samogloska(z):
    elements = {'a', 'e', 'i', 'o', 'u', 'y'}
    if z in elements:
        return True
    return False


def waga_wyrazu(s):
    suma = 0
    n = len(s)
    for i in range( n ):
        suma += ord( s[i] )
    return suma



def zad16(s, T):
    def rek(s, x, T):
        if waga_wyrazu(x) > waga_wyrazu(s):
            return False

        if waga_wyrazu(x) == waga_wyrazu(s):
            if liczba_samoglosek(x) == liczba_samoglosek(s):
                print(x)
                return True

        for z in T:
            if rek(s, x + z, T):
                return True

        return False

print( zad16('ula', ['u', 'l', 'a'] ) )