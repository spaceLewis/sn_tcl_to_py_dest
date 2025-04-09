

from enum import Enum
from datetime import datetime

class ShowStatusOnline(Enum):
    ONLINE = 1
    OFFLINE = 0

class DevAdr(Enum):
    DEVICE1 = "address1"
    DEVICE2 = "address2"
    # Add more devices as needed

class ActDev(Enum):
    DEVICE1 = 0
    DEVICE2 = 1
    # Add more devices as needed

class glb_Error(Enum):
    NO_ERROR = False
    ERROR = True

INFM_COUNTER = 10  # Limit the number of ShowStatus displays

class ShowStatusCounter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def reset(self):
        self.count = 0

class ShowStatusTime:
    def __init__(self):
        self.time = None

    def update(self):
        self.time = datetime.now()

    def get_time(self):
        return self.time