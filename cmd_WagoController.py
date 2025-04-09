

```python
import logging
import requests
from requests.exceptions import RequestException

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class WagoControllerSession:
    def __init__(self, ip_address, username, password):
        self.ip_address = ip_address
        self.username = username
        self.password = password
        self.session = requests.Session()
        self.session.auth = (self.username, self.password)

    def send_request(self, method, url, data=None):
        try:
            response = self.session.request(method, url, data=data)
            response.raise_for_status()
            return response
        except RequestException as e:
            logger.error(f"Request failed: {}".format(e)
            return None

class WagoController:
    def __init__(self, ip_address, username, password):
        self.ip_address = ip_address
        self.username = username
        self.password = password
        self.session = WagoControllerSession(ip_address, username, password)

    def send_command(self, command):
        url = f"http://{self.ip_address}/wb"
        payload = {"cmd": command}
        response = self.session.send_request("POST", url, data=payload)
        if response is not None:
            logger.info(f"Command '{command}' sent successfully")
            return True
        else:
            logger.error(f"Failed to send command '{command}'")
            return False

    def get_status(self):
        url = f"http://{self.ip_address}/wb?cmd=status"
        response = self.session.send_request("GET", url)
        if response is not None:
            logger.info(f"Status: {response.text}")
            return response.text
        else:
            logger.error(f"Failed to get status")
            return None

    def reboot(self):
        return self.send_command("reboot")

    def restart(self):
        return self.send_command("restart")

    def shutdown(self):
        return self.send_command("shutdown")

    def get_version(self):
        url = f"http://{self.ip_address}/wb?cmd=version"
        response = self.session.send_request("GET", url)
        if response is not None:
            logger.info(f"Version: {response.text}")
            return response.text
        else:
            logger.error(f"Failed to get version")
            return None

# Example usage
if __name__ == "__main__":
    wago_controller = WagoController("192.168.1.100", "admin", "password")
    wago_controller.send_command("test")
    wago_controller.get_status()
    wago_controller.reboot()
    wago_controller.restart()
    wago_controller.shutdown()
    wago_controller.get_version()
```