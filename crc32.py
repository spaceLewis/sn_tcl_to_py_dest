

import bytearray

crc32_table = None

def crc_table(width, polynomial):
    table = [0] * 256
    for i in range(256):
        crc = i
        for j in range(8):
            if crc & 1:
                crc = (crc >> 1) ^ polynomial
            else:
                crc >>= 1
        table[i] = crc
    return table

def crc(input_str, width, table, initial_value):
    crc = initial_value
    for byte in bytearray(input_str):
        crc = (crc >> 8) ^ table[(crc & 0xFF) ^ byte]
    return crc & 0xFFFFFFFF

def crc32(input_str):
    global crc32_table
    if input_str is None or len(input_str) == 0:
        raise ValueError("Input string cannot be empty or None")
    try:
        if crc32_table is None:
            crc32_table = crc_table(32, 0x04C11DB7)
        return crc(input_str, 32, crc32_table, 0xFFFFFFFF)
    except Exception as e:
        raise Exception("Error calculating CRC-32 checksum: " + str(e))

def main():
    input_str = "Hello, World!"
    crc32_checksum = crc32(input_str)
    print("CRC-32 checksum for '{}' is: {}".format(input_str, crc32_checksum))

if __name__ == "__main__":
    main()