def even_numbers(func):
    def wrapper(ins):
        orig = func(ins)
        if not orig:
            return('Нет(((')
        elif orig > 10:
            return('ужас, как много четных чисел')
        else:
            return orig
    return wrapper

@even_numbers
def f(L):
    k = 0
    for n in L:
        if n % 2 == 0:
            k += 1
    return k

print('in the first list ', f([99,12,10,47,148]))
print('in the second list ', f([2, 4, 6,8, 10, 12, 14,16,100,150,1000000,1520]))
print('in the third list ', f([1,9,7,45,39]))
