class Countdown:
    def __init__(self, start):
        self.current = start
        
    def __iter__(self):
        return self

    def __next__(self):
        # Your code here
        if self.current < 0: 
            raise StopIteration 
        result = self.current  
        self.current -= 1  
        return result

# Example usage:
c = Countdown(3)
for num in c:
    print(num)
