from random import *

def number_guessing_game():

    def is_valid(n):
        if n.isdigit():
            if 1 <= int(n) <= 100:
                return True
        else:
            return False

    print('Добро пожаловать в числовую угадайку')
    low = input('Выбери минимальное возможное число: ')
    high = input('Выбери максимальное возможное число: ')

    while low > high:
        print('Нижняя граница не может быть больше верхней! Давай попробуем еще раз)')
        low = input('Выбери минимальное возможное число: ')
        high = input('Выбери максимальное возможное число: ')

    guess = input('Введите число: ')

    digit = randint(int(low), int(high))
    if guess == digit:
        print('Вы угадали, поздравляем!')
        print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
    else:
        print('------ Использовано попыток:', 1, '------')
    attempt_counter = 1

    while True:

        if not is_valid(guess):
            print('А может быть все-таки введем целое число от 1 до 100?')
            guess = input('Введите число: ')
            continue
        else:
            guess = int(guess)
            if guess < digit:
                print('Ваше число меньше загаданного, попробуйте еще разок')
            elif guess > digit:
                print('Ваше число больше загаданного, попробуйте еще разок')
            else:
                print('Вы угадали, поздравляем!')
                print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
                break

        guess = input('Введите число: ')
        attempt_counter += 1

        print('------ Использовано попыток:', attempt_counter, '------')
        print()

number_guessing_game()

question = input('Хочешь сыграть еще разок? (Да/Нет): ')

if question == 'Да' or question == 'да':
    number_guessing_game()
elif question == 'Нет' or question == 'нет':
    print('Хорошо, если что - игра всегда ждет тебя, хорошего настроения!))')
else:
    while question not in ['да', 'Да', 'нет', 'Нет']:
        question = input(
            'Не совсем тебя понимаю. Ответь, пожалуйста, '
            'Ты хочешь сыграть еще раз? (Да/Нет): '
            )
    if question == 'Да' or question == 'да':
        number_guessing_game()
    elif question == 'Нет' or question == 'нет':
        print('Хорошо, если что - игра всегда ждет тебя, хорошего настроения!))')
