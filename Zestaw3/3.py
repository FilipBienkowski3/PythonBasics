#Zadanie 3 Napisać program generujący i wypisujący liczby pierwsze mniejsze od N metodą Sita Eratostenesa.
def sieve_eratosthenes(n):
    sieve = [True] * n
    sieve[0] = sieve[1] = False
    
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n, i):
                sieve[j] = False 
    
    primes = [i for i, is_prime in enumerate(sieve) if is_prime]
    return primes

n = 100
print(sieve_eratosthenes(n))