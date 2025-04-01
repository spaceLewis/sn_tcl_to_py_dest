

import configparser

def read_config_values(config_file):
    config = configparser.ConfigParser()
    try:
        config.read(config_file)
        if 'TestObject' in config.sections():
            return config['TestObject']
        else:
            raise KeyError('TestObject section not found in config file')
    except configparser.Error as e:
        print(f"Error reading config file: {e}")
        return None

def read_config_test_object(config_file):
    return read_config_values(config_file)