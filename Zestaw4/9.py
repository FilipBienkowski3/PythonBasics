#Zadanie 9. Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Proszę napisać funkcję, która w poszukuje 
# w tablicy kwadratu o liczbie pól będącej liczbą nieparzystą większą od 1, którego iloczyn 4 pól narożnych wynosi
#  k. Do funkcji należy przekazać tablicę i wartość k. Funkcja powinna zwrócić informacje czy udało się znaleźć 
# kwadrat oraz współrzędne (wiersz, kolumna) środka kwadratu.


def find_square_of_edge_product_k(tab, k):
  for dlugosc_boku in range(2, len(tab), 2):
    for i in range(len(tab)):
      for j in range(len(tab)):
        if i + dlugosc_boku < len(tab) and j + dlugosc_boku < len(tab):
          if tab[i][j] * tab[i + dlugosc_boku][j] * tab[i + dlugosc_boku][
              j + dlugosc_boku] * tab[i][j + dlugosc_boku] == k:
            return (True, j + dlugosc_boku // 2, i + dlugosc_boku // 2)


tab = [[1, 2, 4, 2, 1, 3],
       [3, 2, 56, 7, 7, 4],
       [1, 2, 7, 2, 1, 3],
       [2, 3, 5, 1, 3, 0],
       [3, 2, 56, 7, 7, 4],
       [4, 6, 2, 3, 45, 6]]

print(find_square_of_edge_product_k(tab, 16))
