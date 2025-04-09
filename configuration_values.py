

package configuration_values

class ConfigurationValues:
    def __init__(self):
        self.values = {
            'DB_HOST': {'value': 'localhost', 'description': 'Database host'},
            'DB_PORT': {'value': 5432, 'description': 'Database port'},
            'DB_USERNAME': {'value': 'admin', 'description': 'Database username'},
            'DB_PASSWORD': {'value': 'password', 'description': 'Database password'},
            'API_KEY': {'value': '1234567890', 'description': 'API key'}
        }

    def add_value(self, key, value, description):
        if key not in self.values:
            self.values[key] = {'value': value, 'description': description}
        else:
            raise ValueError(f"Key '{key}' already exists")

    def get_value(self, key):
        return self.values.get(key, {}).get('value')

    def get_description(self, key):
        return self.values.get(key, {}).get('description')

    def update_value(self, key, value):
        if key in self.values:
            self.values[key]['value'] = value
        else:
            raise ValueError(f"Key '{key}' does not exist")

    def update_description(self, key, description):
        if key in self.values:
            self.values[key]['description'] = description
        else:
            raise ValueError(f"Key '{key}' does not exist")

    def delete_value(self, key):
        if key in self.values:
            del self.values[key]
        else:
            raise ValueError(f"Key '{key}' does not exist")

    def get_all_values(self):
        return self.values