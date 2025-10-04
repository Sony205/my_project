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

n = 5
print(f'Числа от {n} до 1')
for number in Countdown(n):
    print(number, end=' ')