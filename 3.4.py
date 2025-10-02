class Countdown:
    def __init__(self, n):
        self.n = n
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.n <= 0:
            raise StopIteration
        c = self.n
        self.n -= 1
        return c

for number in Countdown(5):
    print(number, end=' ')