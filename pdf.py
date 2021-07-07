class PDF:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_function(self, theta):
        from math import exp

        exp_part = exp(self.a * (theta - self.b))

        return self.c + ((1 - self.c) * exp_part / (1 + exp_part))
