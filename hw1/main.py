from bisection import bisection
from falseposition import false_position
from mfp import modify_false_position

from func import f1

if __name__ == '__main__':
    # bisection(f1(), -2, 2)
    # false_position(f1(), -2, 2)
    modify_false_position(f1(), -2, 2)