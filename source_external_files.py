

import importlib.util
import sys

def source_file(file_path):
    try:
        if sys.version_info.major < 3:
            raise Exception("Python version must be 3 or higher")
        spec = importlib.util.spec_from_file_location("module.name", file_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        if module.__name__ != "ATS_lib" and module.__name__ != "Keypad_lib":
            raise Exception("Invalid module imported")
        return module
    except FileNotFoundError:
        print(f"File {file_path} not found")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

ATS_lib = source_file('/path/to/ATS_lib.py')
Keypad_lib = source_file('/path/to/Keypad_lib.py')