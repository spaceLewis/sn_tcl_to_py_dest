

import csv
import modbus_tk
import modbus_tk.defines as cst
import modbus_tk.modbus_tcp as modbus_tcp
import csv_util

def main():
    try:
        # Modbus Communication Logic
        master = modbus_tcp.TcpMaster()
        master.set_timeout(5.0)
        master.set_verbose(True)
        master.open("127.0.0.1", 1700)

        # Validate the Modbus connection
        if not master.is_open():
            print("Modbus connection failed")
            return

        # Read data from a Modbus device
        data = master.execute(1, cst.READ_HOLDING_REGISTERS, 0, 10)

        # Close the connection
        master.close()

        # CSV File Management
        csv_file = "example.csv"
        csv_data = csv_util.read_csv(csv_file)

        # Manipulate CSV files
        csv_util.manipulate_csv(csv_data)

        # Compare CSV files
        csv_util.compare_csv(csv_data, csv_util.read_csv("example2.csv"))

        # Console Application
        print("Modbus data:", data)
        print("CSV data:", csv_data)

        # Call functions implemented in csv_util.py
        csv_util.example_function()

    except Exception as e:
        print("Error:", str(e))

if __name__ == "__main__":
    main()