import argparse
import configparser
import os

# Command-Line Argument Handling
parser = argparse.ArgumentParser()
parser.add_argument("mode", help="Mode of operation")
parser.add_argument("--device", help="Device information")
parser.add_argument("--flash", help="Flash information")
args = parser.parse_args()

# Mode-Specific Requirements
if args.mode == "serialCampaignLaunch":
    # Serial campaign launch mode
    print("Serial campaign launch mode")
    config = configparser.ConfigParser()
    config.read("config_serial_campaign.ini")
    test_dir_list = []
    top_script = ""
    print("Test environment started")
    print("Mode of operation: " + args.mode)
    try:
        test_categories = os.listdir("test_categories")
        for category in test_categories:
            test_dir_list.append(category)
    except FileNotFoundError:
        print("Error: Test categories directory not found")
        exit(1)
    device_info = ""
    print("Device information: " + device_info)

elif args.mode == "Jenkins":
    # Jenkins mode
    if args.device is None:
        print("Error: Device information is required for Jenkins mode")
        exit(1)
    print("Jenkins mode")
    config = configparser.ConfigParser()
    config.read("config_jenkins.ini")
    test_dir_list = []
    top_script = ""
    print("Test environment started")
    print("Mode of operation: " + args.mode)
    try:
        test_categories = os.listdir("test_categories")
        for category in test_categories:
            test_dir_list.append(category)
    except FileNotFoundError:
        print("Error: Test categories directory not found")
        exit(1)
    device_info = args.device
    print("Device information: " + device_info)

elif args.mode == "JenkinsFULLCAMPAIN":
    # Jenkins full campaign mode
    if args.device is None:
        print("Error: Device information is required for Jenkins full campaign mode")
        exit(1)
    print("Jenkins full campaign mode")
    config = configparser.ConfigParser()
    config.read("config_jenkins_full_campaign.ini")
    test_dir_list = []
    top_script = ""
    print("Test environment started")
    print("Mode of operation: " + args.mode)
    try:
        test_categories = os.listdir("test_categories")
        for category in test_categories:
            test_dir_list.append(category)
    except FileNotFoundError:
        print("Error: Test categories directory not found")
        exit(1)
    device_info = args.device
    print("Device information: " + device_info)

elif args.mode == "UnifastCI":
    # UnifastCI mode
    if args.device is None or args.flash is None:
        print("Error: Device and flash information are required for UnifastCI mode")
        exit(1)
    print("UnifastCI mode")
    config = configparser.ConfigParser()
    config.read("config_unifastci.ini")
    test_dir_list = []
    top_script = ""
    print("Test environment started")
    print("Mode of operation: " + args.mode)
    try:
        test_categories = os.listdir("test_categories")
        for category in test_categories:
            test_dir_list.append(category)
    except FileNotFoundError:
        print("Error: Test categories directory not found")
        exit(1)
    device_info = args.device
    print("Device information: " + device_info)

else:
    print("Error: Invalid mode")
    exit(1)
