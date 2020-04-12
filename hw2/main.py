import numpy as np
import sys
import time
import datetime
import random

def rand(n):
	A = []
	b = []
	for _ in range(n):
        #
		ta = []
		for _ in range(n):
			ta.append(random.randint(-10, 10))
		A.append(ta)
        #
		tb = []
		tb.append(random.randint(-50, 50))
		b.append(tb)

	return A, b

def output_file(filename, i, A, b, X):
    filename = './data/' + filename + str(i) + '.txt'
    with open(filename, 'w') as f:
        f.write('size={}\n'.format(i))
        f.write('A\n')
        f.write(str(A))
        f.write('b\n')
        f.write(str(b))
        f.write('X\n')
        f.write(str(X))

TEST = [1, 2, 5, 10, 50, 100, 500, 1000, 5000, 10000]

def main():
    np.set_printoptions(threshold=sys.maxsize)
    for i in TEST:
        A, b = rand(i)
        A = np.asarray(A)
        b = np.asarray(b)

        print('{0}x{0} = '.format(i), end='')
        start = time.time()
        X = np.linalg.solve(A, b)
        elapsed = time.time() - start
        print(elapsed)
        output_file('output_', i, A, b, X)

if __name__ == "__main__":
    main()
