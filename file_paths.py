

package file_paths

import os

# File paths for the test environment
TEST_ENVIRONMENT_FILE_PATHS = {
    'test_data': os.path.join(os.getcwd(), 'test_data'),
    'test_config': os.path.join(os.getcwd(), 'test_config'),
    'test_results': os.path.join(os.getcwd(), 'test_results')
}

# Validate if the file paths exist or are accessible
def validate_file_paths(file_paths):
    for path in file_paths.values():
        if not os.path.exists(path):
            raise FileNotFoundError(f"The file path '{path}' does not exist.")
        if not os.access(path, os.R_OK):
            raise PermissionError(f"The file path '{path}' is not accessible.")

# Handle potential errors that may occur when using the os.path.join function
def get_file_paths():
    try:
        return {
            'test_data': os.path.join(os.getcwd(), 'test_data'),
            'test_config': os.path.join(os.getcwd(), 'test_config'),
            'test_results': os.path.join(os.getcwd(), 'test_results')
        }
    except OSError as e:
        raise Exception(f"An error occurred while getting file paths: {e}")

# Usage
file_paths = get_file_paths()
validate_file_paths(file_paths)