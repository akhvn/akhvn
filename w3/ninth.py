try:
    int('78954')
    #int("ya programmist")
except ValueError:
    print("How do you want to make a number from text?")
finally:
    print("now you're at the finally stage")
