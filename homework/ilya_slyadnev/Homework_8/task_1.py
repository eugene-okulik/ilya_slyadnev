import random

salary = int(input("Ваша зарплата?: "))
bonus = random.choice([True, False])

if bonus:
    random_bonus = random.randint(1, 25000)
    result_salary = salary + random_bonus
else:
    result_salary = salary

print(f'Ваша зарплата: ${result_salary}')
