# methods
from bisection import bisection
from falseposition import false_position
from mfp import modify_false_position
from secant import secant
from newton import newton
from fixed_point import fixed_point
# functions
from func import *

if __name__ == '__main__':
    all_funcs = [f1(), f2(), f3(), f4()]
    all_methods = [bisection, false_position, modify_false_position, secant, newton, fixed_point]
    for f in all_funcs:
        for m in all_methods:
            m(f, *f.bound())
