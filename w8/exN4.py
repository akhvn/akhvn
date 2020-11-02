from itertools import*

def get_combinations_with_r(s, n):
    return list(map(lambda x:''.join(x),list(combinations_with_replacement(sorted(s),n))))
