class FibonacciIterator:
    def __init__(self, max_value):
        self.max_value = max_value
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.a > self.max_value:
             raise StopIteration
        current = self.a
        self.a, self.b = self.b,self.a + self.b
       
        return current
        # Your code here

fib_iter = FibonacciIterator(10)
for num in fib_iter:
    print(num)
