import numpy as np

'''
Calculate the sum
'''
def sum(x, y=None, px=1, py=1):
	# if none
    if y is None:
        y = [1] * len(x)
    if x is None:
        x = [1] * len(y)
    # calc
    tmp = 0
    for a, b in zip(x, y):
        tmp += (a ** px) * (b ** py)
    return tmp

'''
Calculate the necessary terms for Least Square Method

return (A, b) in the matrix equation Ax=b
	both A and b are lists
'''
def calc_terms(n, x, y):
	# Calc for x_i
	left = []
	for i in range(1, 2*n+1):
		left.append(sum(x, None, i))
	# Calc for x_i^n y_i
	right = [sum(None, y)]
	for i in range(1, n+1):
		right.append(sum(x, y, i, 1))
	return (left, right)

def to_matrix(data_len, A, b):
	n = len(A) // 2 + 1
	# Calculate matrix A (nxn)
	A_m = []
	for i in range(n):
		row = []
		for j in range(n):
			if i == 0: # first row
				if j == 0:
					row.append(data_len)
				else:
					row.append(A[j-1])
			else:
				row.append(A[i-1+j])
		A_m.append(row)
	A_m = np.asarray(A_m)
	# Calculate matrix b (1xn)
	b_m = []
	for i in range(n):
		row = [b[i]]
		b_m.append(row)
	b_m = np.asarray(b_m)
	return (A_m, b_m)

'''
Least Square Method for Pn(x)

return a_i as a list [a_0, a_1, ... , a_n]
'''
def least_square(n, x, y):
	A, b = calc_terms(n, x, y)
	A, b = to_matrix(len(x), A, b)
	# print(A)
	# print(b)
	X = np.linalg.solve(A, b)
	print(X)

x = []
y = []

def main():
	np.set_printoptions(precision=3)
	# Read the testdata
	with open('data.txt', 'r') as f:
		for i in f:
			px, py = [float(x) for x in i.strip().split()]
			x.append(px)
			y.append(py)
	#
	for i in range(1, 10):
		least_square(i, x, y)


if __name__ == '__main__':
	main()
