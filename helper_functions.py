

import ctypes

plc_registers = {
    1: 0x1000,
    2: 0x2000,
    3: 0x3000,
    4: 0x4000,
}

break_condition = False

def get_plc_register(device_number):
    if device_number not in plc_registers:
        raise ValueError("Device number not found in plc_registers")
    return plc_registers[device_number]

def read_plc_register(register_number):
    try:
        return ctypes.c_uint16.from_address(register_number).value
    except Exception as e:
        raise Exception(f"Error reading PLC register: {e}")

def create_mask(bit_position, bit_value):
    if not isinstance(bit_position, int) or not isinstance(bit_value, int):
        raise ValueError("Bit position and bit value must be integers")
    if bit_position < 0 or bit_position > 15:
        raise ValueError("Bit position must be between 0 and 15")
    if bit_value not in [0, 1]:
        raise ValueError("Bit value must be 0 or 1")
    mask = 1 << bit_position
    if bit_value == 0:
        mask = ~mask
    return mask

def write_plc_register(register_number, value):
    try:
        ctypes.cast(register_number, ctypes.POINTER(ctypes.c_uint16))[0] = value
    except Exception as e:
        raise Exception(f"Error writing to PLC register: {e}")

def check_break():
    global break_condition
    return break_condition