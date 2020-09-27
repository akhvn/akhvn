from random import *

L = [randint(0,99) for i in range(15)]
print(*L)
for i in range(len(L)):
    for j in range(len(L)-1-i):
        if L[j]>L[j+1]:
            L[j],L[j+1]=L[j+1],L[j]
print(*L)
        
    
    
