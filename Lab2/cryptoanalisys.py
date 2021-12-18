import sys
from utils.constants import *


def pairwise(iterable):  # i'll gladly find any other way to take 2 bytes per time, but we have what we have
    # "s -> (s0, s1), (s2, s3), (s4, s5), ..."
    a = iter(iterable)
    return zip(a, a)


def main():
    filename_in = sys.argv[1]

    # actual key 1294967296
    key_start = 0

    text_length = 0  # needed to make our distribution in percentile
    text = b""
    with open(filename_in, mode='rb') as f_in:  # read one time only, it takes too long to read file many times
        while ch := f_in.read(BYTE_DEPTH):
            text_length += 1
            text += ch

    best_similarity = -1
    best_key = 0
    while key_start < MAX_KEY_LENGTH:

        new_distribution = dict()
        key_index = key_start

        for ch1, ch2 in pairwise(text):
            # taking 2 bytes subtracting key_index and putting new char to new distribution
            old_byte = ch1.to_bytes(1, ENCODING_ENDIAN) + ch2.to_bytes(1, ENCODING_ENDIAN)
            new_ord = (int.from_bytes(old_byte, ENCODING_ENDIAN) - key_index) % M
            new_letter = new_ord.to_bytes(BYTE_DEPTH, ENCODING_ENDIAN).decode(ENCODING_NAME).upper()
            new_distribution[new_letter] = new_distribution.get(new_letter, 0) + 1

            key_index = (key_index + 1)
            if key_index >= MAX_KEY_LENGTH:
                # actually i don't know if this an error?
                raise Exception(f"runs out of key boundaries - '{MAX_KEY_LENGTH}'")

        # creating percentile distribution out of new distribution that we divide to text length
        new_percentile_distribution = {i: v / text_length for i, v in new_distribution.items()}

        # checking two distribution tables, if they are as close as can be
        similarity = 0
        for k, v in BASE_DISTRIBUTION.items():
            similarity += new_percentile_distribution.get(k, 0) - v

        # if we passed an peak 100 keys or more ago, break
        if best_similarity - 0.5 > similarity:
            print(f"There are key - '{best_key}'")
            break
        else:  # renewing best keys and best similarities
            best_key = key_start if similarity > best_similarity else best_key
            best_similarity = max(similarity, best_similarity)

        # nothing found, go checking next key
        key_start += 1

    else:  # well, we looked through all key length but not find any better key
        print(f"Not sure if its what we looking for but Best result - {best_key}")


if __name__ == '__main__':
    main()
