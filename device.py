

import serial

class Device:
    def __init__(self, port, baudrate):
        self.port = port
        self.baudrate = baudrate
        self.serial = self._initialize_serial_connection()

    def _initialize_serial_connection(self):
        try:
            return serial.Serial(self.port, self.baudrate)
        except serial.SerialException as e:
            print(f"Error initializing serial connection: {e}")
            return None

    def mod_tl_read(self):
        try:
            data = self.serial.readline()
            return data.decode('utf-8')
        except serial.SerialException as e:
            print(f"Error reading from serial connection: {e}")
            return None

    def mod_tl_write(self, data):
        try:
            self.serial.write(data.encode('utf-8'))
        except serial.SerialException as e:
            print(f"Error writing to serial connection: {e}")

    def initialization(self):
        self.mod_tl_write(b'INIT\n')
        response = self.mod_tl_read()
        if response == 'INIT_OK\n':
            return True
        else:
            return False

    def parameter_identification(self):
        self.mod_tl_write(b'PARAM_ID\n')
        response = self.mod_tl_read()
        if response == 'PARAM_ID_OK\n':
            return True
        else:
            return False

    def default_values(self):
        self.mod_tl_write(b'DEFAULT_VAL\n')
        response = self.mod_tl_read()
        if response == 'DEFAULT_VAL_OK\n':
            return True
        else:
            return False

    def relay_configuration(self):
        self.mod_tl_write(b'RELAY_CONFIG\n')
        response = self.mod_tl_read()
        if response == 'RELAY_CONFIG_OK\n':
            return True
        else:
            return False

    def ATSCommandSwitch(self):
        self.mod_tl_write(b'ATS_CMD_SWITCH\n')
        response = self.mod_tl_read()
        if response == 'ATS_CMD_SWITCH_OK\n':
            return True
        else:
            return False

    def ATSBackToIniti(self):
        self.mod_tl_write(b'ATS_BACK_TO_INIT\n')
        response = self.mod_tl_read()
        if response == 'ATS_BACK_TO_INIT_OK\n':
            return True
        else:
            return False