

```python
import os
import sys
import importlib.util

# Define global variables
GLOBAL_VAR = "global_variable"

# Initialize an empty list
test_file_list = []

# Load external Python scripts
def load_external_scripts():
    try:
        spec = importlib.util.spec_from_file_location("external_script", "external_script.py")
        external_script = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(external_script)
    except FileNotFoundError:
        print("Error: External script not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

# Validate if the test file exists before appending it to the list
def validate_test_file(test_file):
    if not os.path.exists(test_file):
        print(f"Error: Test file '{test_file}' not found.")
        sys.exit(1)

# Append a test file to the list
def append_test_file(test_file):
    try:
        validate_test_file(test_file)
        test_file_list.append(test_file)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

# Print the test file list
def print_test_file_list():
    print(test_file_list)

# Main function
def main():
    load_external_scripts()
    append_test_file("test_file.txt")
    print_test_file_list()

if __name__ == "__main__":
    main()
```