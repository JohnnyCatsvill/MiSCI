import sys
from utils.cipher import cipher, CipherMode
from utils.constants import ENCODING_NAME


def main():
    filename_in = sys.argv[1]
    filename_out = sys.argv[2]
    secret_key = sys.argv[3].encode(ENCODING_NAME)

    cipher(filename_in, filename_out, secret_key, CipherMode.Cipher)


if __name__ == '__main__':
    main()
