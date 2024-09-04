#Zadanie 5. Dany jest ciąg zer i jedynek zapisany w tablicy T[N]. Proszę napisać funkcję,
#  która odpowiada na pytanie czy jest możliwe pocięcie ciągu na kawałki z których każdy
#  reprezentuje liczbę pierwszą. Długość każdego z kawałków nie może przekraczać 30. Na 
# przykład dla ciągu 111011 jest to możliwe, a dla ciągu 110100 nie jest możliwe.


def prime(n):
  if n < 2 :
    return False
  for i in range(2, int(n**(0.5))+1):
    if n%i == 0 :
      return False
  return True


def fun1(T1,res=0,pos=0,cut=False):
  if T1==0 and prime(res):
    return True
  if T1==0:
    return False
  if cut and not prime(res):
    return False
  if cut:
    res=0
    pos=0
  
  return fun1(T1//10,res+((T1 % 10) * 10**pos),pos+1,False) or fun1(T1//10,res+((T1 % 10) * 10**pos),pos+1,True)

  


T1=111011
T2=110100
print(fun1(T1))