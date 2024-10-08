#Zadanie 5. Dana jest liczba naturalna o niepowtarzających się cyfrach pośród których nie ma zera. Ile różnych liczb podzielnych np. przez 7 można otrzymać poprzez wykreślenie dowolnych cyfr w tej liczbie. Np. dla 2315 będą to 21, 35, 231, 315.

def plus1bin(s):
  i = 1
  while s[-i] != "0":
    i += 1
  s = s[0:-i] + "1" + (i - 1) * "0"
  return s


n = input("Wpisz liczbę o różnych cyfrach bez zera: ")
k = len(n)
counter = 0
mask = k * "0"
for i in range(1, 2**k):
  mask = plus1bin(mask)
  # print(":test:", mask)
  new_num = ""
  for j in range(k):
    if mask[j] == "1":
      new_num = new_num + n[j]

  if int(new_num) % 7 == 0:
    counter += 1
    print(new_num)
print(counter)