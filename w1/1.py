L = []
while True:
    a = input()
    if a == "End":
        break
    else:
        L.append(int(a))
mx = -float('inf')
mn = float('inf')
s = 0
for i in L:
    if i<mn:
        mn = i
    if i>mx:
        mx = i
    s += i
sr = s/len(L)
ch = 0
for i in L:
    ch += (i-sr)**2
srk =(ch/(len(L)-1))**(1/2)
print('max=', mx)
print('min=', mn)
print('srednee=', sr)
print('sredneekvadr=', srk)
    
    


    
        
        
