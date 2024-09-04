#Zadanie 14. Problem wież w Hanoi (treść oczywista)
def move(n, A, B, C):
    if n == 1:
        print(A, "->", B)
    else:
        move(n-1, A, C, B)
        print(A, "->", B)
        move(n-1, C, B, A)

move(3, "A", "B", "C")
