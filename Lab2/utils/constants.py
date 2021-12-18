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

BYTE_DEPTH = 2
ENCODING_NAME = "UTF-16"
ENCODING_ENDIAN = "little"

TEXT_ALPHABET = BYTE_ORDER_MARK + (PS + CR + PUNCTUATION + NUMBERS + ENGLISH_BIG + ENGLISH_SMALL).encode(ENCODING_NAME)
KEY_ALPHABET = NUMBERS.encode(ENCODING_NAME)
M = 2 ** (BYTE_DEPTH * 8)

MAX_KEY_LENGTH = 2**32+1

BASE_DISTRIBUTION = {
    "A": 0.081,
    "B": 0.014,
    "C": 0.027,
    "D": 0.039,
    "E": 0.130,
    "F": 0.029,
    "G": 0.020,
    "H": 0.052,
    "I": 0.065,
    "J": 0.002,
    "K": 0.004,
    "L": 0.034,
    "M": 0.025,
    "N": 0.072,
    "O": 0.079,
    "P": 0.020,
    "R": 0.069,
    "S": 0.061,
    "T": 0.105,
    "U": 0.024,
    "V": 0.009,
    "W": 0.015,
    "X": 0.002,
    "Y": 0.019,
    "Z": 0.001,
}
