class Fib(object):
    """斐波那契数列"""
    def __init__(self, n):
        self.n = n
        self.current = 0
        self.num1 = 1
        self.num2 = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.n:
            ret = self.num1
            self.num1, self.num2 = self.num2, self.num2+self.num1
            self.current += 1
            return ret
        else:
            raise StopIteration

a=Fib(10)
for temp in a:
    print(temp)