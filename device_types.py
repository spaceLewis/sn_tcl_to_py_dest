

package device_types

class DeviceTypes:
    def __init__(self):
        self.device_types = {
            "router": "A device that connects multiple networks together and routes traffic between them.",
            "switch": "A device that connects multiple devices within a network and forwards data packets between them.",
            "firewall": "A device that controls incoming and outgoing network traffic based on predetermined security rules.",
            "server": "A device that provides services, resources, or data to other devices on a network.",
            "workstation": "A device used by an individual for tasks such as programming, data analysis, or graphics design.",
            "printer": "A device that produces a physical copy of a document or image.",
            "scanner": "A device that captures images or documents and converts them into digital data.",
            "modem": "A device that connects a network to the internet via a broadband connection.",
            "hub": "A device that connects multiple devices within a network and broadcasts incoming data to all connected devices."
        }
        self.validate_device_types()

    def validate_device_types(self):
        if not self.device_types:
            raise ValueError("Device types dictionary is empty or null")
        required_keys = ["router", "switch", "firewall", "server", "workstation", "printer", "scanner", "modem", "hub"]
        for key in required_keys:
            if key not in self.device_types:
                raise ValueError(f"Device types dictionary is missing required key: {key}")
            if not self.device_types[key]:
                raise ValueError(f"Device description for {key} is empty or null")

    def get_device_type(self, device_type):
        try:
            return self.device_types[device_type]
        except KeyError:
            raise ValueError(f"Device type {device_type} not found")

    def get_all_device_types(self):
        return self.device_types