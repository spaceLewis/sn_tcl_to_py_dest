

import os
import time

def TlPrint(message):
    print(message)

def TlInput(prompt):
    return input(prompt)

def get_sys_feat(feature):
    return hasattr(os, feature)

def set_prio(pid, priority):
    try:
        os.system(f"renice {priority} {pid}")
    except Exception as e:
        TlPrint(f"Error setting priority: {e}")

def get_prio(pid):
    try:
        output = os.popen(f"ps -p {pid} -o ni").read()
        return int(output.split()[1])
    except Exception as e:
        TlPrint(f"Error getting priority: {e}")
        return None

def tcl4_tower_info():
    return "UniFAST package information"

def GetSysFeat(feature):
    return get_sys_feat(feature)

def TlWrite(register, value):
    try:
        with open(register, 'w') as f:
            f.write(str(value))
    except Exception as e:
        TlPrint(f"Error writing to register: {e}")

def doWaitForObject(obj, timeout=10):
    start_time = time.time()
    while time.time() - start_time < timeout:
        if obj:
            return True
        time.sleep(0.1)
    return False

def doWaitMs(ms):
    time.sleep(ms / 1000)

def read_error_text_file(file_path):
    try:
        with open(file_path, 'r') as f:
            return f.read()
    except Exception as e:
        TlPrint(f"Error reading error text file: {e}")
        return None

def read_parameter_file(file_path):
    try:
        with open(file_path, 'r') as f:
            return f.read()
    except Exception as e:
        TlPrint(f"Error reading parameter file: {e}")
        return None

def detect_device_features():
    try:
        with open("/proc/cpuinfo", 'r') as f:
            cpu_info = f.read()
            if "arm" in cpu_info:
                return "ARM"
            elif "x86" in cpu_info:
                return "x86"
            else:
                return "Unknown"
    except Exception as e:
        TlPrint(f"Error detecting device features: {e}")
        return None