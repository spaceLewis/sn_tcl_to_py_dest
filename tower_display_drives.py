

import os

the_test_dir_list = []

def tower_display_drives():
    global the_test_dir_list
    the_test_dir_list = []
    try:
        for disk in range(65, 91):
            drive = chr(disk) + ":"
            if os.path.exists(drive):
                the_test_dir_list.append(drive)
        return the_test_dir_list
    except Exception as e:
        print(f"An error occurred: {e}")
        return []