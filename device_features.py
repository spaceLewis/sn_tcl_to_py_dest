

from enum import Enum

class DeviceFeatures(Enum):
    BLUETOOTH = "Bluetooth connectivity"
    WI_FI = "Wi-Fi connectivity"
    GPS = "Global Positioning System"
    CAMERA = "Camera functionality"
    FINGERPRINT_READER = "Fingerprint reader"
    FACE_RECOGNITION = "Face recognition"
    VOICE_ASSISTANT = "Voice assistant"
    WATER_RESISTANCE = "Water resistance"
    DUST_RESISTANCE = "Dust resistance"
    HEART_RATE_MONITOR = "Heart rate monitor"
    BLOOD_OXYGEN_LEVEL_MONITOR = "Blood oxygen level monitor"
    BATTERY_SAVING_MODE = "Battery saving mode"
    FAST_CHARGING = "Fast charging"
    WIRELESS_CHARGING = "Wireless charging"
    NFC = "Near Field Communication"
    FINGERPRINT_SENSOR = "Fingerprint sensor"
    PROXIMITY_SENSOR = "Proximity sensor"
    ACCELEROMETER = "Accelerometer"
    GYROSCOPE = "Gyroscope"
    COMPASS = "Compass"
    BAROMETER = "Barometer"
    AMBIENT_LIGHT_SENSOR = "Ambient light sensor"
    TEMPERATURE_SENSOR = "Temperature sensor"
    HUMIDITY_SENSOR = "Humidity sensor"
    PRESSURE_SENSOR = "Pressure sensor"

    def __repr__(self):
        return f"{self.name} - {self.value}"