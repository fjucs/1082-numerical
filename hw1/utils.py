
def print_result(cnt, c, a=None, b=None):
    if a == None and b == None:
        print('[{:2d}] c={:.15f}'.format(cnt, c))
    else:
        print('[{:2d}] c={:.15f}; a={:.10f}; b={:.10f}'.format(cnt, c, a, b))
