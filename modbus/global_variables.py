

package modbus

import logging

# Initialize logger
logger = logging.getLogger(__name__)

# Global variables
theDebugFlagObj = False
DevAdr = []
ActDev = None
BreakPoint = False
errorInfo = {}
glb_Error = False

# Function to set debug flag
def set_debug_flag(debug_flag):
    global theDebugFlagObj
    theDebugFlagObj = debug_flag

# Function to get debug flag
def get_debug_flag():
    return theDebugFlagObj

# Function to set device address
def set_dev_adr(dev_adr):
    global DevAdr
    DevAdr = dev_adr

# Function to get device address
def get_dev_adr():
    return DevAdr

# Function to set active device
def set_act_dev(act_dev):
    global ActDev
    ActDev = act_dev

# Function to get active device
def get_act_dev():
    return ActDev

# Function to set breakpoint
def set_break_point(break_point):
    global BreakPoint
    BreakPoint = break_point

# Function to get breakpoint
def get_break_point():
    return BreakPoint

# Function to set error information
def set_error_info(error_info):
    global errorInfo
    errorInfo = error_info

# Function to get error information
def get_error_info():
    return errorInfo

# Function to set global error
def set_glb_error(glb_error):
    global glb_Error
    glb_Error = glb_error

# Function to get global error
def get_glb_error():
    return glb_Error

# Function to log error
def log_error(error):
    logger.error(error)

# Function to log info
def log_info(info):
    logger.info(info)