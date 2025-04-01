

```python
import sys

def validate_python_version():
    if sys.version_info.major < 3:
        raise Exception("Python version must be 3 or higher")

def initialize_test_file_list():
    try:
        theTestFileList = []
        return theTestFileList
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def validate_test_file_list(test_file_list):
    if not test_file_list:
        raise Exception("Test file list is empty")

def main():
    validate_python_version()
    theTestFileList = initialize_test_file_list()
    validate_test_file_list(theTestFileList)

if __name__ == "__main__":
    main()
```