

import os
import time
import logging
from TlTestCase import TlTestCase
import modbus_tk
import modbus_tk.defines as cst
from modbus_tk import modbus_rtu
import serial
import subprocess
import json

class Utils:
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def clear_tower_before_night(self):
        self.logger.info("Clearing tower before night")
        # implement clearing tower before night functionality
        subprocess.run(["/usr/bin/clear_tower_before_night.sh"])

    def init_database_log_campaign_header(self):
        self.logger.info("Initializing database log campaign header")
        # implement initializing database log campaign header functionality
        subprocess.run(["/usr/bin/init_database_log_campaign_header.sh"])

    def reset_wago_digital_outputs(self):
        self.logger.info("Resetting WAGO digital outputs")
        # implement resetting WAGO digital outputs functionality
        master = modbus_rtu.RtuMaster(serial.Serial('COM1', 19200, timeout=1))
        master.execute(1, cst.WRITE_SINGLE_REGISTER, 0x0000, output_value=0x0000)

    def set_sto_management_for_cip_safety_firmware(self):
        self.logger.info("Setting STO management for CIP safety firmware")
        # implement setting STO management for CIP safety firmware functionality
        subprocess.run(["/usr/bin/set_sto_management_for_cip_safety_firmware.sh"])

    def get_device_features(self):
        self.logger.info("Getting device features")
        # implement getting device features functionality
        with open("device_features.json", "r") as file:
            return json.load(file)

    def get_system_features(self):
        self.logger.info("Getting system features")
        # implement getting system features functionality
        with open("system_features.json", "r") as file:
            return json.load(file)

    def set_plc_power_supply(self):
        self.logger.info("Setting PLC power supply")
        # implement setting PLC power supply functionality
        subprocess.run(["/usr/bin/set_plc_power_supply.sh"])

    def set_switch_power_supply(self):
        self.logger.info("Setting switch power supply")
        # implement setting switch power supply functionality
        subprocess.run(["/usr/bin/set_switch_power_supply.sh"])

    def wait_for_ping_response(self):
        self.logger.info("Waiting for ping response")
        # implement waiting for ping response functionality
        subprocess.run(["/usr/bin/wait_for_ping_response.sh"])

    def open_modbus_connection(self):
        self.logger.info("Opening Modbus connection")
        # implement opening Modbus connection functionality
        master = modbus_rtu.RtuMaster(serial.Serial('COM1', 19200, timeout=1))
        return master

    def read_object_from_device(self, master, address):
        self.logger.info("Reading object from device")
        # implement reading object from device functionality
        return master.execute(1, cst.READ_HOLDING_REGISTERS, address, 1)

    def print_object_from_device(self, object):
        self.logger.info("Printing object from device")
        # implement printing object from device functionality
        print(object)

    def switch_on_device(self, master, address):
        self.logger.info("Switching on device")
        # implement switching on device functionality
        master.execute(1, cst.WRITE_SINGLE_REGISTER, address, output_value=0x0001)

    def switch_off_device(self, master, address):
        self.logger.info("Switching off device")
        # implement switching off device functionality
        master.execute(1, cst.WRITE_SINGLE_REGISTER, address, output_value=0x0000)

    def check_device_version(self, master, address):
        self.logger.info("Checking device version")
        # implement checking device version functionality
        return master.execute(1, cst.READ_HOLDING_REGISTERS, address, 1)

    def read_configuration_values(self):
        self.logger.info("Reading configuration values")
        # implement reading configuration values functionality
        with open("configuration_values.json", "r") as file:
            return json.load(file)

    def set_command_interface(self):
        self.logger.info("Setting command interface")
        # implement setting command interface functionality
        subprocess.run(["/usr/bin/set_command_interface.sh"])

    def read_atv_parameter_file(self):
        self.logger.info("Reading ATV parameter file")
        # implement reading ATV parameter file functionality
        with open("atv_parameter_file.json", "r") as file:
            return json.load(file)

    def read_alti_lab_parameter_file(self):
        self.logger.info("Reading AltiLab parameter file")
        # implement reading AltiLab parameter file functionality
        with open("alti_lab_parameter_file.json", "r") as file:
            return json.load(file)

    def read_safety_parameter_file(self):
        self.logger.info("Reading safety parameter file")
        # implement reading safety parameter file functionality
        with open("safety_parameter_file.json", "r") as file:
            return json.load(file)

    def read_safety_error_file(self):
        self.logger.info("Reading safety error file")
        # implement reading safety error file functionality
        with open("safety_error_file.json", "r") as file:
            return json.load(file)

    def read_sm_mapping_files(self):
        self.logger.info("Reading SM mapping files")
        # implement reading SM mapping files functionality
        with open("sm_mapping_files.json", "r") as file:
            return json.load(file)

    def switch_on_load(self, master, address):
        self.logger.info("Switching on load")
        # implement switching on load functionality
        master.execute(1, cst.WRITE_SINGLE_REGISTER, address, output_value=0x0001)

    def switch_off_load(self, master, address):
        self.logger.info("Switching off load")
        # implement switching off load functionality
        master.execute(1, cst.WRITE_SINGLE_REGISTER, address, output_value=0x0000)

    def init_fortis_load(self):
        self.logger.info("Initializing Fortis load")
        # implement initializing Fortis load functionality
        subprocess.run(["/usr/bin/init_fortis_load.sh"])

    def wait_for_time_in_milliseconds(self, milliseconds):
        self.logger.info("Waiting for specified time in milliseconds")
        # implement waiting for specified time in milliseconds functionality
        time.sleep(milliseconds / 1000)

    def write_report_head(self):
        self.logger.info("Writing report head")
        # implement writing report head functionality
        with open("report.txt", "w") as file:
            file.write("Report Head")

    def print_message(self, message):
        self.logger.info("Printing message")
        # implement printing message functionality
        print(message)

    def print_error_message(self, message):
        self.logger.error("Printing error message")
        # implement printing error message functionality
        print(message)

    def set_test_case_name(self, test_case_name):
        TlTestCase.set_test_case_name(test_case_name)