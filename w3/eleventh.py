def c():
    raise ValueError('exception')
def a():
    if 5+5 == 10:
        b()   
def b():
    c()
a()

#vidno chto oshibka v def c()
#a imenno perevod slova v tip dannyh int nevozmozhen
