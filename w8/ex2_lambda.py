fib=lambda n:[[(m.append(1),m[-1])[1]if i<2 else (m.append(m[-1]+m[-2]),m[-1])[1]for i in range(n)]for m in [[]]][0]
print(*fib(9))
