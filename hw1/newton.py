from utils import print_result
import random

def get_delta(eq, c):
    s = lambda x: eq.s(x)
    sd = lambda x: eq.sd(x)
    return - (s(c)/sd(c))

def newton(eq, a, b, eps=10e-10):
    print('Newton method: {} a={}, b={}'.format(eq.get_name(), a, b), end='')
    s = lambda x: eq.s(x)
    sd = lambda x: eq.sd(x)
    cnt = 1
    c = a + random.random()*(b-a)
    print(', c={}'.format(c))
    delta = get_delta(eq, c)
    while abs(delta) >= eps:
        print_result(cnt, c)
        #
        c += delta
        delta = get_delta(eq, c)
        cnt += 1
    print_result(cnt, c)
