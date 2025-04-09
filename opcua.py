

from opcua import Client
from urllib.parse import urlparse

class Opcua:
    def __init__(self, url):
        self.url = url
        self.client = Client(url)
        self.connected = False

    def open_connection(self):
        try:
            self.client.connect()
            self.connected = True
        except Exception as e:
            print(f"Error opening connection: {e}")

    def close_connection(self):
        try:
            self.client.disconnect()
            self.connected = False
        except Exception as e:
            print(f"Error closing connection: {e}")

    def is_connected(self):
        return self.connected

    def validate_url(self):
        try:
            result = urlparse(self.url)
            return all([result.scheme, result.netloc])
        except ValueError:
            return False