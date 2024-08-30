#Zadanie 3. Napisz program wczytujący liczbę naturalną z klawiatury i odpowiadający na pytanie, czy liczba naturalna jest palindromem, a następnie czy jest palindromem w systemie dwójkowym.

num = int(input())

rev_num = 0
num_copy = num
while num_copy > 0:
  rev_num = rev_num * 10 + num_copy % 10
  num_copy //= 10

print(rev_num == num)
#zapis liczby
liczba_w_2=0
while num_copy>0:
  
  liczba_w_2=liczba_w_2 *10 +num_copy%2
  num_copy//=2
print(liczba_w_2)
# binary
num1 = int(input())

rev_num1 = 0
num_copy1 = num1
while num_copy1 > 0:
  rev_num1 = rev_num1 * 2 + num_copy1 % 2
  num_copy1 //= 2
print(rev_num)
print(rev_num1 == num1)
