

import socket
import struct

class ModbusTCP:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.MBTCPCom = {'host': host, 'port': port}
        self.MBTCPioCom = {'host': host, 'port': port}
        self.sock = None

    def connect(self):
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.connect((self.host, self.port))
        except socket.error as e:
            print(f"Error connecting to {self.host}:{self.port}: {e}")
            return False
        return True

    def execute_command(self, command):
        try:
            self.sock.sendall(command)
            response = self.sock.recv(1024)
            if len(response) < 6:
                print("Invalid response from Modbus TCP device")
                return None
            return response
        except socket.error as e:
            print(f"Error sending or receiving data: {e}")
            return None

    def close(self):
        if self.sock:
            self.sock.close()
            self.sock = None

def main():
    try:
        modbus_tcp = ModbusTCP('localhost', 1700)
        if not modbus_tcp.connect():
            return
        command = struct.pack('>HH', 1, 2)
        response = modbus_tcp.execute_command(command)
        if response:
            print(response)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        modbus_tcp.close()

if __name__ == "__main__":
    main()