

package modbus

import logging

class ModbusException(Exception):
    def __init__(self, message):
        if not message:
            message = "An unknown error occurred during Modbus communication"
        super().__init__(message)
        logging.error(message)

class ModbusTimeoutException(ModbusException):
    def __init__(self, message):
        if not message:
            message = "A timeout occurred during Modbus communication"
        super().__init__(message)