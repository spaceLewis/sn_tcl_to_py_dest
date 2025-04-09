

import ctypes
import time

# Dictionary to map device numbers to PLC register numbers
device_map = {
    1: 0x1000,
    2: 0x1001,
    3: 0x1002,
    4: 0x1003,
}

# Global variable to check break condition
break_condition = False

# Load the PLC library
plc_lib = ctypes.CDLL('./plc_lib.so')

# Define the PLC register data type
plc_reg_t = ctypes.c_uint16

# Define the PLC register pointer type
plc_reg_ptr_t = ctypes.POINTER(plc_reg_t)

# Define the PLC register array
plc_regs = (plc_reg_t * 10)()

# Initialize the PLC register array
for i in range(10):
    plc_regs[i] = 0

# Define the PLC register pointer
plc_reg_ptr = plc_reg_ptr_t(plc_regs)

# Function to control on/off
def ctrl_on_off(device_num, state):
    global break_condition
    if break_condition:
        return
    plc_reg_num = device_map[device_num]
    mask = 1 << (device_num - 1)
    if state:
        plc_lib.set_plc_reg(plc_reg_ptr, plc_reg_num, mask)
    else:
        plc_lib.clear_plc_reg(plc_reg_ptr, plc_reg_num, mask)

# Function to phase inversion
def phase_inversion(device_num):
    global break_condition
    if break_condition:
        return
    plc_reg_num = device_map[device_num]
    mask = 1 << (device_num - 1)
    plc_lib.toggle_plc_reg(plc_reg_ptr, plc_reg_num, mask)

# Function to load on/off
def load_on_off(device_num, state):
    global break_condition
    if break_condition:
        return
    plc_reg_num = device_map[device_num]
    mask = 1 << (device_num - 1)
    if state:
        plc_lib.set_plc_reg(plc_reg_ptr, plc_reg_num, mask)
    else:
        plc_lib.clear_plc_reg(plc_reg_ptr, plc_reg_num, mask)

# Function to wait for relay
def do_wait_for_relay(device_num):
    global break_condition
    if break_condition:
        return
    plc_reg_num = device_map[device_num]
    mask = 1 << (device_num - 1)
    while True:
        if plc_lib.get_plc_reg(plc_reg_ptr, plc_reg_num) & mask:
            break
        time.sleep(0.1)

# Function to wait for relay with wait time
def do_wait_for_relay_waittime(device_num, wait_time):
    global break_condition
    if break_condition:
        return
    plc_reg_num = device_map[device_num]
    mask = 1 << (device_num - 1)
    start_time = time.time()
    while True:
        if plc_lib.get_plc_reg(plc_reg_ptr, plc_reg_num) & mask:
            break
        if time.time() - start_time > wait_time:
            break
        time.sleep(0.1)

# Function to check relay
def check_relay(device_num):
    global break_condition
    if break_condition:
        return
    plc_reg_num = device_map[device_num]
    mask = 1 << (device_num - 1)
    return bool(plc_lib.get_plc_reg(plc_reg_ptr, plc_reg_num) & mask)

# Function to validate PLC register numbers
def validate_plc_reg_num(plc_reg_num):
    if plc_reg_num < 0x1000 or plc_reg_num > 0x1003:
        raise ValueError("Invalid PLC register number")

# Function to handle errors during interaction with PLC registers
def handle_plc_error(error_code):
    if error_code != 0:
        raise Exception("Error interacting with PLC register")

# Function to set PLC register
def set_plc_reg(plc_reg_ptr, plc_reg_num, mask):
    validate_plc_reg_num(plc_reg_num)
    error_code = plc_lib.set_plc_reg(plc_reg_ptr, plc_reg_num, mask)
    handle_plc_error(error_code)

# Function to clear PLC register
def clear_plc_reg(plc_reg_ptr, plc_reg_num, mask):
    validate_plc_reg_num(plc_reg_num)
    error_code = plc_lib.clear_plc_reg(plc_reg_ptr, plc_reg_num, mask)
    handle_plc_error(error_code)

# Function to toggle PLC register
def toggle_plc_reg(plc_reg_ptr, plc_reg_num, mask):
    validate_plc_reg_num(plc_reg_num)
    error_code = plc_lib.toggle_plc_reg(plc_reg_ptr, plc_reg_num, mask)
    handle_plc_error(error_code)

# Function to get PLC register
def get_plc_reg(plc_reg_ptr, plc_reg_num):
    validate_plc_reg_num(plc_reg_num)
    error_code, value = plc_lib.get_plc_reg(plc_reg_ptr, plc_reg_num)
    handle_plc_error(error_code)
    return value