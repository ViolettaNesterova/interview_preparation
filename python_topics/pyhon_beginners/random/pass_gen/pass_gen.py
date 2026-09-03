from random import *

# Ждем ответ Да/Нет
def include_pass(variable, include_text):
    while variable not in variants_answer_yes and variable not in variants_answer_no:
        print()
        print('Не понял ваш ответ.')
        variable = input(f'Включать ли {include_text} в пароль (да/нет): ')


digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''
variants_answer_yes = ['да', 'Да', 'ДА']
variants_answer_no = ['нет', 'Нет', 'НЕТ']

# Ввод количества генераций пароля
number_pass = input('Введите необходимое количество генераций: ')
while not number_pass.isdigit():
    number_pass = input('Не понял вас. Введите необходимое количество генераций: ')

# Длина пароля
length_pass = input('Задайте длину пароля: ')
while not length_pass.isdigit():
    print()
    print('Не понял ваш ответ.')
    length_pass = input('Задайте длину пароля: ')

# Включать цифры в пароль
digits_pass = input('Включать ли цифры (1-9) в пароль (да/нет): ')
include_pass(digits_pass, 'цифры (1-9)')

# Включать прописные буквы в пароль
uppercase_letters_pass = input('Включать ли прописные буквы (A-Z) в пароль (да/нет): ')
include_pass(uppercase_letters_pass, 'прописные буквы (A-Z)')

# Включать строчные буквы в пароль
lowercase_letters_pass = input('Включать ли строчные буквы (a-z) в пароль (да/нет): ')
include_pass(lowercase_letters_pass, 'строчные буквы (a-z)')

# Включать символы в пароль
symbols_pass = input('Включать ли символы (!#$%&*+-=?@^_) в пароль (да/нет): ')
include_pass(symbols_pass, 'символы (!#$%&*+-=?@^_)')

# Исключить неоднозначные символы (il1Lo0O)
exclude_symbols_pass = input('Исключать ли неоднозначные символы (il1Lo0O) из пароля (да/нет): ')
while exclude_symbols_pass not in variants_answer_yes and exclude_symbols_pass not in variants_answer_no:
        print()
        print('Не понял ваш ответ.')
        variable = input(f'Исключать ли неоднозначные символы (il1Lo0O) из пароля (да/нет): ')

if digits_pass in variants_answer_yes:
     chars += digits

if uppercase_letters_pass in variants_answer_yes:
     chars += uppercase_letters

if lowercase_letters_pass in variants_answer_yes:
     chars += lowercase_letters

if symbols_pass in variants_answer_yes:
     chars += punctuation

if exclude_symbols_pass in variants_answer_yes:
     for sym in 'il1Lo0O':
        chars = chars.replace(sym, '')



'''
digits_pass = input('Включать ли цифры (1-9) в пароле (да/нет): ')
while digits_pass not in variants_answer_no and digits_pass not in variants_answer_yes:
    print()
    print('Не понял ваш ответ.')
    digits_pass = input('Включать ли цифры (1-9) в пароле (да/нет): ')

uppercase_letters_pass = input('Включать ли прописные буквы в пароле (да/нет): ')
while uppercase_letters_pass not in variants_answer_yes and uppercase_letters_pass not in variants_answer_no:
    print()
    print('Не понял ваш ответ.')
    uppercase_letters_pass = input('Включать ли прописные буквы в пароле (да/нет): ')

lowercase_letters_pass = input('Включать ли прописные буквы в пароле (да/нет): ')
while lowercase_letters_pass not in variants_answer_yes and lowercase_letters_pass not in variants_answer_no:
    print()
    print('Не понял ваш ответ.')
    uppercase_letters_pass = input('Включать ли прописные буквы в пароле (да/нет): ')
'''
