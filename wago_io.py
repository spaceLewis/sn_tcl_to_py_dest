

import logging
import requests

class WagoIO:
    def __init__(self, ip_address, username, password):
        self.ip_address = ip_address
        self.username = username
        self.password = password
        self.logger = logging.getLogger(__name__)

    def get_digital_input(self, input_number):
        if not isinstance(input_number, int) or input_number < 0:
            self.logger.error("Invalid digital input number")
            return None
        url = f"http://{self.ip_address}/api/v1/digital_inputs/{input_number}"
        try:
            response = requests.get(url, auth=(self.username, self.password))
            response.raise_for_status()
            return response.json()["value"]
        except requests.exceptions.RequestException as e:
            self.logger.error(f"Failed to get digital input {input_number}: {e}")
            return None

    def set_digital_output(self, output_number, value):
        if not isinstance(output_number, int) or output_number < 0:
            self.logger.error("Invalid digital output number")
            return False
        if not isinstance(value, bool):
            self.logger.error("Invalid digital output value")
            return False
        url = f"http://{self.ip_address}/api/v1/digital_outputs/{output_number}"
        data = {"value": value}
        try:
            response = requests.put(url, json=data, auth=(self.username, self.password))
            response.raise_for_status()
            return True
        except requests.exceptions.RequestException as e:
            self.logger.error(f"Failed to set digital output {output_number}: {e}")
            return False

    def get_analog_input(self, input_number):
        if not isinstance(input_number, int) or input_number < 0:
            self.logger.error("Invalid analog input number")
            return None
        url = f"http://{self.ip_address}/api/v1/analog_inputs/{input_number}"
        try:
            response = requests.get(url, auth=(self.username, self.password))
            response.raise_for_status()
            return response.json()["value"]
        except requests.exceptions.RequestException as e:
            self.logger.error(f"Failed to get analog input {input_number}: {e}")
            return None

    def set_analog_output(self, output_number, value):
        if not isinstance(output_number, int) or output_number < 0:
            self.logger.error("Invalid analog output number")
            return False
        if not isinstance(value, (int, float)) or value < 0 or value > 100:
            self.logger.error("Invalid analog output value")
            return False
        url = f"http://{self.ip_address}/api/v1/analog_outputs/{output_number}"
        data = {"value": value}
        try:
            response = requests.put(url, json=data, auth=(self.username, self.password))
            response.raise_for_status()
            return True
        except requests.exceptions.RequestException as e:
            self.logger.error(f"Failed to set analog output {output_number}: {e}")
            return False

    def get_device_info(self):
        url = f"http://{self.ip_address}/api/v1/device_info"
        try:
            response = requests.get(url, auth=(self.username, self.password))
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            self.logger.error(f"Failed to get device info: {e}")
            return None

    def reboot_device(self):
        url = f"http://{self.ip_address}/api/v1/reboot"
        try:
            response = requests.post(url, auth=(self.username, self.password))
            response.raise_for_status()
            return True
        except requests.exceptions.RequestException as e:
            self.logger.error(f"Failed to reboot device: {e}")
            return False

    def get_firmware_version(self):
        url = f"http://{self.ip_address}/api/v1/firmware_version"
        try:
            response = requests.get(url, auth=(self.username, self.password))
            response.raise_for_status()
            return response.json()["version"]
        except requests.exceptions.RequestException as e:
            self.logger.error(f"Failed to get firmware version: {e}")
            return None