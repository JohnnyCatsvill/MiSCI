from functools import cache

from utils.constants import *
from enum import Enum


class CipherMode(Enum):
    Cipher = 0
    Decipher = 1

@cache
def r(index) -> int:
    if index == 1:
        return (1 * A + C) % MAX_KEY_LENGTH
    return (r(index - 1) * A + C) % MAX_KEY_LENGTH


def cipher(filename_in: str, filename_out: str, secret_key: bytes, mode: CipherMode):

    # guard to cut off situation when there are bad chars in key
    for ch_ord in secret_key:
        if ch_ord not in KEY_ALPHABET:
            raise Exception(f"KEY unsupported characters - '{ch_ord.to_bytes(BYTE_DEPTH, ENCODING_ENDIAN)}'")

    key = int(secret_key.decode(ENCODING_NAME))

    # opening files to be read / written in binary mode
    with open(filename_in, mode='rb') as f_in, \
            open(filename_out, mode='wb') as f_out:

        # preparing index for key, to know what part of key should be used in our ciphering
        key_ord = key
        key_val = r(key_ord)

        # reading input file 2 bytes per time
        while ch_byte := f_in.read(BYTE_DEPTH):
            # guard to cut off bad char before ciphering text
            if mode == CipherMode.Cipher and ch_byte not in TEXT_ALPHABET:
                raise Exception(f"TEXT unsupported characters - '{ch_byte.decode(ENCODING_NAME)}'")

            # taking char ordeal numbers and adding or subtracting them basing on mode
            ch_ord = int.from_bytes(ch_byte, ENCODING_ENDIAN)
            new_ord = ((ch_ord + key_val) if mode == CipherMode.Cipher else (ch_ord - key_val)) % M
            # creating new char of certain encoding
            new_byte = new_ord.to_bytes(BYTE_DEPTH, ENCODING_ENDIAN)

            # guard to cut off bad char after deciphering text
            if mode == CipherMode.Decipher and new_byte not in TEXT_ALPHABET:
                raise Exception(f"TEXT unsupported characters - '{new_byte.decode(ENCODING_NAME)}'")

            # writing char into output file
            f_out.write(new_byte)

            # incrementing key index, and zeroing index if it's runs out secret key boundary
            key_ord += 1
            key_val = r(key_ord)
