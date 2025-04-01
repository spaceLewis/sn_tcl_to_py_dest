

import modbus
import pymodbus

def do_print_mode(mode):
    print(f"Mode: {mode}")

def do_print_error_text(error_text):
    print(f"Error Text: {error_text}")

def do_get_error_text(error_code):
    error_texts = {
        1: "Error 1",
        2: "Error 2",
        3: "Error 3"
    }
    return error_texts.get(error_code, "Unknown Error")

def print_proc_entry_info(proc_entry):
    print(f"Process Entry Info: {proc_entry}")

def do_print_win_error_text(error_code):
    error_texts = {
        1: "Windows Error 1",
        2: "Windows Error 2",
        3: "Windows Error 3"
    }
    print(f"Windows Error Text: {error_texts.get(error_code, 'Unknown Windows Error')}")

def show_status(status):
    print(f"Status: {status}")

def do_print_status(status):
    print(f"Status: {status}")

def do_print_modules(modules):
    print(f"Modules: {modules}")

def read_device_parameters(device_id):
    client = pymodbus.ModbusTcpClient(device_id)
    client.connect()
    result = client.read_holding_registers(0, 10)
    client.close()
    return result.registers

def print_device_parameters(device_id):
    parameters = read_device_parameters(device_id)
    print(f"Device Parameters: {parameters}")

def read_error_texts(device_id):
    client = pymodbus.ModbusTcpClient(device_id)
    client.connect()
    result = client.read_holding_registers(10, 10)
    client.close()
    return result.registers

def print_error_texts(device_id):
    error_texts = read_error_texts(device_id)
    print(f"Error Texts: {error_texts}")

def read_status(device_id):
    client = pymodbus.ModbusTcpClient(device_id)
    client.connect()
    result = client.read_holding_registers(20, 10)
    client.close()
    return result.registers

def print_status(device_id):
    status = read_status(device_id)
    print(f"Status: {status}")