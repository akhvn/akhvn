n = int(input('choose your number: '))
try:
    k = n / 0
except ZeroDivisionError:
    print("Делим на ноль")
