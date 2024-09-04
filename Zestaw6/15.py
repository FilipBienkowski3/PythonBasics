#Zadanie 15. Problem 8 Hetmanów (treść oczywista)
import copy


def queen(lvl, board):
  global licznik
  if lvl == 8:
    licznik += 1
    print(licznik)
    return
  for i in range(8):
    if board[lvl][i] == 0:
      bc = copy.deepcopy(board)
      bc[lvl][i] = 2
      #lewy skos
      k, l = i - 1, lvl + 1
      while k >= 0 and l < 8:
        bc[l][k] = 1
        k -= 1
        l += 1
      #wdol
      l = lvl + 1
      while l < 8:
        bc[l][i] = 1
        l += 1
      #prawyskos
      k = i + 1
      l = lvl + 1
      while k < 8 and l < 8:
        bc[l][k] = 1
        k += 1
        l += 1
      queen(lvl + 1, bc)


licznik = 0
board = [[0 for i in range(8)] for i in range(8)]
queen(0, board)
