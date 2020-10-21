import argparse

def prime_num(n: int):
	PL = []
	a = 2
	while len(PL) != n:
		for i in PL:
			if a % i == 0:
				break
		else:
			PL.append(a)
		a+=1
	return PL 
	
if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument(
		'--show-all',
		'-a',
		action="store_true",
		help="showing also all previous \
		prime numbers before N"
	)
	parser.add_argument(
		'--file',
		 '-f',
		 action="store",
		 type=argparse.FileType("w"),
		 help="file for output"
	)
	parser.add_argument(
		'number',
		type=int
	)
	
	namespace = parser.parse_args()
	
	output = "the {} prime number is {}".format(namespace.number, prime_num(namespace.number)[-1])
	if namespace.show_all is None:
		print(output)

	if namespace.show_all:
		print("list of prime numbers: {}".format(prime_num(namespace.number)))
		if namespace.file:
			print(output, file=namespace.file)

	if namespace.file:
		print("Check out {}".format(namespace.file))
		print(output, file=namespace.file)
