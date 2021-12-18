# I. Тип криптографического преобразования:
# 1) схема Цезаря;

# II. Разрядность слова сообщения:
# 1) 8 бит;

# III. Тип основного ключа:
# 1) периодический;

# IV. Метод криптоанализа:
# 1) метод сужения;

# V. Ограничения на алфавит сообщения:
# 1) перевод строки(ПС), возврат каретки(ВК), знаки препинания(ЗП), цифры(Ц), русские буквы альтернативной кодировки;

# VI. Ограничения на алфавит основного ключа
# 4) Ц, английские и русские в альтернативной кодировке заглавные буквы.

# VII. Ограничения на линейную конгруэнтную последовательность (на модуль ЛКДПСЧ)
# 8) нет.



def chars(ch1: str, ch2: str):
    return "".join([chr(c) for c in range(ord(ch1), ord(ch2)+1)])


PS = "\r"
CR = "\n"
PUNCTUATION = " !\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
NUMBERS = chars("0", "9")
RUSSIAN_BIG = chars("А", "Я") + "Ё"
RUSSIAN_SMALL = chars("а", "я") + "ё"
ENGLISH_BIG = chars("A", "Z")
ENGLISH_SMALL = chars("A", "Z")

BYTE_DEPTH = 1
ENCODING_NAME = "windows-1251"
ENCODING_ENDIAN = "little"

TEXT_ALPHABET = (PS + CR + PUNCTUATION + NUMBERS + RUSSIAN_BIG + RUSSIAN_SMALL).encode(ENCODING_NAME)
KEY_ALPHABET = (NUMBERS + RUSSIAN_BIG + ENGLISH_BIG).encode(ENCODING_NAME)
M = 2 ** (BYTE_DEPTH * 8)

MAX_KEY_LENGTH = 32
