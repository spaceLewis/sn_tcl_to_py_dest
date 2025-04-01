

import os
import json
import logging

class KeypadLib:
    def __init__(self, param_file_path, param_type_file_path):
        self.param_file_path = param_file_path
        self.param_type_file_path = param_type_file_path
        self.logger = logging.getLogger(__name__)

    def read_param_file(self):
        try:
            with open(self.param_file_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            self.logger.error(f"File not found: {self.param_file_path}")
            return {}
        except json.JSONDecodeError as e:
            self.logger.error(f"Invalid JSON in file: {self.param_file_path} - {e}")
            return {}
        except Exception as e:
            self.logger.error(f"Error reading file: {self.param_file_path} - {e}")
            return {}

    def read_param_type_file(self):
        try:
            with open(self.param_type_file_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            self.logger.error(f"File not found: {self.param_type_file_path}")
            return {}
        except json.JSONDecodeError as e:
            self.logger.error(f"Invalid JSON in file: {self.param_type_file_path} - {e}")
            return {}
        except Exception as e:
            self.logger.error(f"Error reading file: {self.param_type_file_path} - {e}")
            return {}

    def get_param_value(self, param_name):
        params = self.read_param_file()
        return params.get(param_name)

    def get_param_type(self, param_name):
        param_types = self.read_param_type_file()
        return param_types.get(param_name)

    def update_param_value(self, param_name, new_value):
        params = self.read_param_file()
        if param_name in params:
            params[param_name] = new_value
            try:
                with open(self.param_file_path, 'w') as file:
                    json.dump(params, file)
            except Exception as e:
                self.logger.error(f"Error writing file: {self.param_file_path} - {e}")
        else:
            self.logger.error(f"Parameter not found: {param_name}")

    def update_param_type(self, param_name, new_type):
        param_types = self.read_param_type_file()
        if param_name in param_types:
            param_types[param_name] = new_type
            try:
                with open(self.param_type_file_path, 'w') as file:
                    json.dump(param_types, file)
            except Exception as e:
                self.logger.error(f"Error writing file: {self.param_type_file_path} - {e}")
        else:
            self.logger.error(f"Parameter not found: {param_name}")