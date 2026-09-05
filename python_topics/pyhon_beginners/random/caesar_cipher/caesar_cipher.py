RU_LOWER = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
RU_UPPER = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

EN_LOWER = 'abcdefghijklmnopqrstuvwxyz'
EN_UPPER = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Допустимые варианты ввода направления шифрования
DIRECTION_LIST = ['ш', 'д', 'шифрование', 'дешифрование']
DIRECTION_LIST_CIPHER = ['ш', 'шифрование']

# Допустимые варианты ввода языка
RU_LANG = ['ru', 'russian', 'ру', 'русский', 'рус']
ENG_LANG = ['en', 'eng', 'english', 'англ', 'английский', 'анг']
LANG_LIST = RU_LANG + ENG_LANG

def shift_char(char, k, lower, upper):
    """Сдвигает символ char на k позиций вперёд по алфавиту.

    Регистр сохраняется. Символы, отсутствующие в алфавите
    (пробелы, знаки препинания, цифры), возвращаются без изменений.
    """
    if char in lower:
        return lower[(lower.index(char) + k) % len(lower)]
    elif char in upper:
        return upper[(upper.index(char) + k) % len(upper)]
    else:
        return char


def deshift_char(char, k, lower, upper): 
    """Сдвигает символ char на k позиций назад по алфавиту (дешифрование)."""
    if char in lower:
        return lower[(lower.index(char) - k) % len(lower)]
    elif char in upper:
        return upper[(upper.index(char) - k) % len(upper)]
    else:
        return char


def sentence_is_valid(sentence): 
    """Предложение валидно, если оно не пустое и не состоит из пробелов."""
    return len(sentence.strip()) != 0


def shift_is_valid(shift):
    """Сдвиг валиден, если это неотрицательное целое число."""
    return shift.isdigit()


def direction_is_valid(direction):
    """Проверяет, что направление введено корректно."""
    return direction.lower() in DIRECTION_LIST


def lang_is_valid(lang):
    """Проверяет, что язык введён корректно."""
    return lang.lower() in LANG_LIST

print('Привет!', 'Это простой шифратор-дешифратор по алгоритму Цезаря.')

# Ввод и проверка предложения
sentence = input('Введите предложение: ')
while not sentence_is_valid(sentence):
    print('Некорректные данные.')
    sentence = input('Введите предложение: ')


# Ввод и проверка сдвига
shift = input('Введите сдвиг: ')
while not shift_is_valid(shift):
    print('Некорректные данные.')
    shift = input('Введите сдвиг: ')
shift = int(shift)


# Ввод и проверка направления
direction = input("Шифрование или дешифрование (ш/д)? ")
while not direction_is_valid(direction):
    print('Некорректные данные.')
    direction = input("Шифрование или дешифрование (ш/д)? ")


# Ввод и проверка языка
lang = input('Выберите язык (Ru/Eng): ')
while not lang_is_valid(lang):
    print('Некорректные данные.')
    lang = input("Выберите язык (Ru/Eng): ")


chars = list(sentence)


for i in range(len(chars)):
    if direction.lower() in DIRECTION_LIST_CIPHER and lang.lower() in RU_LANG: # если шифрование и русский
        chars[i] = shift_char(chars[i], shift, RU_LOWER, RU_UPPER)
    elif direction.lower() in DIRECTION_LIST_CIPHER and lang.lower() in ENG_LANG:
        chars[i] = shift_char(chars[i], shift, EN_LOWER, EN_UPPER)
    elif direction.lower() not in DIRECTION_LIST_CIPHER and lang.lower() in RU_LANG:
        chars[i] = deshift_char(chars[i], shift, RU_LOWER, RU_UPPER)
    elif direction.lower() not in DIRECTION_LIST_CIPHER and lang.lower() in ENG_LANG:
        chars[i] = deshift_char(chars[i], shift, EN_LOWER, EN_UPPER)

print(''.join(chars))

