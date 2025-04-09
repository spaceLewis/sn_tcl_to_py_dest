

package modbus

import logging
from pymodbus.client.sync import ModbusTcpClient
from pymodbus.exceptions import ModbusIOException

theDebugFlagObj = logging.getLogger('modbus')
DevAdr = {}
ActDev = None
BreakPoint = False

class ModbusException(Exception):
    pass

class ModbusConnectionException(ModbusException):
    pass

class ModbusTimeoutException(ModbusException):
    pass

class ModbusReadException(ModbusException):
    pass

class ModbusDevice:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.client = None
        self.timeout = 1.0

    def open(self):
        try:
            self.client = ModbusTcpClient(self.host, self.port)
            self.client.connect()
        except ModbusIOException as e:
            raise ModbusConnectionException(f"Failed to connect to Modbus device: {e}")

    def close(self):
        if self.client:
            self.client.close()

    def set_timeout(self, timeout):
        if self.client:
            self.timeout = timeout
            self.client.timeout = timeout

    def get_timeout(self):
        return self.timeout

    def read(self, address, count):
        try:
            result = self.client.read_holding_registers(address, count)
            return result.registers
        except ModbusIOException as e:
            raise ModbusReadException(f"Failed to read from Modbus device: {e}")

def ModTlReadIntern(device, address, count):
    try:
        return device.read(address, count)
    except ModbusReadException as e:
        theDebugFlagObj.error(f"Error reading from Modbus device: {e}")
        return None

def validate_device_address(address):
    if address not in DevAdr:
        raise ModbusException(f"Invalid device address: {address}")

def validate_active_device(device):
    if device != ActDev:
        raise ModbusException(f"Invalid active device: {device}")