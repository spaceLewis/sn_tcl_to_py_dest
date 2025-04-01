

import plc_registers

def set_relay(relay, state):
    plc_registers.write_register(relay, 1 if state else 0)

def wait_for_relay(relay, state, timeout=None, waittime=None):
    if timeout is not None:
        start_time = plc_registers.get_time()
        while plc_registers.read_register(relay) != state:
            if plc_registers.get_time() - start_time > timeout:
                return False
    elif waittime is not None:
        plc_registers.sleep(waittime)
    return plc_registers.read_register(relay) == state

def check_relay(relay):
    return plc_registers.read_register(relay)