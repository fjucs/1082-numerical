import random
import matplotlib.pyplot as plt
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])

'''Generate num random floats [low, high]'''
def gen_numbers(num, low, high):
    n = []
    for _ in range(num):
        n.append(random.uniform(low, high))
    return n

'''Generate num random coordinate'''
def gen_data(num, low, high, func):
    x = gen_numbers(num, low, high)
    y = []
    pl = []

    if not func:
        raise RuntimeError('`func` is None')

    for i in x:
        y.append(func(i))

    for x, y in zip(x, y):
        pl.append(Point(x, y))
    return pl

'''Plot the points'''
def plot(name, data: Point, orig: Point, save=True) -> None:
    plt.cla()
    plt.clf()
    plt.title(name or 'default')
    # Convert point to xlist and ylist
    xl = []
    yl = []
    for x, y in data:
        xl.append(x)
        yl.append(y)
    plt.plot(xl, yl, 'r-')
    a = []
    b = []
    for x, y in orig:
        a.append(x)
        b.append(y)
    plt.plot(a, b, 'bo')
    #
    plt.ylim(-10, 30)
    #
    if save:
        plt.savefig('{}.png'.format(name or 'default'))
    else:
        plt.show()
