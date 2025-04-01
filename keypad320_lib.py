

import os
import json

class Keypad320Lib:
    def __init__(self):
        self.parameter_files = {}
        self.parameter_type_files = {}

    def read_parameter_file(self, file_path):
        if os.path.exists(file_path):
            try:
                with open(file_path, 'r') as file:
                    self.parameter_files[file_path] = json.load(file)
            except json.JSONDecodeError as e:
                raise ValueError(f"Failed to parse JSON in file {file_path}: {e}")
        else:
            raise FileNotFoundError(f"File {file_path} not found")

    def read_parameter_type_file(self, file_path):
        if os.path.exists(file_path):
            try:
                with open(file_path, 'r') as file:
                    self.parameter_type_files[file_path] = json.load(file)
            except json.JSONDecodeError as e:
                raise ValueError(f"Failed to parse JSON in file {file_path}: {e}")
        else:
            raise FileNotFoundError(f"File {file_path} not found")

    def get_parameter(self, file_path, parameter_name):
        if file_path in self.parameter_files:
            return self.parameter_files[file_path].get(parameter_name)
        else:
            raise ValueError(f"File {file_path} not loaded")

    def get_parameter_type(self, file_path, parameter_name):
        if file_path in self.parameter_type_files:
            return self.parameter_type_files[file_path].get(parameter_name)
        else:
            raise ValueError(f"File {file_path} not loaded")

    def update_parameter_file(self, file_path, new_parameters):
        if file_path in self.parameter_files:
            self.parameter_files[file_path] = new_parameters
        else:
            raise ValueError(f"File {file_path} not loaded")

    def delete_parameter_file(self, file_path):
        if file_path in self.parameter_files:
            del self.parameter_files[file_path]
        else:
            raise ValueError(f"File {file_path} not loaded")

    def update_parameter_type_file(self, file_path, new_parameter_types):
        if file_path in self.parameter_type_files:
            self.parameter_type_files[file_path] = new_parameter_types
        else:
            raise ValueError(f"File {file_path} not loaded")

    def delete_parameter_type_file(self, file_path):
        if file_path in self.parameter_type_files:
            del self.parameter_type_files[file_path]
        else:
            raise ValueError(f"File {file_path} not loaded")