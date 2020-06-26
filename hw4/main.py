import numpy as np
import matplotlib.pyplot as plt
import math

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

left = [Σx, Σx^2, Σx^3, ..., Σx^2n]
right = [Σy, Σyx, Σyx^2, ..., Σyx^n]
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

'''
Convert the A and b list to np.ndarray
'''
def to_matrix(data_len, A, b):
	n = len(A) // 2 + 1
	# Calculate matrix A (nxn)
	A_m = []
	for i in range(n):
		row = []
		for j in range(n):
			# first row
			if i == 0:
				if j == 0:
					row.append(data_len)
				else:
					row.append(A[j-1])
			# the following rows
			else:
				row.append(A[i-1+j])
		A_m.append(row)
	A_m = np.asarray(A_m, dtype=np.float64)
	# Calculate matrix b (1xn)
	b_m = []
	for i in range(n):
		row = [b[i]]
		b_m.append(row)
	b_m = np.asarray(b_m, dtype=np.float64)
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
	try:
		X = np.linalg.solve(A, b)
	except np.linalg.LinAlgError:
		print('不存在反矩陣')
		return None
	return X

'''
Evaluate for P_n(x) for given a_i
'''
def eval_pn(ai, x):
	ans = 0
	for i, v in enumerate(ai):
		a = v[0]
		if i == 0:
			ans += a
		else:
			ans += (x ** i) * a
	return ans

'''
Find the best choice of n for Pn(x)

sigma_m^2 = Σ( (P_m(x_i) - f(x_i))^2 / (n-m) )
And find the smallest sigma_i and i is the best choice
'''
def find_best_choice(x, y, limit=10):
	slist = []
	for i in range(1, limit+1):
		a = least_square(i, x, y) # get a_i of Pm(x)
		# check if least square failed?
		if a is None:
			continue
		# cal all Pn(x_i)
		plist = []
		for j in x:
			p = eval_pn(a, j)
			plist.append(p)
		# cal for sigma_i^2
		sigma = 0
		for pi, yi in zip(plist, y):
			sigma += (pi - yi) ** 2
		sigma = sigma / (len(x) - i) if len(x) - i != 0 else -1
		# sigma = math.sqrt(sigma)
		slist.append(sigma)

	besti = 0
	bestv = slist[0]
	for i, v in enumerate(slist):
		# print(i, v)
		if bestv > v and v > 0:
			besti = i
			bestv = v
	return besti+1

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
	plt.scatter(x, y, s=10, c='r') # draw the dataset
	# Find the best choice
	n = find_best_choice(x, y, 100)
	print('Best Choice=', n)
	# Least Square Method
	A = least_square(n, x, y)

	rang = [-10, 10]
	off = 0.01
	# Plot the Pn(x)
	xi = np.arange(*rang, off)
	yi = [eval_pn(A, t) for t in xi]
	plt.plot(xi, yi)
	plt.show()

if __name__ == '__main__':
	main()
