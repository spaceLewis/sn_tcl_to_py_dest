

import csv
import os
import sys

# Global variables
theTestSubDirList = []
theTestDirList = []
theTopScript = ""
Geraet = ""
serialCampaignLaunch = False
Jenkins = False
JenkinsFULLCAMPAIN = False
UnifastCI = False

def get_data_from_csv_converted_from_excel(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        data = list(reader)
    return data

def excel_column_number_to_letter(column_number):
    column_letter = ""
    while column_number > 0:
        column_number, remainder = divmod(column_number - 1, 26)
        column_letter = chr(65 + remainder) + column_letter
    return column_letter

def excel_column_letter_to_number(column_letter):
    column_number = 0
    for char in column_letter:
        column_number = column_number * 26 + ord(char) - 64
    return column_number

def get_cell_value(file_path, row, column):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        data = list(reader)
    return data[row][column]

def import_csv_data(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        data = list(reader)
    return data

def compare_csv_files(file_path1, file_path2):
    data1 = import_csv_data(file_path1)
    data2 = import_csv_data(file_path2)
    differences = []
    for i in range(max(len(data1), len(data2))):
        if i >= len(data1):
            differences.append(f"Row {i+1} is missing in {file_path1}")
        elif i >= len(data2):
            differences.append(f"Row {i+1} is missing in {file_path2}")
        else:
            for j in range(max(len(data1[i]), len(data2[i]))):
                if j >= len(data1[i]):
                    differences.append(f"Cell ({i+1},{j+1}) is missing in {file_path1}")
                elif j >= len(data2[i]):
                    differences.append(f"Cell ({i+1},{j+1}) is missing in {file_path2}")
                elif data1[i][j] != data2[i][j]:
                    differences.append(f"Cell ({i+1},{j+1}) has different values in {file_path1} and {file_path2}")
    return differences

def import_csv_lines(file_path, lines):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        data = list(reader)
    return [data[i] for i in lines]

def import_csv_columns(file_path, columns):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        data = list(reader)
    return [[row[i] for i in columns] for row in data]

def main():
    global theTestSubDirList, theTestDirList, theTopScript, Geraet, serialCampaignLaunch, Jenkins, JenkinsFULLCAMPAIN, UnifastCI
    # Initialize global variables
    theTestSubDirList = []
    theTestDirList = []
    theTopScript = ""
    Geraet = ""
    serialCampaignLaunch = False
    Jenkins = False
    JenkinsFULLCAMPAIN = False
    UnifastCI = False

    # Read configuration files
    if os.path.exists('config.txt'):
        with open('config.txt', 'r') as file:
            for line in file:
                if line.startswith('theTestSubDirList='):
                    theTestSubDirList = line.split('=')[1].strip().split(',')
                elif line.startswith('theTestDirList='):
                    theTestDirList = line.split('=')[1].strip().split(',')
                elif line.startswith('theTopScript='):
                    theTopScript = line.split('=')[1].strip()
                elif line.startswith('Geraet='):
                    Geraet = line.split('=')[1].strip()
                elif line.startswith('serialCampaignLaunch='):
                    serialCampaignLaunch = line.split('=')[1].strip().lower() == 'true'
                elif line.startswith('Jenkins='):
                    Jenkins = line.split('=')[1].strip().lower() == 'true'
                elif line.startswith('JenkinsFULLCAMPAIN='):
                    JenkinsFULLCAMPAIN = line.split('=')[1].strip().lower() == 'true'
                elif line.startswith('UnifastCI='):
                    UnifastCI = line.split('=')[1].strip().lower() == 'true'

    # Enter loop to run tests based on the selected campaign mode
    while True:
        # Display menu
        print("Menu:")
        print("1. Run tests")
        print("2. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            # Execute user commands and run tests
            if serialCampaignLaunch:
                # Run tests in serial campaign mode
                for test_dir in theTestDirList:
                    for test_sub_dir in theTestSubDirList:
                        test_path = os.path.join(test_dir, test_sub_dir)
                        if os.path.exists(test_path):
                            print(f"Running tests in {test_path}")
                            # Run tests in the test directory
                            for file in os.listdir(test_path):
                                if file.endswith('.py'):
                                    test_file = os.path.join(test_path, file)
                                    print(f"Running test {test_file}")
                                    # Run the test file
                                    exec(open(test_file).read())
                        else:
                            print(f"Test directory {test_path} does not exist")
            elif Jenkins:
                # Run tests in Jenkins mode
                for test_dir in theTestDirList:
                    for test_sub_dir in theTestSubDirList:
                        test_path = os.path.join(test_dir, test_sub_dir)
                        if os.path.exists(test_path):
                            print(f"Running tests in {test_path}")
                            # Run tests in the test directory
                            for file in os.listdir(test_path):
                                if file.endswith('.py'):
                                    test_file = os.path.join(test_path, file)
                                    print(f"Running test {test_file}")
                                    # Run the test file
                                    exec(open(test_file).read())
                        else:
                            print(f"Test directory {test_path} does not exist")
            elif JenkinsFULLCAMPAIN:
                # Run tests in Jenkins full campaign mode
                for test_dir in theTestDirList:
                    for test_sub_dir in theTestSubDirList:
                        test_path = os.path.join(test_dir, test_sub_dir)
                        if os.path.exists(test_path):
                            print(f"Running tests in {test_path}")
                            # Run tests in the test directory
                            for file in os.listdir(test_path):
                                if file.endswith('.py'):
                                    test_file = os.path.join(test_path, file)
                                    print(f"Running test {test_file}")
                                    # Run the test file
                                    exec(open(test_file).read())
                        else:
                            print(f"Test directory {test_path} does not exist")
            elif UnifastCI:
                # Run tests in Unifast CI mode
                for test_dir in theTestDirList:
                    for test_sub_dir in theTestSubDirList:
                        test_path = os.path.join(test_dir, test_sub_dir)
                        if os.path.exists(test_path):
                            print(f"Running tests in {test_path}")
                            # Run tests in the test directory
                            for file in os.listdir(test_path):
                                if file.endswith('.py'):
                                    test_file = os.path.join(test_path, file)
                                    print(f"Running test {test_file}")
                                    # Run the test file
                                    exec(open(test_file).read())
                        else:
                            print(f"Test directory {test_path} does not exist")
            else:
                print("Invalid campaign mode")
        elif choice == "2":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()