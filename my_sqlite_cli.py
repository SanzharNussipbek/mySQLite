import csv
import os.path
from os import path
from my_sqlite_request import MySqliteRequest

def isFile(csv_name: str) -> bool:
    return path.exists(csv_name)

def trim_values(table: list) -> list:
    for i in range(len(table)):
        for j in range(len(table[i])):
            table[i][j] = table[i][j].strip()
            if table[i][j][0] == '\"':
                table[i][j] = table[i][j][1:-1]  
    return table 

def read_csv_file(csv_name: str) -> list:
    table = []
    with open(csv_name) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='\n')
        for row in csv_reader:
            table.append(row[0].split(','))   
    return trim_values(table)

def read_csv_str(csv: str) -> list:
    table = csv.split('\n')
    for i in range(len(table)):
        table[i] = table[i].split(',')
    return trim_values(table)

def run():
    table = []
    csv = './src/grades.csv'
    table = read_csv_file(csv) if isFile(csv) else read_csv_str(csv)
    
if __name__ == '__main__':
    run()