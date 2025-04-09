

package config_TestObject

import os
import configparser

def read_config_file(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Configuration file '{file_path}' not found")

    config = configparser.ConfigParser()
    config.optionxform = str

    try:
        config.read(file_path)
    except configparser.Error as e:
        raise ValueError(f"Failed to read configuration file: {e}")

    return config

def parse_test_object_config(config):
    try:
        test_object_name = config.get('TestObject', 'test_object_name')
        test_object_description = config.get('TestObject', 'test_object_description')
        test_object_tags = config.get('TestObject', 'test_object_tags').split(',')
        test_object_priority = config.get('TestObject', 'test_object_priority')

        if not isinstance(test_object_name, str) or not isinstance(test_object_description, str) or not isinstance(test_object_tags, list) or not isinstance(test_object_priority, str):
            raise ValueError("Invalid data type in configuration file")

        return {
            'test_object_name': test_object_name,
            'test_object_description': test_object_description,
            'test_object_tags': test_object_tags,
            'test_object_priority': test_object_priority
        }

    except configparser.NoSectionError:
        raise ValueError("Missing 'TestObject' section in configuration file")
    except configparser.NoOptionError as e:
        raise ValueError(f"Missing required key in 'TestObject' section: {e}")

def config_test_object():
    config = read_config_file('test_object.cfg')
    return parse_test_object_config(config)