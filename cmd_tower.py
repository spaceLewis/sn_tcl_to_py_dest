

import csv
import xml.dom.minidom as tdom
import os
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def ReadVARListFile(filename, Print=False):
    var_list = {}
    try:
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                if line:
                    key, value = line.split('=')
                    var_list[key] = value
        if Print:
            for key, value in var_list.items():
                print(f"{key} = {value}")
        return var_list
    except FileNotFoundError:
        logger.error(f"File {filename} not found")
        return None
    except Exception as e:
        logger.error(f"Error reading file {filename}: {str(e)}")
        return None

def ReadParaFile_ATV(filename):
    theATVParaNameTable = []
    theATVParaIndexTable = []
    theATVenumListTable = []
    theATVenumValueTable = []
    theATVenumNameTable = []
    try:
        doc = tdom.parse(filename)
        root = doc.documentElement
        for para in root.getElementsByTagName('parameter'):
            name = para.getElementsByTagName('name')[0].firstChild.nodeValue
            index = para.getElementsByTagName('index')[0].firstChild.nodeValue
            enum_list = para.getElementsByTagName('enum_list')[0].firstChild.nodeValue.split(',')
            enum_value = para.getElementsByTagName('enum_value')[0].firstChild.nodeValue.split(',')
            enum_name = para.getElementsByTagName('enum_name')[0].firstChild.nodeValue.split(',')
            theATVParaNameTable.append(name)
            theATVParaIndexTable.append(index)
            theATVenumListTable.append(enum_list)
            theATVenumValueTable.append(enum_value)
            theATVenumNameTable.append(enum_name)
        return theATVParaNameTable, theATVParaIndexTable, theATVenumListTable, theATVenumValueTable, theATVenumNameTable
    except FileNotFoundError:
        logger.error(f"File {filename} not found")
        return None
    except Exception as e:
        logger.error(f"Error parsing file {filename}: {str(e)}")
        return None

def ReadCSVFile(filename):
    data = []
    try:
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                data.append(row)
        return data
    except FileNotFoundError:
        logger.error(f"File {filename} not found")
        return None
    except Exception as e:
        logger.error(f"Error reading file {filename}: {str(e)}")
        return None

def ReadTXTFile(filename):
    data = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                data.append(line.strip())
        return data
    except FileNotFoundError:
        logger.error(f"File {filename} not found")
        return None
    except Exception as e:
        logger.error(f"Error reading file {filename}: {str(e)}")
        return None