

package FFT041_FaultStopMode

import os
import sys
import time
import unittest
from unittest.mock import patch, MagicMock
from fft_tests import FFTTestCase
import subprocess
import re

class FFT041_FaultStopMode(FFTTestCase):
    def setUp(self):
        super().setUp()
        self.test_file = 'FFT041_FaultStopMode.tcl'

    def test_fault_stop_mode(self):
        with patch('fft_tests.FFTTestCase.run_test') as mock_run_test:
            mock_run_test.return_value = True
            result = self.run_test(self.test_file)
            self.assertTrue(result)
            self.assertEqual(result, True)

    def test_fault_stop_mode_failure(self):
        with patch('fft_tests.FFTTestCase.run_test') as mock_run_test:
            mock_run_test.return_value = False
            result = self.run_test(self.test_file)
            self.assertFalse(result)
            self.assertEqual(result, False)

    def run_test(self, test_file):
        try:
            output = subprocess.check_output(['tclsh', test_file], stderr=subprocess.STDOUT)
            output = output.decode('utf-8')
            if re.search(r'Fault Stop Mode Test: PASS', output):
                return True
            else:
                return False
        except subprocess.CalledProcessError as e:
            print(f"Error running test: {e}")
            return False

if __name__ == '__main__':
    unittest.main()