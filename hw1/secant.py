from utils import print_result

def calc_c(eq, a, b):
    solve = lambda x: eq.s(x)
    fa = solve(a)
    fb = solve(b)
    return ((a*fb)-(b*fa))/(fb-fa)

def secant(eq, a, b, eps=10e-10):
    print('Modify Secant method: {}'.format(eq.get_name()))
    solve = lambda x: eq.s(x)
    cnt = 1
    c = calc_c(eq, a, b)
    a = b
    b = c
    while abs(b-a) >= eps:
        print_result(cnt, c, a, b)
        cnt += 1
        c = calc_c(eq, a, b)
        a = b
        b = c
    print_result(cnt, c, a, b)
