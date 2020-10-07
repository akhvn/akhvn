L1=[i for i in range(1,50,10)]
L9=[i for i in range(9,50,10)]
L = sorted(L1+L9)
print(*[i**2 for i in L])
