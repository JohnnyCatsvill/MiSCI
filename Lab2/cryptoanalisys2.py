import math
import sys
from functools import cache
from utils.constants import *


def sum(start, end, j, a, r, function) -> int:
    i = start
    res = 0
    while i <= end:
        res += function(i, j, a, r)
        i += 1
    return res

@cache  # сохраняет значения функции в память, чтобы не рассчитывать их заново
def r(index)-> int:
    if index == 1:
        return (1*A+C) % MAX_KEY_LENGTH
    return (r(index-1) * A + C) % MAX_KEY_LENGTH


def main():
    filename_in = sys.argv[1]

    # actual key 1
    start = 1
    j = start
    c = []

    n = 0  # length of file
    a = []
    with open(filename_in, mode='rb') as f_in:  # read one time only, it takes too long to read file many times
        while ch := f_in.read(BYTE_DEPTH):
            n += 1
            a.append(int.from_bytes(ch, ENCODING_ENDIAN))

    while j < SEARCH_CAP:
        sum_ar = sum(0, n-1, j, a, r, lambda i, j, a, r: r(i+j) * a[i])
        sum_a = sum(0, n-1, j, a, r, lambda i, j, a, r: a[i])
        sum_r = sum(0, n-1, j, a, r, lambda i, j, a, r: r(i+j))
        sum_a2 = sum(0, n-1, j, a, r, lambda i, j, a, r: a[i]**2)
        sum_r2 = sum(0, n-1, j, a, r, lambda i, j, a, r: r(i+j)**2)

        new_c = ((n * sum_ar) - (sum_a * sum_r)) / math.sqrt((n * sum_a2 - sum_a**2)*(n * sum_r2 - sum_r**2))
        c.append(new_c)
        j += 1

    peak_val = min(c)
    peak_index = c.index(peak_val)

    print("Пиковое значение:", peak_val)
    print("Индекс ключа", peak_index + start)
    print()
    print(c)


if __name__ == '__main__':
    main()
