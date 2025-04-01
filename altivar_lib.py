

import os
import json

class ParameterFileReader:
    def __init__(self, file_path):
        self.file_path = file_path

    def read(self):
        try:
            with open(self.file_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            raise ValueError(f"File not found: {self.file_path}")
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON: {e}")

class ParameterFileUpdater:
    def __init__(self, file_path):
        self.file_path = file_path

    def update(self, parameter_name, new_value, parameters):
        if parameter_name not in parameters:
            raise ValueError(f"Parameter not found: {parameter_name}")
        parameters[parameter_name] = new_value
        with open(self.file_path, 'w') as file:
            json.dump(parameters, file)

class AltivarLibrary:
    def __init__(self, parameter_file_path, parameter_type_file_path):
        self.parameter_file_reader = ParameterFileReader(parameter_file_path)
        self.parameter_type_file_reader = ParameterFileReader(parameter_type_file_path)
        self.parameter_file_updater = ParameterFileUpdater(parameter_file_path)
        self.parameter_type_file_updater = ParameterFileUpdater(parameter_type_file_path)

    def get_parameter(self, parameter_name):
        parameters = self.parameter_file_reader.read()
        return parameters.get(parameter_name)

    def get_parameter_type(self, parameter_name):
        parameter_types = self.parameter_type_file_reader.read()
        return parameter_types.get(parameter_name)

    def update_parameter(self, parameter_name, new_value):
        parameters = self.parameter_file_reader.read()
        self.parameter_file_updater.update(parameter_name, new_value, parameters)

    def update_parameter_type(self, parameter_name, new_type):
        parameter_types = self.parameter_type_file_reader.read()
        self.parameter_type_file_updater.update(parameter_name, new_type, parameter_types)