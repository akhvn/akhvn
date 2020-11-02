from itertools import*

def get_combinations(s, n):
    res=[]
    for i in range(1,n+1):
        res+=list(map(lambda x:''.join(x),list(combinations(sorted(s),i))))
    return res
