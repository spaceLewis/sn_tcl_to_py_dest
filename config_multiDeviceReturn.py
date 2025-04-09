

```python
import os
import sys

# Define the list of devices
devices = ['AltiLab', 'ATS', 'FFT146']

# Define the dictionary of device types
device_types = {
    'AltiLab': 'altivar',
    'ATS': 'ats',
    'FFT146': 'fft146'
}

# Define the active device
active_device = 'AltiLab'

# Check if the system feature 'EAETower1' is enabled
if os.environ.get('EAETOWER1_ENABLED', 'false').lower() == 'true':
    # Source the Altivar library if it is
    sys.path.insert(0, '/path/to/altivar/library')

# Check if the active device is in the list of devices
if active_device not in devices:
    raise ValueError("Active device not found in the list of devices")

# Switch based on the device type and perform the necessary actions
for i, device in enumerate(devices):
    if device == active_device:
        if device_types[device] == 'altivar':
            # Check if the parameter file for AltiLab devices exists
            if os.path.exists('altivar_parameter_file.txt'):
                # Read the parameter file for AltiLab devices
                with open('altivar_parameter_file.txt', 'r') as f:
                    altivar_parameters = f.read()
            else:
                raise FileNotFoundError("Parameter file for AltiLab devices not found")
        elif device_types[device] == 'ats':
            # Check if the unified mapping file for ATS devices exists
            if os.path.exists('ats_unified_mapping_file.txt'):
                # Read the unified mapping file for ATS devices
                with open('ats_unified_mapping_file.txt', 'r') as f:
                    ats_unified_mapping = f.read()
            else:
                raise FileNotFoundError("Unified mapping file for ATS devices not found")
        elif device_types[device] == 'fft146':
            try:
                # Import the fft146_alarm_management module
                from fft146_alarm_management import initialize_alarm_management
                # Initialize the alarm management system for FFT146 devices
                initialize_alarm_management()
            except ImportError:
                raise ImportError("Failed to import fft146_alarm_management module")
        else:
            raise ValueError("Unsupported device type")

# Set the value of i
i = devices.index(active_device)

# Return the value of the device at index i
return devices[i]
```