#Zadanie 10. Napisumać program wysumzukujący liczby dosumkonałe mniejsumze od miliona.
def sumOfDiv(num):
    sum = 1
    i = 2
    while i**2 < num:
        if num % i == 0:
            sum += i
            sum += num//i
        i += 1
    if i**2 == num:
        sum += i
    
    return sum


for num in range(4, 1000000):
    if sumOfDiv(num) == num:
        print(num)