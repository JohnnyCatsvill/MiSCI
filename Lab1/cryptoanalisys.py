import sys
from utils.constants import *


def break_with_certain_length(filename_in: str, breaking_index: int, key_length: int,
                              alphabet: set[int]) -> bytes | int:
    with open(filename_in, mode='rb') as f_in:
        old_set = alphabet
        key_index = 0
        while ch := f_in.read(BYTE_DEPTH):
            if key_index == breaking_index:  # reading until we find working index

                # get new set out of all possibilities of subtracting ciphered letter and whole alphabet
                # and checking if new letter still belong to our alphabet
                new_set = set((ord(ch) - i) % M for i in alphabet if (ord(ch) - i) % M in alphabet)

                old_set = new_set & old_set  # inner joining new and old sets
                if not old_set:
                    break   # well out set is empty, nothing to do here
            key_index = (key_index + 1) % key_length

        if len(old_set) == 1:  # should be exactly one
            return old_set.pop().to_bytes(BYTE_DEPTH, ENCODING_ENDIAN)
        else:  # our set not comes down, it probably empty
            return 1


def main():
    filename_in = sys.argv[1]
    A = set(i for i in TEXT_ALPHABET + KEY_ALPHABET)  # it looks like set of integers, because its easier to work with

    key_length = 1
    key = b""

    while key_length < MAX_KEY_LENGTH:
        while key_length < MAX_KEY_LENGTH:
            res = break_with_certain_length(filename_in, 0, key_length, A)  # getting or byte letter of integer error

            if type(res) == bytes:  # if we get result we wanted to (only one byte, not integer error)
                key += res  # add possible part_of_key to key
                break  # breaking out of our while, we probably find exact length of key

            key_length += 1  # well bad res, trying other length

        if key_length < MAX_KEY_LENGTH:  # if breaking out of while and key_length still in searching range
            for key_index in range(1, key_length):  # finding other parts of key
                res = break_with_certain_length(filename_in, key_index, key_length, A)

                if type(res) == bytes:  # if we still getting good result
                    key += res  # adding them to key
                else:  # good try, key could be here, but we cant break this exact char
                    print(f"Not valid key - '{key.decode(ENCODING_NAME)}'")
                    break  # running everything again with new key_length

            else:  # we find all parts of key!
                print(f"Key is - '{key.decode(ENCODING_NAME)}'")
                break  # no need to go deeper

    else:  # well, we looked through all key length but not find any valid key
        print("Well no key for today")


if __name__ == '__main__':
    main()
