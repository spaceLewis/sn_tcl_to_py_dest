

import usb.core
import usb.util
import os

class FileManager:
    def __init__(self):
        self.session_handle = None

    def file_manager_open_session(self):
        self.session_handle = usb.core.find(idVendor=0x03EB, idProduct=0x6124)
        if self.session_handle is None:
            raise ValueError('Device not found')
        return self.session_handle

    def file_manager_get_file(self, file_path):
        if self.session_handle is None:
            raise ValueError('Session not opened')
        if not os.path.isfile(file_path):
            raise ValueError('Invalid file path')
        try:
            with open(file_path, 'rb') as file:
                file_contents = file.read()
            return file_contents
        except Exception as e:
            raise ValueError('Error reading file: ' + str(e))

    def file_manager_dump_hex_to_file(self, file_path, hex_data):
        if self.session_handle is None:
            raise ValueError('Session not opened')
        if not os.path.isdir(os.path.dirname(file_path)):
            raise ValueError('Invalid file path')
        try:
            with open(file_path, 'wb') as file:
                file.write(bytearray.fromhex(hex_data))
        except Exception as e:
            raise ValueError('Error writing file: ' + str(e))