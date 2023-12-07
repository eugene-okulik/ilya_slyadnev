result = [
    "результат операции: 42",
    "результат операции: 54",
    "результат работы программы: 209",
    "результат: 2"
]


def print_results(result_list):
    for string_result in result_list:
        number = int(string_result.split()[-1]) + 10
        print(number)


print_results(result)
