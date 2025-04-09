

import time
import unittest
from unittest.mock import MagicMock
from relay_configuration import setRelayConfiguration
import logging

class TestCases(unittest.TestCase):

    def setUp(self):
        self.device = MagicMock()
        self.logger = logging.getLogger(__name__)

    def tearDown(self):
        self.device.reset_mock()

    def test_device_behavior_under_power_failure(self):
        try:
            # Configure relay configuration
            setRelayConfiguration("power_failure")
            self.logger.info("Relay configuration set to power failure")

            # Wait for device to respond
            self.wait_for_device_response(10)

            # Check device behavior
            self.assertTrue(self.device.is_power_off())
            self.logger.info("Device is power off")
        except Exception as e:
            self.logger.error(f"Test case failed: {e}")
            self.fail()

    def test_device_behavior_under_network_failure(self):
        try:
            # Configure relay configuration
            setRelayConfiguration("network_failure")
            self.logger.info("Relay configuration set to network failure")

            # Wait for device to respond
            self.wait_for_device_response(10)

            # Check device behavior
            self.assertTrue(self.device.is_network_down())
            self.logger.info("Device is network down")
        except Exception as e:
            self.logger.error(f"Test case failed: {e}")
            self.fail()

    def test_device_behavior_under_sensor_failure(self):
        try:
            # Configure relay configuration
            setRelayConfiguration("sensor_failure")
            self.logger.info("Relay configuration set to sensor failure")

            # Wait for device to respond
            self.wait_for_device_response(10)

            # Check device behavior
            self.assertTrue(self.device.is_sensor_down())
            self.logger.info("Device is sensor down")
        except Exception as e:
            self.logger.error(f"Test case failed: {e}")
            self.fail()

    def test_device_behavior_under_software_failure(self):
        try:
            # Configure relay configuration
            setRelayConfiguration("software_failure")
            self.logger.info("Relay configuration set to software failure")

            # Wait for device to respond
            self.wait_for_device_response(10)

            # Check device behavior
            self.assertTrue(self.device.is_software_down())
            self.logger.info("Device is software down")
        except Exception as e:
            self.logger.error(f"Test case failed: {e}")
            self.fail()

    def wait_for_device_response(self, timeout):
        start_time = time.time()
        while time.time() - start_time < timeout:
            if self.device.is_responding():
                self.logger.info("Device is responding")
                return
            time.sleep(1)
        self.logger.error("Device did not respond within timeout")
        self.fail()

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    unittest.main()