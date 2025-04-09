

package crc

def reflect(v: int, b: int) -> int:
    if not isinstance(v, int) or not isinstance(b, int):
        raise TypeError("Both v and b must be integers")
    if b <= 0:
        raise ValueError("b must be a positive integer")
    if v.bit_length() > b:
        raise ValueError("v is too large for b bits")
    r = 0
    for i in range(b):
        if (v & (1 << i)):
            r |= (1 << (b - 1 - i))
    return r