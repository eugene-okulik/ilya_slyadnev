result = [
    "результат операции: 42",
    "результат операции: 54",
    "результат работы программы: 209",
    "результат: 2"
]

for string_result in result:
    number = int(string_result.split()[-1]) + 10
    print(number)
