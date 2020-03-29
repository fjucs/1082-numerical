from utils import print_result

def bisection(eq, a, b, eps=10e-10):
    solve = lambda x: eq.s(x)
    cnt = 1
    print('Bisection method: {}'.format(eq.get_name()))
    if solve(a) * solve(b) > 0:
        raise RuntimeError('Cannot solve in bisection method')
    while abs(b - a) >= eps:
        c = (a + b) / 2
        print_result(cnt, c, a, b)
        if solve(a) * solve(c) < 0:
            b = c
        else:
            a = c
        cnt += 1
    print_result(cnt, c, a, b)