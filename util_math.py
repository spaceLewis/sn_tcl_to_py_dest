

import random

def doMeanValue(values):
    return sum(values) / len(values)

def min(values):
    return min(values)

def max(values):
    return max(values)

def MakeCRC(data):
    crc = 0xFFFF
    for byte in data:
        crc = (crc >> 8) ^ (byte ^ (crc & 0xFF))
    return crc

def MakeCRC_word(data):
    if not isinstance(data, list) or not all(isinstance(word, int) for word in data):
        raise ValueError("Input data must be a list of words")
    crc = 0xFFFF
    for word in data:
        crc = (crc >> 8) ^ (word ^ (crc & 0xFF))
    return crc

def UINT08_TO_INT08(value):
    if value > 127:
    return value - 256
else:
    return value

def UINT_TO_INT(value):
    if value > 2147483647:
        return value - 4294967296
    else:
        return value

def UDINT_TO_DINT(value):
    if value > 4294967295:
        return value - 4294967296
    else:
        return value

def sign(value):
    if not isinstance(value, int):
        raise ValueError("Input value must be an integer")
    if value < 0:
        return -1
    elif value > 0:
        return 1
    else:
        return 0

def even(value):
    return value % 2 == 0

def odd(value):
    return value % 2 != 0

def generateRandom(value):
    return random.randint(0, value)

def WordShiftZeroL(value, shift):
    if shift > 16:
        raise ValueError("Shift value cannot be greater than 16")
    return (value << shift) & 0xFFFF