import sys
from utils.cipher import cipher, CipherMode


def main():
    filename_in = sys.argv[1]
    filename_out = sys.argv[2]
    secret_key = sys.argv[3].encode("windows-1251")

    cipher(filename_in, filename_out, secret_key, CipherMode.Decipher)


if __name__ == '__main__':
    main()
