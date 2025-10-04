def fibonaccі(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

n = 5
print(f'Первые {n} чисел Фибоначчи')
for num in fibonaccі(n):
    print(num, end=' ')
