from random import randint


# блаблабла бла блаблабла бла блаблабла
number = randint(1, 100)


def main():
    while True:

        guess = int(input('Введите число:'))

        if guess < number:
            print('ваше число меньше того, что загадано')
        elif guess > number:
            print('Ваше число больше того, что загадано')
        elif guess == number:
            break


main()
print('Отличная интуиция! Вы угадали число :)')
