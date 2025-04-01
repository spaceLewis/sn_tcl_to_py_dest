

import bytearray

crc_ccitt_table = None

def crc_table(width, polynomial):
    table = bytearray(width << 8)
    for i in range(256):
        crc = i
        for j in range(8):
            if crc & 1:
                crc = (crc >> 1) ^ polynomial
            else:
                crc >>= 1
        table[i] = crc
    return table

def crc_ccitt(input_string, width=16, table=None, initial_value=0xFFFF):
    global crc_ccitt_table
    if input_string is None or len(input_string) == 0:
        raise ValueError("Input string cannot be empty or None")
    if width != 16:
        raise ValueError("Width must be 16 for CRC-CCITT")
    if polynomial != 0x1021:
        raise ValueError("Polynomial must be 0x1021 for CRC-CCITT")
    try:
        if crc_ccitt_table is None:
            crc_ccitt_table = crc_table(width, 0x1021)
        if table is None:
            table = crc_ccitt_table
        crc = initial_value
        for byte in bytearray(input_string):
            crc = (crc >> 8) ^ table[(crc & 0xFF) ^ byte]
        return crc
    except Exception as e:
        raise Exception("Error calculating CRC-CCITT checksum: " + str(e))