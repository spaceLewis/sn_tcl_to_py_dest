

package environment_variables

import os

class EnvironmentVariables:
    def __init__(self):
        self.test_environment = {
            'DB_HOST': os.getenv('DB_HOST', 'localhost'),
            'DB_PORT': os.getenv('DB_PORT', '5432'),
            'DB_USERNAME': os.getenv('DB_USERNAME', 'test_user'),
            'DB_PASSWORD': os.getenv('DB_PASSWORD', 'test_password'),
            'DB_NAME': os.getenv('DB_NAME', 'test_database'),
            'API_URL': os.getenv('API_URL', 'http://localhost:8080/api')
        }

    def get_environment_variables(self):
        return self.test_environment