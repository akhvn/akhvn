import sys
import argparse

def fib(n: int):
	a, b = 0, 1
	for i in range(n):
		a, b = b, a + b
	return a


def CreateParser(c: str):
	prs = argparse.ArgumentParser()
	if len(c) > 1:
		prs.add_argument('--' + str(c))

	else:
		prs.add_argument("-" + str(c))

	return prs


if __name__ == "__main__":
	prs = CreateParser('n')
	namespace = prs.parse_args()

	print(fib(int(namespace.n)))
