import csv
import os.path
from os import path

def trim_values(table: list) -> list:
    for i in range(len(table)):
        for j in range(len(table[i])):
            table[i][j] = table[i][j].strip()
            if table[i][j][0] == '\"':
                table[i][j] = table[i][j][1:-1]  
    return table 

def get_full_name(filename: str) -> str:
    return filename if filename[-4:] == '.csv' else filename + '.csv'

def print_dict(data: dict) -> None:
    for item in data:
        for key, value in item.items():
            print('%-6s:' % key, value)
        print()

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
    for row in table:
        item = {}
        for i in range(len(header)):
            item[header[i]] = row[i]
        data.append(item)
    # print_dict(data)
    return data
