#Zadanie 2 Napisać program wczytujący dwie liczby naturalne i odpowiadający na pytanie czy są one
#zbudowane z takich samych cyfr, np. 123 i 321, 1255 i 5125, 11000 i 10001.

a, b = map(int, input().split())

print(sorted(str(a)) == sorted(str(b)))
a, b = input().split()

digits = [0]*10 #!
for d in a:
    digits[int(d)] += 1

for d in b:
    digits[int(d)] -= 1

for i in range(10):
    if digits[i] != 0:
        print("NIE")
        break
else:
    print("TAK")
