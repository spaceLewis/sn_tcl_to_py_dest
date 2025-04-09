

import serial

class Modbus:
    def __init__(self, theSerialBaud):
        self.theSerialBaud = theSerialBaud
        self.serial_port = None

    def open_rs(self):
        print("Switching on serial interface...")
        while True:
            try:
                interface_number = input("Enter serial interface number: ")
                if self.serial_port is not None:
                    print("Serial port is already open.")
                    break
                self.serial_port = serial.Serial(interface_number, self.theSerialBaud)
                print(f"Serial port {interface_number} opened successfully.")
                break
            except serial.SerialException as e:
                print(f"Error opening serial port: {e}")

    def close_rs(self):
        if self.serial_port is not None:
            try:
                self.serial_port.close()
                print("Serial port closed successfully.")
                self.serial_port = None
            except serial.SerialException as e:
                print(f"Error closing serial port: {e}")
        else:
            print("Serial port is already closed.")