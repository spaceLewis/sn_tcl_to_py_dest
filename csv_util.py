

import csv
import re
import os

EMPTY_FIELD = ''
NEW_LINE_SEPARATOR = '__NEW_LINE__'
COMMA_SEPARATOR = '__COMMA__'
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def getDataFromCSVConvertedFromExcel(filePath):
    if not os.path.isfile(filePath):
        print("Invalid file path")
        return []
    data = []
    with open(filePath, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append([cell.replace(NEW_LINE_SEPARATOR, '\n').replace(COMMA_SEPARATOR, ',') for cell in row])
    return data

def excelColumnNumberToLetter(columnNumber):
    columnLetter = ''
    while columnNumber > 0:
        columnNumber, remainder = divmod(columnNumber - 1, 26)
        columnLetter = ALPHABET[remainder] + columnLetter
    return columnLetter

def excelColumnLetterToNumber(columnLetter):
    columnNumber = 0
    for i, letter in enumerate(columnLetter[::-1]):
        columnNumber += (ord(letter) - ord('A') + 1) * (26 ** i)
    return columnNumber

def getCellValue(data, row, column):
    if row < len(data) and column < len(data[0]):
        return data[row][column]
    return EMPTY_FIELD

def importCSVData(filePath):
    if not os.path.isfile(filePath):
        print("Invalid file path")
        return []
    data = []
    with open(filePath, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
    return data

def compareCSVFiles(filePath1, filePath2):
    if not os.path.isfile(filePath1) or not os.path.isfile(filePath2):
        print("Invalid file path")
        return False
    data1 = importCSVData(filePath1)
    data2 = importCSVData(filePath2)
    if len(data1) != len(data2):
        return False
    for i in range(len(data1)):
        if len(data1[i]) != len(data2[i]):
            return False
        for j in range(len(data1[i])):
            if data1[i][j] != data2[i][j]:
                return False
    return True

def importCSVLines(filePath):
    if not os.path.isfile(filePath):
        print("Invalid file path")
        return []
    lines = []
    with open(filePath, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            lines.append(row)
    return lines

def importCSVColumns(filePath):
    if not os.path.isfile(filePath):
        print("Invalid file path")
        return []
    columns = []
    with open(filePath, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            for i, cell in enumerate(row):
                if len(columns) <= i:
                    columns.append([])
                columns[i].append(cell)
    return columns

def addBlankRowsAndColumns(data):
    max_rows = max(len(row) for row in data)
    for row in data:
        while len(row) < max_rows:
            row.append(EMPTY_FIELD)
    return data

def replaceNewLinesAndCommas(data):
    for i, row in enumerate(data):
        for j, cell in enumerate(row):
            data[i][j] = cell.replace('\n', NEW_LINE_SEPARATOR).replace(',', COMMA_SEPARATOR)
    return data

def printData(data):
    for row in data:
        print(row)

def main():
    filePath = 'example.csv'
    data = getDataFromCSVConvertedFromExcel(filePath)
    data = addBlankRowsAndColumns(data)
    data = replaceNewLinesAndCommas(data)
    printData(data)

if __name__ == "__main__":
    main()