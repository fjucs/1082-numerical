from utils import print_result

def calc_c(a, fa, b, fb):
    return ((a*fb)-(b*fa)) / (fb-fa)

def modify_false_position(eq, a, b, eps=10e-10):
    print('Modify False Position method: {}'.format(eq.get_name()))
    solve = lambda x: eq.s(x)
    cnt = 1
    pre_c = 0.0
    fa = solve(a)
    fb = solve(b)
    c = calc_c(a, fa, b, fb)
    while abs(c - pre_c) >= eps:
        print_result(cnt, c, a, b)
        #
        fc = solve(c)
        if fa * fc < 0:
            b = c
            fa = fa/2
        else:
            a = c
            fb = fb/2
        #
        pre_c = c
        c = calc_c(a, fa, b, fb)
        cnt += 1
    print_result(cnt, c, a, b)