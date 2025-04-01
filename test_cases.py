

import unittest
from device import Device
from utility import Utility

class TestCases(unittest.TestCase):

    def TC_FFT041_FaultStopMode_TC01(self):
        device = Device()
        utility = Utility()
        device.connect()
        device.set_fault_stop_mode(True)
        self.assertTrue(device.get_fault_stop_mode())
        device.disconnect()

    def TC_FFT041_FaultStopMode_TC02(self):
        device = Device()
        utility = Utility()
        device.connect()
        device.set_fault_stop_mode(False)
        self.assertFalse(device.get_fault_stop_mode())
        device.disconnect()

    def TC_FFT041_FaultStopMode_TC03(self):
        device = Device()
        utility = Utility()
        device.connect()
        device.set_fault_stop_mode(True)
        device.trigger_fault()
        self.assertTrue(device.is_fault_triggered())
        device.reset_fault()
        self.assertFalse(device.is_fault_triggered())
        device.disconnect()

    def TC_FFT041_FaultStopMode_TC04(self):
        device = Device()
        utility = Utility()
        device.connect()
        device.set_fault_stop_mode(False)
        device.trigger_fault()
        self.assertTrue(device.is_fault_triggered())
        device.reset_fault()
        self.assertFalse(device.is_fault_triggered())
        device.disconnect()

if __name__ == '__main__':
    unittest.main()