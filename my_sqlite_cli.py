from my_sqlite_request import MySqliteRequest
from typeHandler import isStr, isList, print_hash
from cmdHandler import process_cmd
from test import test
import sys
from queries import SELECT, DELETE, UPDATE, INSERT, VALUES, WHERE, ORDER, JOIN, FROM, INTO, DESC, ASC, SET

# function to execute commands
def execute(commands: dict):
    actions = commands['actions']
    request = MySqliteRequest()

    if FROM in actions:
        values = commands[FROM]
        request = request._from(values[0])

    if UPDATE in actions:
        values = commands[UPDATE]
        request = request.update(values)

    if INSERT in actions:
        values = commands[INSERT]
        request = request.update(values)

    if VALUES in actions:
        values = commands[VALUES]
        request = request.values(values)
    
    if JOIN in actions:
        values = commands[JOIN]
        request = request.join(values[0], values[1], values[2])

    if ORDER in actions:
        values = commands[ORDER]
        request = request.order(values[0], values[1])

    if WHERE in actions:
        values = commands[WHERE][0]
        request = request.where(values[0], values[1])

    if SET in actions:
        values = commands[SET]
        request = request.set(values)
    
    if DELETE in actions:
        request = request.delete()

    if SELECT in actions:
        values = commands[SELECT]
        request = request.select(values)
        
    request.run(pretty = False)

# function to run the program
def run():
    # get commands from command line
    commands = process_cmd()

    # execute the commands
    execute(commands)

# Don't need this function yet
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

# main
if __name__ == '__main__':
    run()

    # Uncomment the line below to test the program
    # test(pretty = False)
