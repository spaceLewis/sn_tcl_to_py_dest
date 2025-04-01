

from opcua import Client
from urllib.parse import urlparse
import logging

class OpcuaConnection:
    def __init__(self, url):
        self.url = url
        self.client = Client(url)
        self.validate_url()

    def validate_url(self):
        try:
            result = urlparse(self.url)
            if not all([result.scheme, result.netloc]):
                raise ValueError("Invalid URL")
        except ValueError as e:
            logging.error(f"Invalid URL: {e}")
            raise

    def open_connection(self):
        try:
            self.client.connect()
        except Exception as e:
            logging.error(f"Connection failed: {e}")
            raise

    def close_connection(self):
        self.client.disconnect()

    def get_node(self, node_id):
        try:
            return self.client.get_node(node_id)
        except Exception as e:
            logging.error(f"Node not found: {e}")
            raise

    def get_children(self, node):
        return node.get_children()

    def get_browse_name(self, node):
        return node.get_browse_name()

    def get_display_name(self, node):
        return node.get_display_name()

    def get_node_class(self, node):
        return node.get_node_class()

    def get_description(self, node):
        return node.get_description()

    def get_value(self, node):
        return node.get_value()

    def set_value(self, node, value):
        try:
            node.set_value(value)
        except Exception as e:
            logging.error(f"Invalid value: {e}")
            raise