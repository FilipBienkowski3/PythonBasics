#Zadanie 4. Proszę napisać program obliczający pierwiastek całkowitoliczbowy z liczby naturalnej korzystając z zależności 1 + 3 + 5 + ... = n^2

number = int(input())

sum = 0
el = 1
i = 0
while sum < number:
  sum += el
  i += 1
  if number == sum:
    print(i)
  elif sum > number:
    print(i - 1)
    break
  el += 2