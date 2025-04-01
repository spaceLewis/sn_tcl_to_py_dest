

import bytearray

def crc_table(poly, width):
    if not isinstance(poly, int) or not isinstance(width, int):
        raise ValueError("poly and width must be integers")
    if width < 1 or width > 32:
        raise ValueError("width must be between 1 and 32")
    if poly < 1 or poly > (1 << width) - 1:
        raise ValueError("poly must be between 1 and 2^width - 1")

    table = bytearray(width * 256)
    mask = (1 << width) - 1
    top = 1 << (width - 1)
    for i in range(256):
        crc = i
        for _ in range(8):
            if crc & top:
                crc = (crc << 1) ^ poly
            else:
                crc <<= 1
        table[i] = crc & mask
    return table

CRC_POLYNOMIALS = {
    "CRC-8": 0x1D,
    "CRC-16": 0x1021,
    "CRC-32": 0x04C11DB7
}

CRC_TABLES = {
    "CRC-8": crc_table(CRC_POLYNOMIALS["CRC-8"], 8),
    "CRC-16": crc_table(CRC_POLYNOMIALS["CRC-16"], 16),
    "CRC-32": crc_table(CRC_POLYNOMIALS["CRC-32"], 32)
}