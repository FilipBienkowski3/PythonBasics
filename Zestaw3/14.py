#Zadanie 14. Napisać program wyznaczający na drodze eksperymentu prawdopodobieństwo tego, że w
#grupie N przypadkowo spotkanych osób, co najmniej dwie urodziły się tego samego dnia roku. Wyznaczyć
#wartości prawdopodobieństwa dla N z zakresu 20-40.


def calc_probability(n):
  k = 365
  p_prim = 1
  for i in range(n):
    p_prim *= 1 - i / k

  return 1 - p_prim


print(calc_probability(20))
print(calc_probability(30))
print(calc_probability(40))
