

import sys
import argparse
import logging
import pymodbus
from pymodbus.exceptions import ModbusIOException, ModbusException

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def modtlread(args):
    try:
        # Create a Modbus client
        client = pymodbus.ModbusSerialClient(method='rtu', port=args.port, baudrate=args.baudrate, timeout=1)

        # Connect to the Modbus server
        client.connect()

        # Read servo drive objects
        result = client.read_holding_registers(args.address, args.count, unit=args.unit)

        # Close the Modbus client
        client.close()

        return result

    except ModbusIOException as e:
        logging.error(f"Modbus I/O error: {e}")
        return None

    except ModbusException as e:
        logging.error(f"Modbus error: {e}")
        return None

    except Exception as e:
        logging.error(f"Unknown error: {e}")
        return None

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='ModTlRead procedure')
    parser.add_argument('--port', help='Modbus port', required=True)
    parser.add_argument('--baudrate', help='Modbus baudrate', required=True, type=int)
    parser.add_argument('--address', help='Modbus address', required=True, type=int)
    parser.add_argument('--count', help='Number of registers to read', required=True, type=int)
    parser.add_argument('--unit', help='Modbus unit ID', required=True, type=int)

    args = parser.parse_args()

    if not 0 <= args.baudrate <= 115200:
        logging.error("Invalid baudrate. Must be between 0 and 115200.")
        sys.exit(1)

    if not 0 <= args.address <= 65535:
        logging.error("Invalid address. Must be between 0 and 65535.")
        sys.exit(1)

    if not 1 <= args.count <= 125:
        logging.error("Invalid count. Must be between 1 and 125.")
        sys.exit(1)

    if not 0 <= args.unit <= 247:
        logging.error("Invalid unit ID. Must be between 0 and 247.")
        sys.exit(1)

    result = modtlread(args)

    if result is None:
        logging.error("Error reading registers")
    elif result.isError():
        logging.error(f"Error: {result}")
    else:
        logging.info(f"Registers: {result.registers}")