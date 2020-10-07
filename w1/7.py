def f(a,b=10,c=20):
    return (a+b)**c
print('1:',f(7,3,1))
print('2:',f(7,b=3,c=5))
print('3:',f(*[9,12,3]))
print('4:',f(**{'a':10,'b':1,'c':7}))
