

import time
import logging
import wagoio

# Define the logger
logger = logging.getLogger(__name__)

# Define the Wago IO device
device = wagoio.WagoIO()

def wc_Test_Active():
    try:
        # Test if the device is active
        if device.is_active():
            logger.info("Device is active")
        else:
            logger.error("Device is not active")
    except wagoio.DeviceCommunicationError as e:
        logger.error(f"Device communication error: {e}")

def wc_Check_DQx():
    try:
        # Check the digital outputs
        for i in range(1, 9):
            if device.get_digital_output(i):
                logger.info(f"DQ{i} is high")
            else:
                logger.info(f"DQ{i} is low")
    except wagoio.DeviceCommunicationError as e:
        logger.error(f"Device communication error: {e}")

def wc_Check_BrakeOut():
    try:
        # Check the brake output
        if device.get_brake_output():
            logger.info("Brake output is high")
        else:
            logger.info("Brake output is low")
    except wagoio.DeviceCommunicationError as e:
        logger.error(f"Device communication error: {e}")

def wc_Test_NoFault():
    try:
        # Test if there are no faults
        if device.get_fault():
            logger.error("Fault detected")
        else:
            logger.info("No faults detected")
    except wagoio.DeviceCommunicationError as e:
        logger.error(f"Device communication error: {e}")

def wc_Set_REF():
    try:
        # Set the reference value
        device.set_reference(1000)
        logger.info("Reference value set to 1000")
    except wagoio.DeviceCommunicationError as e:
        logger.error(f"Device communication error: {e}")

def wc_Set_LIMN():
    try:
        # Set the negative limit value
        device.set_negative_limit(500)
        logger.info("Negative limit value set to 500")
    except wagoio.DeviceCommunicationError as e:
        logger.error(f"Device communication error: {e}")

def wc_Set_LIMP():
    try:
        # Set the positive limit value
        device.set_positive_limit(1500)
        logger.info("Positive limit value set to 1500")
    except wagoio.DeviceCommunicationError as e:
        logger.error(f"Device communication error: {e}")

def wc_Set_FAULT_RESET():
    try:
        # Reset the fault
        device.reset_fault()
        logger.info("Fault reset")
    except wagoio.DeviceCommunicationError as e:
        logger.error(f"Device communication error: {e}")

def wc_Set_ENABLE():
    try:
        # Enable the device
        device.enable()
        logger.info("Device enabled")
    except wagoio.DeviceCommunicationError as e:
        logger.error(f"Device communication error: {e}")

def wc_Set_HALT():
    try:
        # Halt the device
        device.halt()
        logger.info("Device halted")
    except wagoio.DeviceCommunicationError as e:
        logger.error(f"Device communication error: {e}")

def wc_Set_EndSW():
    try:
        # Set the end switch
        device.set_end_switch(True)
        logger.info("End switch set")
    except wagoio.DeviceCommunicationError as e:
        logger.error(f"Device communication error: {e}")

def wc_SetSTO():
    try:
        # Set the safe torque off
        device.set_safe_torque_off(True)
        logger.info("Safe torque off set")
    except wagoio.DeviceCommunicationError as e:
        logger.error(f"Device communication error: {e}")

def wc_SetSTO_Channel():
    try:
        # Set the safe torque off channel
        device.set_safe_torque_off_channel(1)
        logger.info("Safe torque off channel set to 1")
    except wagoio.DeviceCommunicationError as e:
        logger.error(f"Device communication error: {e}")

def wc_SetSTOex():
    try:
        # Set the extended safe torque off
        device.set_extended_safe_torque_off(True)
        logger.info("Extended safe torque off set")
    except wagoio.DeviceCommunicationError as e:
        logger.error(f"Device communication error: {e}")

def wc_SetSTO_Channelex():
    try:
        # Set the extended safe torque off channel
        device.set_extended_safe_torque_off_channel(2)
        logger.info("Extended safe torque off channel set to 2")
    except wagoio.DeviceCommunicationError as e:
        logger.error(f"Device communication error: {e}")