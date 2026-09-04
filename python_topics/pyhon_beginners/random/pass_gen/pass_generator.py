import random


DIGITS = '0123456789'
LOWERCASE_LETTERS = 'abcdefghijklmnopqrstuvwxyz'
UPPERCASE_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
PUNCTUATION = '!#$%&*+-=?@^_'

chars = ''

variants_answer_yes = ['да', 'Да', 'ДА']
variants_answer_no = ['нет', 'Нет', 'НЕТ']

# Список групп используемых элементов
selected_chars = []


# Проверка ответа Да/Нет
def include_pass(variable, include_text):
    while variable not in variants_answer_yes and variable not in variants_answer_no:
        print()
        print('Не понял ваш ответ.')
        variable = input(f'Включать ли {include_text} в пароль (да/нет): ')

    return variable


# Наполнение списка selected_chars и строки chars
def filling_chars(variable, char, chars):
    if variable in variants_answer_yes:
        selected_chars.append(char)
        chars += char
    return chars


def generate_password(length, chars, selected_chars):

    while length < len(selected_chars):
        print(
            'С выбранным набором категорий элементов '
            f'минимальная допустимая длина {len(selected_chars)}'
        )
        length = input('Введите корректную длину пароля: ')
    length = int(length)

    password = ''

    for categories in selected_chars:
        password += random.choice(categories)

    for _ in range(length - len(selected_chars)):
        password += random.choice(chars)

    password = list(password)
    random.shuffle(password)

    return ''.join(password)


# Количество паролей
number_pass = input('Введите необходимое количество паролей: ')

while not number_pass.isdigit():
    print()
    print('Не смог идентифицировать ваш ответ.')
    number_pass = input('Введите необходимое количество паролей: ')

number_pass = int(number_pass)


# Длина пароля
length_pass = input('Введите длину пароля: ')

while not length_pass.isdigit():
    print()
    print('Не смог идентифицировать ваш ответ.')
    length_pass = input('Задайте длину пароля: ')

length_pass = int(length_pass)

selected_chars = []

while len(selected_chars) == 0:
    # Цифры
    digits_pass = input('Включать ли цифры (1-9) в пароль (да/нет): ')
    digits_pass = include_pass(digits_pass, 'цифры (1-9)')

    # Прописные буквы
    uppercase_letters_pass = input('Включать ли прописные буквы (A-Z) в пароль (да/нет): ')
    uppercase_letters_pass = include_pass(uppercase_letters_pass, 'прописные буквы (A-Z)')

    # Строчные буквы
    lowercase_letters_pass = input('Включать ли строчные буквы (a-z) в пароль (да/нет): ')
    lowercase_letters_pass = include_pass(lowercase_letters_pass, 'строчные буквы (a-z)')

    # Символы
    symbols_pass = input('Включать ли символы (!#$%&*+-=?@^_) в пароль (да/нет): ')
    symbols_pass = include_pass(symbols_pass, 'символы (!#$%&*+-=?@^_)')

    # Исключить неоднозначные символы (il1Lo0O)
    exclude_symbol_pass = input(
        'Исключить ли неоднозначные символы '
        '(il1Lo0O) из пароля (да/нет): '
        )
    while exclude_symbol_pass not in variants_answer_yes and exclude_symbol_pass not in variants_answer_no:
        print()
        print('Не понял ваш ответ.')
        exclude_symbol_pass = input(f'Исключить ли неоднозначные символы (il1Lo0O) из пароля (да/нет): ')

    chars = filling_chars(digits_pass, DIGITS, chars)
    chars = filling_chars(uppercase_letters_pass, UPPERCASE_LETTERS, chars)
    chars = filling_chars(lowercase_letters_pass, LOWERCASE_LETTERS, chars)
    chars = filling_chars(symbols_pass, PUNCTUATION, chars)

    if len(selected_chars) == 0:
        print()
        print('⚠️ Необходимо выбрать хотя бы одну категорию символов.')


if exclude_symbol_pass in variants_answer_yes:
    for char in 'il1Lo0O':
        if char in chars:
            chars = chars.replace(char, '')

    for index in range(len(selected_chars)):
        for char in 'il1Lo0O':
            if char in selected_chars[index]:
                selected_chars[index] = selected_chars[index].replace(char, '')

for i in range(1, number_pass + 1):
    print()
    print('🔴', 'Пароль №', i, '   -------    ', generate_password(length_pass, chars, selected_chars))





