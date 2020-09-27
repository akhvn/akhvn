#from random import *

L = int(input('Введите длину массива: '))
#A = [randint(0,99) for i in range(L)]
A = list(map(int,input().split()))
#print(*A)
k = 0
B = []
while sum(B)<sum(A):
    B.append(A[k]+A[-k-1])
    k+=1
print(B)
