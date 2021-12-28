# 1222412

# I. Тип криптографического преобразования:
# 1) схема Цезаря;

# II. Разрядность слова сообщения:
# 2) 16 бит;

# III. Тип основного ключа:
# 2) линейный конгруэнтный.

# IV. Метод криптоанализа:
# 2) корреляционный.

# V. Ограничения на алфавит сообщения:
# 4) ограничения только на вероятность встречаемости.

# VI. Ограничения на алфавит основного ключа
# 1) нет;

# VII. Ограничения на линейную конгруэнтную последовательность (на модуль ЛКДПСЧ)
# 2) 2^32+1;


def chars(ch1: str, ch2: str):
    return "".join([chr(c) for c in range(ord(ch1), ord(ch2)+1)])


PS = "\r"
CR = "\n"
PUNCTUATION = " !\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
NUMBERS = chars("0", "9")
RUSSIAN_BIG = chars("А", "Я") + "Ё"
RUSSIAN_SMALL = chars("а", "я") + "ё"
ENGLISH_BIG = chars("A", "Z")
ENGLISH_SMALL = chars("a", "z")
BYTE_ORDER_MARK = b'\xff\xfe'

BYTE_DEPTH = 1
ENCODING_NAME = "windows-1251"
ENCODING_ENDIAN = "little"

TEXT_ALPHABET = BYTE_ORDER_MARK + (PS + CR + PUNCTUATION + NUMBERS + ENGLISH_BIG + ENGLISH_SMALL).encode(ENCODING_NAME)
KEY_ALPHABET = NUMBERS.encode(ENCODING_NAME)
M = 2 ** (BYTE_DEPTH * 8)
A = 3
C = 0

MAX_KEY_LENGTH = 2**32+1

SEARCH_CAP = 200