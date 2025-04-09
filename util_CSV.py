

import csv
import os

def read_csv_file(file_path):
    if not isinstance(file_path, str):
        raise TypeError("File path must be a string")
    try:
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            data = list(reader)
        return data
    except FileNotFoundError:
        raise FileNotFoundError(f"File {file_path} not found")
    except PermissionError:
        raise PermissionError(f"Permission denied to read file {file_path}")
    except Exception as e:
        raise Exception(f"An error occurred while reading file {file_path}: {str(e)}")

def write_csv_file(file_path, data):
    if not isinstance(file_path, str):
        raise TypeError("File path must be a string")
    if not isinstance(data, list) or not all(isinstance(row, list) for row in data):
        raise TypeError("Data must be a list of lists")
    try:
        with open(file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)
    except PermissionError:
        raise PermissionError(f"Permission denied to write to file {file_path}")
    except Exception as e:
        raise Exception(f"An error occurred while writing to file {file_path}: {str(e)}")

def append_csv_file(file_path, data):
    if not isinstance(file_path, str):
        raise TypeError("File path must be a string")
    if not isinstance(data, list) or not all(isinstance(row, list) for row in data):
        raise TypeError("Data must be a list of lists")
    try:
        with open(file_path, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)
    except PermissionError:
        raise PermissionError(f"Permission denied to write to file {file_path}")
    except Exception as e:
        raise Exception(f"An error occurred while appending to file {file_path}: {str(e)}")

def check_csv_file_exists(file_path):
    if not isinstance(file_path, str):
        raise TypeError("File path must be a string")
    return os.path.isfile(file_path)

def create_csv_file(file_path, data=None):
    if not isinstance(file_path, str):
        raise TypeError("File path must be a string")
    if data is not None and not isinstance(data, list) or not all(isinstance(row, list) for row in data):
        raise TypeError("Data must be a list of lists")
    try:
        with open(file_path, 'w', newline='') as file:
            if data is not None:
                writer = csv.writer(file)
                writer.writerows(data)
    except PermissionError:
        raise PermissionError(f"Permission denied to create file {file_path}")
    except Exception as e:
        raise Exception(f"An error occurred while creating file {file_path}: {str(e)}")

def delete_csv_file(file_path):
    if not isinstance(file_path, str):
        raise TypeError("File path must be a string")
    try:
        if check_csv_file_exists(file_path):
            os.remove(file_path)
    except PermissionError:
        raise PermissionError(f"Permission denied to delete file {file_path}")
    except Exception as e:
        raise Exception(f"An error occurred while deleting file {file_path}: {str(e)}")