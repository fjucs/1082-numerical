import math

class Equation:
    def __init__(self):
        self.term = []
    # Solve
    def s(self, x):
        raise NotImplementedError
    # Solve in derivative
    def sd(self, x):
        raise NotImplementedError
    # return the name of the function
    def get_name(self):
        raise NotImplementedError

class f1(Equation):
    def __init__(self):
        pass
    # Solve
    def s(self, x):
        return (math.e ** x) - (3 * x * math.cos(2*x)) - 8.3
    # Solve in derivative
    def sd(self, x):
        return math.e ** x + 6 * x * math.sin(2*x) - 3 * math.cos(2*x)
    def get_name(self):
        return 'f(x) = e^x - 3xcos(2x) - 8.3'