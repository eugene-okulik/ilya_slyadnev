def fibo():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


fibo_gen = fibo()


def get_fibo_number(n):
    for _ in range(n - 1):
        next(fibo_gen)
    return next(fibo_gen)


print("Пятое число:", get_fibo_number(5))
print("Двухсотое число:", get_fibo_number(200))
print("Тысячное число:", get_fibo_number(1000))
print("Стотысячное число:", get_fibo_number(100000))
