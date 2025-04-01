

```python
import os
import sys
import importlib.util

# Define the list of devices
devices = ['Altivar', 'PACY', 'Other']

# Define the dictionary of device types
device_types = {
    'Altivar': 'altivar',
    'PACY': 'pacy',
    'Other': 'other'
}

# Define the active device
active_device = 'Altivar'

# Define the paths to various files
parameter_file_path = '/path/to/parameter/file'
parameter_type_file_path = '/path/to/parameter/type/file'
alarm_management_system_path = '/path/to/alarm/management/system'

# Check if the system feature 'EAETower1' is enabled
if 'EAETower1' in os.environ:
    # Source the Altivar library
    altivar_library_path = '/path/to/altivar/library'
    if os.path.exists(altivar_library_path):
        sys.path.append(altivar_library_path)
        altivar_spec = importlib.util.find_spec('altivar')
        if altivar_spec is not None:
            altivar = importlib.util.module_from_spec(altivar_spec)
            altivar_spec.loader.exec_module(altivar)
            try:
                # Read the parameter file and parameter type file for Altivar devices
                altivar.read_parameter_file(parameter_file_path)
                altivar.read_parameter_type_file(parameter_type_file_path)
            except Exception as e:
                print(f"Error reading parameter files: {e}")
        else:
            print("Altivar module not found")
    else:
        print("Altivar library path does not exist")

    # Switch based on the device type
    if active_device == 'Altivar':
        # Perform actions for Altivar devices
        try:
            altivar.initialize_alarm_management_system(alarm_management_system_path)
            altivar.set_configuration_values()
        except Exception as e:
            print(f"Error initializing alarm management system or setting configuration values for Altivar: {e}")
    elif active_device == 'PACY':
        # Perform actions for PACY devices
        pacy_library_path = '/path/to/pacy/library'
        if os.path.exists(pacy_library_path):
            sys.path.append(pacy_library_path)
            pacy_spec = importlib.util.find_spec('pacy')
            if pacy_spec is not None:
                pacy = importlib.util.module_from_spec(pacy_spec)
                pacy_spec.loader.exec_module(pacy)
                try:
                    pacy.initialize_alarm_management_system(alarm_management_system_path)
                    pacy.set_configuration_values()
                except Exception as e:
                    print(f"Error initializing alarm management system or setting configuration values for PACY: {e}")
            else:
                print("PACY module not found")
        else:
            print("PACY library path does not exist")
    else:
        # Perform actions for other devices
        other_library_path = '/path/to/other/library'
        if os.path.exists(other_library_path):
            sys.path.append(other_library_path)
            other_spec = importlib.util.find_spec('other')
            if other_spec is not None:
                other = importlib.util.module_from_spec(other_spec)
                other_spec.loader.exec_module(other)
                try:
                    other.initialize_alarm_management_system(alarm_management_system_path)
                    other.set_configuration_values()
                except Exception as e:
                    print(f"Error initializing alarm management system or setting configuration values for other devices: {e}")
            else:
                print("Other module not found")
        else:
            print("Other library path does not exist")

# Check if the system feature 'PACY_APP_FLEX' is enabled
if 'PACY_APP_FLEX' in os.environ:
    # Perform actions for PACY_APP_FLEX
    pacy_app_flex_library_path = '/path/to/pacy_app_flex/library'
    if os.path.exists(pacy_app_flex_library_path):
        sys.path.append(pacy_app_flex_library_path)
        pacy_app_flex_spec = importlib.util.find_spec('pacy_app_flex')
        if pacy_app_flex_spec is not None:
            pacy_app_flex = importlib.util.module_from_spec(pacy_app_flex_spec)
            pacy_app_flex_spec.loader.exec_module(pacy_app_flex)
            try:
                pacy_app_flex.initialize_alarm_management_system(alarm_management_system_path)
                pacy_app_flex.set_configuration_values()
            except Exception as e:
                print(f"Error initializing alarm management system or setting configuration values for PACY_APP_FLEX: {e}")
        else:
            print("PACY_APP_FLEX module not found")
    else:
        print("PACY_APP_FLEX library path does not exist")
```