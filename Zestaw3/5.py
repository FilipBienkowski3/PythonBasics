#Zadanie 5.
#Napisać program, który wczytuje wprowadzany z klawiatury ciąg liczb naturalnych zakończonych zerem stanowiącym wyłącznie znacznik końca danych. Program powinien wypisać 10 co do wielkości
#wartość, jaka wystąpiła w ciągu. Można założyć, że w ciągu znajduje się wystarczająca liczba elementów
def sort(arr):
  min = 10000
  for k in range(len(arr)):
    for i in range(k, len(arr)):
      if arr[i] <= min:
        tmp = i
        min = arr[i]
    arr[tmp], arr[k] = arr[k], min
    min = 10000
  return arr[9]

arr = [
  3, 5, 123, 5345, 7, 56, 67, -6, 34, 54, 3, 6, 6, 4234, 6, 3, 52, 678, 0, 5,
  52, 21
]
print(sort(arr))
