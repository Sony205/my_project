def fibonaccі(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

for num in fibonaccі(5):
    print(num, end=' ')
