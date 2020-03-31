from math import e, sin, cos, log

class Equation:
    def __init__(self):
        self.term = []
    # Solve
    def s(self, x):
        raise NotImplementedError
    # Solve in derivative
    def sd(self, x):
        raise NotImplementedError
    # Solve in fixed point method
    def fp(self, x):
        raise NotImplementedError
    # return range
    def bound(self):
        raise NotImplementedError
    # return the name of the function
    def get_name(self):
        raise NotImplementedError

class f1(Equation):
    def __init__(self):
        pass
    def s(self, x):
        return (e ** x) - (3 * x * cos(2*x)) - 8.3
    def sd(self, x):
        return e ** x + 6 * x * sin(2*x) - 3 * cos(2*x)
    def fp(self, x):
        raise OverflowError
    def bound(self):
        return -2, 2
    def get_name(self):
        return 'f(x) = e^x - 3xcos(2x) - 8.3'

class f2(Equation):
    def __init__(self):
        pass
    def s(self, x):
        return (e**(x*sin(x))) - x*cos(2*x) - 2.8
    def sd(self, x):
        return 2*x*sin(2*x) - cos(2*x) + (e**(x*sin(x)))*(sin(x)+x*cos(x))
    def fp(self, x):
        return log(x*cos(2*x)+2.8)/sin(x)
    def bound(self):
        return 0, 2
    def get_name(self):
        return 'f(x) = e^{x*sinx}-x*cos(2x)-2.8'

class f3(Equation):
    def __init__(self):
        self.term = []
    def s(self, x):
        return sin(cos(e**x))
    def sd(self, x):
        return -((e**x)*sin(e**x)*cos(cos(e**x)))
    def fp(self, x):
        raise ValueError
    def bound(self):
        return 0, 1
    def get_name(self):
        return 'f(x) = sin(cos(e^x))'

class f4(Equation):
    def __init__(self):
        self.term = []
    def s(self, x):
        return (e**(x*sin(x))) + sin(x)
    def sd(self, x):
        return ((e**(x*sin(x)))*(sin(x)+x*cos(x)))+cos(x)
    def fp(self, x):
        raise log(sin(x))/sin(x)
    def bound(self):
        return 2, 4
    def get_name(self):
        return 'f(x) = e^{x*sin(x)} + cos(x)'
