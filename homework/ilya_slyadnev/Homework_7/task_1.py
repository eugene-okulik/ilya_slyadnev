import random


random_number = random.randint(0, 9)

while True:
    enter_number = int(input("Угадайте цифру от 0 до 9: "))
    if enter_number == random_number:
        print("Поздравляю! Вы угадали!")
        break
    else:
        print("Попробуйте снова.")
