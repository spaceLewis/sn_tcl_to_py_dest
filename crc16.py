

import bytearray

crc16_table = None

def crc_table(width, polynomial):
    if not isinstance(width, int) or not isinstance(polynomial, int):
        raise ValueError("Width and polynomial must be integers")
    if width <= 0 or polynomial <= 0:
        raise ValueError("Width and polynomial must be positive")
    table = bytearray(width * 256)
    for i in range(256):
        crc = i
        for j in range(width):
            if crc & 1:
                crc = (crc >> 1) ^ polynomial
            else:
                crc >>= 1
        table[i] = crc
    return table

def crc(input_string, width, table, initial_value):
    if not isinstance(input_string, bytearray) or not isinstance(width, int) or not isinstance(table, bytearray) or not isinstance(initial_value, int):
        raise ValueError("Invalid input types")
    if len(input_string) == 0:
        raise ValueError("Input string cannot be empty")
    crc = initial_value
    for byte in input_string:
        crc = (crc >> 8) ^ table[(crc & 0xFF) ^ byte]
    return crc

def crc16(input_string, initial_value=0xFFFF):
    global crc16_table
    if input_string is None:
        raise ValueError("Input string cannot be None")
    if not isinstance(input_string, bytearray):
        input_string = bytearray(input_string, 'utf-8')
    if crc16_table is None:
        crc16_table = crc_table(16, 0x1021)
    try:
        return crc(input_string, 16, crc16_table, initial_value)
    except Exception as e:
        raise Exception("Error calculating CRC-16 checksum: {}".format(str(e)))