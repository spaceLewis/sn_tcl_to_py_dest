

import time
import ctypes
import win32api
import win32con

class UtilPrint:
    def do_print_mode(self, mode):
        print(f"Current drive mode: {mode}")

    def do_print_error_text(self, error_code):
        error_text = self.do_get_error_text(error_code)
        print(f"Error {error_code}: {error_text}")

    def do_get_error_text(self, error_code):
        error_texts = {
            1: "Error 1",
            2: "Error 2",
            3: "Error 3",
            # Add more error codes and texts as needed
        }
        return error_texts.get(error_code, "Unknown error")

    def print_proc_entry_info(self, proc_entry):
        print(f"Procedure entry information: {proc_entry}")

    def do_print_win_error_text(self, error_code):
        error_text = ctypes.FormatError(error_code)
        print(f"Windows error {error_code}: {error_text}")

    def show_status(self, status):
        print(f"Current status: {status}")

    def do_print_status(self, drive_state, ref_channel, cmd_channel):
        print(f"Drive state: {drive_state}, Reference channel: {ref_channel}, Command channel: {cmd_channel}")

    def do_print_modules(self, modules):
        print("Modules and option boards:")
        for module in modules:
            print(module)

    def do_print_fault_info(self, fault_info):
        print("Fault information:")
        for info in fault_info:
            print(info)

    def do_print_SM_ErrorState(self, error_state):
        print(f"Error state: {error_state}")

    def do_print_com_para(self, com_para):
        print("Communication parameters:")
        for para in com_para:
            print(para)

    def do_print_io(self, io_info):
        print("I/O information:")
        for info in io_info:
            print(info)

    def do_display_error_memory(self, error_memory):
        print("Error memory information:")
        for address, value in error_memory.items():
            print(f"Address: {address}, Value: {value}")

    def do_reset(self):
        print("Device reset")

    def do_wait_ms(self, ms):
        time.sleep(ms / 1000)

    def do_wait_for_object(self, object, timeout=10):
        start_time = time.time()
        while not object:
            time.sleep(0.1)
            if time.time() - start_time > timeout:
                print("Timeout waiting for object")
                break