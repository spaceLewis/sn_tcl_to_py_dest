

import xml.etree.ElementTree as ET
import csv
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Global variables to store data extracted from configuration files
enum_number = {}
var_list = []
lxm_object_list = []
parameter_file_atv_old = []
para_file_atv = []
para_file_safety = []
error_file_safety = []

def enum_number_init(file_name):
    global enum_number
    try:
        tree = ET.parse(file_name)
        root = tree.getroot()
        for child in root:
            enum_number[child.attrib['name']] = child.attrib['value']
    except FileNotFoundError:
        logging.error(f"File {file_name} not found")
    except ET.ParseError:
        logging.error(f"Failed to parse {file_name}")

def read_var_list_file(file_name):
    global var_list
    try:
        with open(file_name, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                var_list.append(row)
    except FileNotFoundError:
        logging.error(f"File {file_name} not found")
    except csv.Error:
        logging.error(f"Failed to read {file_name}")

def read_lxm_object_list_file(file_name):
    global lxm_object_list
    try:
        with open(file_name, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                lxm_object_list.append(row)
    except FileNotFoundError:
        logging.error(f"File {file_name} not found")
    except csv.Error:
        logging.error(f"Failed to read {file_name}")

def read_parameter_file_atv_old(file_name):
    global parameter_file_atv_old
    try:
        with open(file_name, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                parameter_file_atv_old.append(row)
    except FileNotFoundError:
        logging.error(f"File {file_name} not found")
    except csv.Error:
        logging.error(f"Failed to read {file_name}")

def read_para_file_atv(file_name):
    global para_file_atv
    try:
        with open(file_name, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                para_file_atv.append(row)
    except FileNotFoundError:
        logging.error(f"File {file_name} not found")
    except csv.Error:
        logging.error(f"Failed to read {file_name}")

def read_para_file_safety(file_name):
    global para_file_safety
    try:
        with open(file_name, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                para_file_safety.append(row)
    except FileNotFoundError:
        logging.error(f"File {file_name} not found")
    except csv.Error:
        logging.error(f"Failed to read {file_name}")

def read_error_file_safety(file_name):
    global error_file_safety
    try:
        with open(file_name, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                error_file_safety.append(row)
    except FileNotFoundError:
        logging.error(f"File {file_name} not found")
    except csv.Error:
        logging.error(f"Failed to read {file_name}")

def display_varlist():
    for var in var_list:
        print(var)

def display_objectlist():
    for obj in lxm_object_list:
        print(obj)

def main():
    enum_number_init('enum_number.xml')
    read_var_list_file('var_list.csv')
    read_lxm_object_list_file('lxm_object_list.csv')
    read_parameter_file_atv_old('parameter_file_atv_old.csv')
    read_para_file_atv('para_file_atv.csv')
    read_para_file_safety('para_file_safety.csv')
    read_error_file_safety('error_file_safety.csv')
    display_varlist()
    display_objectlist()

if __name__ == '__main__':
    main()