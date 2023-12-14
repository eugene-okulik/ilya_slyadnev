def operation_decorator(func):
    def wrapper(num1, num2):
        if num1 == num2:
            return func(num1, num2, '+')
        elif num1 > num2:
            return func(num1, num2, '-')
        elif num2 > num1:
            return func(num1, num2, '/')
        elif num1 < 0 or num2 < 0:
            return func(num1, num2, '*')

    return wrapper


@operation_decorator
def calc(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '/':
        return num1 / num2
    elif operation == '*':
        return num1 * num2


result = calc(5, 5)
print(result)
