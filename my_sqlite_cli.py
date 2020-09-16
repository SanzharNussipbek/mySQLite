from my_sqlite_request import MySqliteRequest
from typeHandler import isStr, isList, print_hash
from cmdHandler import process_cmd
from test import test
import sys

def run():
    commands = process_cmd()
    for item in commands:
        print()
        print_hash(item)
        

def get_request(text: str)->list:
    data = text.split('.')
    functions = []
    values = []
    
    for item in data:
        items = item.split('(')
        functions.append(items[0])
        if items[0] != 'run':
            items[1] = items[1][:-1].split(',')
            values.append(items[1])
    
    data = {}
    for i in range(len(values)):
        data[functions[i]] = values[i]
    
    request = MySqliteRequest()
    for key, value in data.items():
        if key == 'MySqliteRequest':
            request = request._from(value[0])
        elif key == 'select':
            request = request.select(value[0])
        elif key == 'where':
            request = request.where(value[0], value[1])   
    
    request.run(pretty=True)
    
if __name__ == '__main__':
    run()
    # test(False)
