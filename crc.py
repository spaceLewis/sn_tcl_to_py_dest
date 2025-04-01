

import argparse
import bytearray

def crc_calculate(data, initial_value):
    crc_value = initial_value
    crc_table = bytearray([0] * 256)
    for i in range(256):
        crc = i
        for _ in range(8):
            if crc & 1:
                crc = (crc >> 1) ^ 0x8C
            else:
                crc >>= 1
        crc_table[i] = crc
    for byte in bytearray(data):
        crc_value = crc_table[(crc_value ^ byte) & 0xFF]
    return crc_value

def crc_file(file_name, initial_value):
    with open(file_name, 'rb') as file:
        data = file.read()
    return crc_calculate(data, initial_value)

def main():
    parser = argparse.ArgumentParser(description='CRC checksum calculation tool')
    parser.add_argument('input', help='input string or file name')
    parser.add_argument('-f', '--file', action='store_true', help='input is a file name')
    parser.add_argument('-i', '--initial', type=int, default=0, help='initial CRC value')
    args = parser.parse_args()

    if args.initial < 0 or args.initial > 255:
        print("Invalid initial CRC value")
        return

    if args.file:
        try:
            crc_value = crc_file(args.input, args.initial)
        except FileNotFoundError:
            print("File not found")
            return
    else:
        crc_value = crc_calculate(args.input, args.initial)

    print(f'CRC value: {crc_value}')

if __name__ == '__main__':
    main()