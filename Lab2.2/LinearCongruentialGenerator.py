class LinearCongruentialGenerator:
    def __init__(self, x0, a, b, k):
        self.state = x0
        self.a = a
        self.b = b
        self.m = 2**k

    def next(self):
        self.state = (self.a * self.state + self.b) % self.m
        return self.state / self.m
    