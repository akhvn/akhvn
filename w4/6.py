def cool_wrap(func):
    def wrapper(inlist):
        original = func(inlist)
        if not original:
            return('Нет')
        elif original > 10:
            return('Очень много')
        else:
            return original
    return wrapper


@cool_wrap
def f(lst):
    count = 0
    for num in lst:
        if num % 2 == 0:
            count += 1
    return count

print(f([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(f([1, 3, 5]))
print(f([2, 4, 6, 8, 10, 12, 14, 16, 20, 24, 32, 40, 48]))
