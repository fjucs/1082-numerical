from utils import print_result
import random

def fixed_point(eq, a, b, eps=10e-10):
    print('Fixed Point method: {}'.format(eq.get_name()), end='')
    try:
        fixed_point_impl(eq, a, b, eps)
    except:
        print('Divergence')
        return

def fixed_point_impl(eq, a, b, eps=10e-10):
    s = lambda x: eq.s(x)
    sd = lambda x: eq.sd(x)
    fp = lambda x: eq.fp(x)
    c = a + random.random()*(b-a)
    print(' c={}'.format(c))
    pre_c = c
    cnt = 1
    #
    c = fp(pre_c)
    while abs(c-pre_c) >= eps:
        print_result(cnt, c)
        pre_c = c
        c = fp(pre_c)
        cnt += 1
    print_result(cnt, c)
