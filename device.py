

package device

class Device:
    def __init__(self):
        self.encoder_settings = None
        self.relay_configuration = None
        self.keypad_status = None
        self.device_status = False
        self.ats_parameters = None
        self.default_values = None
        self.relay_status = None

    def reset_device(self):
        self.encoder_settings = None
        self.relay_configuration = None
        self.keypad_status = None
        self.device_status = False
        self.ats_parameters = None
        self.default_values = None
        self.relay_status = None

    def adapt_encoder_settings(self, settings):
        self.encoder_settings = settings

    def device_on(self):
        self.device_status = True

    def ats_para_identification(self):
        self.ats_parameters = "ATS parameters identified"

    def do_set_defaults(self):
        self.default_values = "Default values set"

    def set_relay_configuration(self, configuration):
        self.relay_configuration = configuration

    def check_all_relay_status(self):
        self.relay_status = "Relay status checked"

    def ats_command_switch(self, command):
        if command == "on":
            self.ats_parameters = "ATS command on"
        elif command == "off":
            self.ats_parameters = "ATS command off"

    def do_wait_for_keypad_status(self, status):
        while self.keypad_status != status:
            pass