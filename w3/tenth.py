class NegError(Exception):
    def __init__(self, text):
        self.txt = text
 
a = input("Input positive number: ")
try:
    a = int(a)
    if a < 0:
        raise NegError("Do you really think, it's positive?")
except NegError as ne:
    print(ne)
else:
    print(a)
