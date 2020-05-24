import random
import math

import methods

def load_data(name):
    data_list = []
    with open(name, 'r') as f:
        lines = f.readlines()
        # print(lines)
        data = []
        for i in lines:
            if i != '\n':
                x, y = [float(x) for x in i.strip('\n').split(' ')]
                data.append(methods.Point(x, y))
                # print()
            else:
                data_list.append(data)
                data = []
        data_list.append(data)
    return data_list

# sinx-cosx*x+e*sinx*cosx
def func(x):
    sinx = math.sin(x)
    cosx = math.cos(x)
    return sinx - cosx + math.e * sinx * cosx

def main():
    dl = load_data('data.txt')

    dl.append(methods.gen_data(50, 2.5, 7.5, func))

    print(dl[0])

    methods.plot('Lagrange DataSet0', methods.lagrange(dl[0]), dl[0], False)
    # for x, y in dl[0]:
    #     print(x, y)
    # a = methods.lagrange(dl[0])
    # print(a)


if __name__ == "__main__":
    main()
