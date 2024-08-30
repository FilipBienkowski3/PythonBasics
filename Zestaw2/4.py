#Zadanie 4. Liczba dwu-trzy-piątkowa w rozkładzie na czynniki pierwsze nie posiada innych czynników niż 2,3,5. Jedynka też jest taką liczbą. Napisz program, który wylicza ile takich liczb znajduje się w przedziale od 1 do N włącznie.


num = int(input())

counter = 0

num_2 = 1
while num_2 <= num:
  num_3 = num_2
  while num_3 <= num:
    num_5 = num_3
    while num_5 <= num:
      counter += 1
      num_5 *= 5
    num_3 *= 3
  num_2 *= 2

print(counter)
# inne

numerek = int(input("podaj:"))
count = 1
for i in range(2, numerek + 1):
  while i != 1:
    if i % 2 == 0:
      i = i / 2
      if i == 1:
        count += 1
    elif i % 3 == 0:
      i = i / 3
      if i == 1:
        count += 1
    elif i % 5 == 0:
      i = i / 5
      if i == 1:
        count += 1
    else:
      break
print(count)
