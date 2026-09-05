RU_LOWER = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
RU_UPPER = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

EN_LOWER = 'abcdefghijklmnopqrstuvwxyz'
EN_UPPER = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

direction_list = [
    'ш', 'д', 'шифрование', 'дешифрование'
    ]

direction_list_cipher = ['ш', 'шифрование']

lang_list = [
    'ru', 'eng', 'en', 'russian', 'english', 'ру', 'анг', 'англ', 'русский', 'рус'
    ]

ru_lang = [
    'ru', 'russian', 'ру', 'русский', 'рус'
]

eng_lang = [
    'en', 'eng', 'english', 'англ', 'английский', 'анг'
]

def shift_char(char, k, lower, upper):
    if char in lower:
        return lower[(lower.index(char) + k) % len(lower)]
    elif char in upper:
        return upper[(upper.index(char) + k) % len(upper)]
    else:
        return char


def deshift_char(char, k, lower, upper):
    if char in lower:
        return lower[(lower.index(char) - k) % len(lower)]
    elif char in upper:
        return upper[(upper.index(char) - k) % len(upper)]
    else:
        return char


def sentence_is_valid(sentence):
    return len(sentence.strip()) != 0


def shift_is_valid(shift):
    return shift.isdigit()


def direction_is_valid(direction):
    return direction.lower() in direction_list


def lang_is_valid(lang):
    return lang.lower() in lang_list

print('Привет!', 'Это простой шифратор-дешифратор по алгоритму Цезаря.')

sentence = input('Введите предложение: ')
while not sentence_is_valid(sentence):
    print('Некорректные данные.')
    sentence = input('Введите предложение: ')


shift = input('Введите сдвиг: ')
while not shift_is_valid(shift):
    print('Некорректные данные.')
    shift = input('Введите сдвиг: ')

shift = int(shift)


direction = input("Шифрование или дешифрование (ш/д)? ")
while not direction_is_valid(direction):
    print('Некорректные данные.')
    direction = input("Шифрование или дешифрование (ш/д)? ")


lang = input('Выберите язык (Ru/Eng): ')
while not lang_is_valid(lang):
    print('Некорректные данные.')
    lang = input("Выберите язык (Ru/Eng)")


chars = list(sentence)


for i in range(len(chars)):
    if direction.lower() in direction_list_cipher and lang.lower() in ru_lang: # если шифрование и русский
        chars[i] = shift_char(chars[i], shift, RU_LOWER, RU_UPPER)
    elif direction.lower() in direction_list_cipher and lang.lower() in eng_lang:
        chars[i] = shift_char(chars[i], shift, EN_LOWER, EN_UPPER)
    elif direction.lower() not in direction_list_cipher and lang.lower() in ru_lang:
        chars[i] = deshift_char(chars[i], shift, RU_LOWER, RU_UPPER)
    elif direction.lower() not in direction_list_cipher and lang.lower() in eng_lang:
        chars[i] = deshift_char(chars[i], shift, EN_LOWER, EN_UPPER)

print(''.join(chars))

