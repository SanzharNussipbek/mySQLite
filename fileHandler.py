import csv
import os.path
from os import path
from typeHandler import isNum, isFloat

# function to trim all values from the table list
def trim_values(table: list) -> list:
    for i in range(len(table)):
        for j in range(len(table[i])):
            table[i][j] = table[i][j].strip()
            if table[i][j][0] == '\"':
                table[i][j] = table[i][j][1:-1]  
    return table 

# function to get the file name with its .csv extension
def get_full_name(filename: str) -> str:
    return filename if filename[-4:] == '.csv' else filename + '.csv'

# function to read csv file and save its data into table
def read_csv_file(filename: str) -> list:
    filename = get_full_name(filename)
    table = []
    
    with open(filename, mode='r', encoding='utf-8-sig') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='\n')
        for row in csv_reader:
            table.append(row[0].split(','))   
    
    table = trim_values(table)
    header = table[0]
    table = table[1:]
    data = []
    
    # save data as rows of hashes
    for row in table:
        item = {}
        for i in range(len(header)):
            if isNum(row[i]):
                row[i] = float(row[i]) if isFloat(row[i]) else int(row[i])
            item[header[i].upper()] = row[i]
        data.append(item)
    
    return data

# function to get column names of the table from csv file
def get_table_columns(filename: str) -> list:
    filename = get_full_name(filename)
    with open(filename, mode='r', encoding='utf-8-sig') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='\n')
        for row in csv_reader:
            row[0] = row[0].split(',')
            for i in range(len(row[0])):
                row[0][i] = row[0][i].strip()
                if row[0][i][0] == '\"':
                    row[0][i] = row[0][i][1:]

                if row[0][i][-1] == '\"':
                    row[0][i] = row[0][i][:-1]
            return row[0]