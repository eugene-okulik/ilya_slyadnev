result_1 = "результат операции: 42"
result_2 = "результат операции: 514"
result_3 = "результат работы программы: 9"

number_1 = int(result_1[result_1.index(':') + 2:]) + 10
number_2 = int(result_2[result_2.index(':') + 2:]) + 10
number_3 = int(result_3[result_3.index(':') + 2:]) + 10

print("Результат 1:", number_1)
print("Результат 2:", number_2)
print("Результат 3:", number_3)
