from itertools import*

def get_permutations(s, n):
    return sorted(list(map(lambda x:''.join(x),permutations(s,n))))
