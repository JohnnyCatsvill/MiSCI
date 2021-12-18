def chars(ch1: str, ch2: str):
    return "".join([chr(c) for c in range(ord(ch1), ord(ch2)+1)])


PS = "\r"
CR = "\n"
PUNCTUATION = " !\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
NUMBERS = chars("0", "9")
RUSSIAN = chars("а", "я") + chars("А", "Я") + "ёЁ"
ENGLISH = chars("a", "z") + chars("A", "Z")

BYTE_DEPTH = 1
ENCODING_NAME = "windows-1251"
ENCODING_ENDIAN = "little"

TEXT_ALPHABET = (PS + CR + PUNCTUATION + NUMBERS + RUSSIAN + ENGLISH).encode(ENCODING_NAME)
KEY_ALPHABET = (NUMBERS + RUSSIAN + ENGLISH).encode(ENCODING_NAME)
M = 2 ** (BYTE_DEPTH * 8)

MAX_KEY_LENGTH = 32
