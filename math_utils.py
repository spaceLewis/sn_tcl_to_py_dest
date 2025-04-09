

import random

def calculate_mean(values):
    if len(values) == 0:
        raise ValueError("Cannot calculate mean of an empty list")
    return sum(values) / len(values)

def get_smaller(a, b):
    return min(a, b)

def get_larger(a, b):
    return max(a, b)

def unsigned_to_signed(unsigned_value, bit_length):
    if not isinstance(bit_length, int) or bit_length <= 0:
        raise ValueError("Bit length must be a positive integer")
    if unsigned_value >= (1 << bit_length - 1):
        return unsigned_value - (1 << bit_length)
    else:
        return unsigned_value

def get_sign(value):
    if not isinstance(value, (int, float)):
        raise ValueError("Input value must be a number")
    if value < 0:
        return -1
    elif value > 0:
        return 1
    else:
        return 0

def is_even(value):
    if not isinstance(value, int):
        raise ValueError("Input value must be an integer")
    return value % 2 == 0

def is_odd(value):
    return not is_even(value)

def generate_random_number(min_value, max_value):
    if not isinstance(min_value, int) or not isinstance(max_value, int):
        raise ValueError("Min and max values must be integers")
    if min_value > max_value:
        raise ValueError("Min value must be less than or equal to max value")
    return random.randint(min_value, max_value)