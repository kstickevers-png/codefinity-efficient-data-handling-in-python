class OddRange:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
        self.current = None

    def __iter__(self):
        return self

    def __next__(self):
        if self.current == None:
            self.current= self.start
        while self.current < self.stop and self.current % 2 == 0:
            self.current += 1
# now self.current is odd (or >= stop)
        if self.current >= self.stop:
            raise StopIteration
        result = self.current
        self.current += 2
        return result

# Example usage
odds = OddRange(3, 11)
for number in odds:
    print(number)
