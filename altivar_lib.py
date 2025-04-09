

package altivar_lib

import os
import json

class Altivar_lib:
    def __init__(self, parameter_file_path='altivar_parameters.json', parameter_type_file_path='altivar_parameter_types.json'):
        self.parameter_file_path = parameter_file_path
        self.parameter_type_file_path = parameter_type_file_path

    def read_parameter_file(self):
        try:
            if os.path.exists(self.parameter_file_path):
                with open(self.parameter_file_path, 'r') as file:
                    data = json.load(file)
                    if not isinstance(data, dict):
                        raise ValueError('Invalid JSON content')
                    return data
            else:
                return {}
        except json.JSONDecodeError as e:
            raise ValueError('Invalid JSON file') from e
        except Exception as e:
            raise Exception('Error reading parameter file') from e

    def read_parameter_type_file(self):
        try:
            if os.path.exists(self.parameter_type_file_path):
                with open(self.parameter_type_file_path, 'r') as file:
                    data = json.load(file)
                    if not isinstance(data, dict):
                        raise ValueError('Invalid JSON content')
                    return data
            else:
                return {}
        except json.JSONDecodeError as e:
            raise ValueError('Invalid JSON file') from e
        except Exception as e:
            raise Exception('Error reading parameter type file') from e