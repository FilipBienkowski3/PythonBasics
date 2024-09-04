#Zadanie 5. Dany jest zbiór punktów leżących na płaszczyźnie 
# opisany przy pomocy struktury dane = [(x1, y1),(x2, y2),(x3, y3), ...(xN , yN )]
#  Proszę napisać funkcję, która zwraca wartość True jeżeli zbiorze istnieją 
# 4 punkty wyznaczające kwadrat o bokach równoległych do osi układu współrzędnych, 
# a wewnątrz tego kwadratu nie ma żadnych innych punktów. Do funkcji należy przekazać strukturę opisującą położenie punktów.
def kwadrat(dane):
  for p1 in dane:
    for bok in range(1, 6):
      x = p1[0]
      y = p1[1]
      count = 0
      #1
      for q, w in [(x + bok, y), (x + bok, y + bok), (x, y + bok)]:

        for p2 in dane:
          if p1 == p2:
            continue
          if q == p2[0] and w == p2[1]:
            count += 1
            break
      if count == 3:
        return True
      count = 0
      #2
      for q, w in [(x + bok, y), (x + bok, y - bok), (x, y - bok)]:

        for p2 in dane:
          if p1 == p2:
            continue
          if q == p2[0] and w == p2[1]:
            count += 1
            break
      if count == 3:
        return True
      count = 0
      #3
      for q, w in [(x - bok, y), (x - bok, y - bok), (x, y - bok)]:

        for p2 in dane:
          if p1 == p2:
            continue
          if q == p2[0] and w == p2[1]:
            count += 1
            break
      if count == 3:
        return True
      count = 0
      #4
      for q, w in [(x - bok, y), (x - bok, y + bok), (x, y + bok)]:

        for p2 in dane:
          if p1 == p2:
            continue
          if q == p2[0] and w == p2[1]:
            count += 1
            break
      if count == 3:
        return True
      #5
      count = 0
      for q, w in [(x + bok, y + bok), (x - bok, y - bok), (x - bok, y + bok),
                   (x + bok, y - bok)]:
        for p2 in dane:
          if p1 == p2:
            continue
          if q == p2[0] and w == p2[1]:
            count += 1
            break
      if count == 4:
        return True
  return False


dane = [(4, 4),
        (0, 0),
        (-4, -4),
        (4, -4),
        (-4, 4)]
print(kwadrat(dane))
