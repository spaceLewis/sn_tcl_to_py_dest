

import csv
import string

def excel_column_number_to_letter(n):
    result = ''
    while n > 0:
        n, remainder = divmod(n - 1, 26)
        result = string.ascii_uppercase[remainder] + result
    return result

def excel_column_letter_to_number(s):
    result = 0
    for char in s:
        result = result * 26 + string.ascii_uppercase.index(char) + 1
    return result

def get_cell_value(file_path, sheet_name, cell):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        data = list(reader)
    row = int(cell[1:]) - 1
    col = excel_column_letter_to_number(cell[0]) - 1
    return data[row][col]

def import_csv_data(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        data = list(reader)
    return data

def compare_csv_files(file_path1, file_path2, detailedView=False):
    data1 = import_csv_data(file_path1)
    data2 = import_csv_data(file_path2)
    differences = []
    max_rows = max(len(data1), len(data2))
    max_cols = max(len(data1[0]) if data1 else 0, len(data2[0]) if data2 else 0)
    for i in range(max_rows):
        if i >= len(data1):
            differences.append(f'Row {i+1} is missing in {file_path1}')
        elif i >= len(data2):
            differences.append(f'Row {i+1} is missing in {file_path2}')
        else:
            for j in range(max_cols):
                if j >= len(data1[i]):
                    data1[i].append('')
                if j >= len(data2[i]):
                    data2[i].append('')
                if data1[i][j] != data2[i][j]:
                    differences.append(f'Difference at row {i+1}, column {j+1}: {data1[i][j]}}, {data2[i][j]}}')
    if detailedView:
        for diff in differences:
            print(diff)
    return differences

def import_csv_lines(file_path, lines):
    data = import_csv_data(file_path)
    return [data[i] for i in lines]

def import_csv_columns(file_path, columns):
    data = import_csv_data(file_path)
    return [[row[i] for i in columns] for row in data]