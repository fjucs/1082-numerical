from utils import print_result

def calc_c(a, fa, b, fb):
    return ((a*fb)-(b*fa)) / (fb-fa)

def get_c(eq, a, b):
    solve = lambda x: eq.s(x)
    return calc_c(a, solve(a), b, solve(b))

def false_position(eq, a, b, eps=10e-10):
    print('False Position method: {}'.format(eq.get_name()))
    solve = lambda x: eq.s(x)
    cnt = 1
    pre_c = 0.0
    c = get_c(eq, a, b)
    while abs(c - pre_c) >= eps:
        print_result(cnt, c, a, b)
        #
        if solve(a) * solve(c) < 0:
            b = c
        else:
            a = c
        #
        pre_c = c
        c = get_c(eq, a, b)
        cnt += 1
    print_result(cnt, c, a, b)