from typeHandler import isStr, isList
import sys

SELECT = 'SELECT'
DELETE = 'DELETE'
UPDATE = 'UPDATE'
WHERE  = 'WHERE'
ORDER  = 'ORDER'
JOIN   = 'JOIN'
ASC    = 'ASC'
DESC   = 'DESC'
FROM   = 'FROM'


def get_terminal_lines() -> list:
    lines = sys.stdin.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i][:-1]
    return lines

def get_proper_data(item: str) -> list or str:
    if ',' in item:
        item = item[:-1] if item[-1] == ',' else item.strip().split(',')
    return item

def get_proper_data_values(values: list, item: list or str) -> list:
    if isList(item):
        for item in item:
            values.append(item.strip())
    
    elif isStr(item):
        values.append(item)

    return values

def get_values(data: list) -> list:
    values = []
    
    for i in range(len(data)):
        data[i] = get_proper_data(data[i])
        values = get_proper_data_values(values, data[i])
    
    return values

def process_cmd() -> list:
    lines = get_terminal_lines()
    commands = []
    
    for line in lines:
        command = {}
        line = line.split(' ')
        
        # for single word queries: SELECT, DELETE
        if len(line) == 1 and (line[0].upper() == SELECT or line[0].upper() == DELETE):
            command['action'] = line[0].upper()
            command['values'] = None
        
        else:
            # SELECT query
            if line[0].upper() == SELECT:
                command['action'] = SELECT
                command['values'] = get_values(line[1:])
            
            # WHERE query
            elif line[0].upper() == WHERE:
                command['action'] = WHERE
                values = get_values(line[1:])
                print('Values:', values)

                if len(values) >= 3:
                    attribute = values[0]
                    criteria = values[2:].join(' ')
                    
                    if criteria[0] == '\'' and criteria[-1] == '\'':
                        criteria = criteria[1:-1]
                    
                    else:
                        criteria = int(criteria)
                    
                    command['values'] = [attribute, criteria]
                
                elif len(values) == 1:
                    command['values'] = values[0].split('=')
                
                else:
                    print('Incorrect number of arguments for WHERE query')
                    quit
            
            # FROM query
            elif line[0].upper() == FROM:
                command['action'] = FROM
                command['values'] = line[1]

            # UPDATE query
            elif line[0].upper() == UPDATE:
                command['action'] = UPDATE
                command['values'] = line[1]
            
            # SET query
            elif line[0].upper() == FROM:
                command['action'] = FROM
                command['values'] = line[1]

            # JOIN ON query
            elif line[0].upper() == JOIN and line[1].upper() == 'ON':
                command['action'] = JOIN
                command['values'] = line[1:]
            
            # ORDER BY query
            elif line[0].upper() == ORDER and line[1].upper() == 'BY':
                command['action'] = ORDER

                if len(line) > 3 and line[3].upper() == DESC:
                    command['values'] = [DESC, line[2]]
                
                else:
                    command['values'] = [ASC, line[2]]
            
            # UNKNOWN
            else:
                print('Unknown command: "%s"' % line[0])
        
        commands.append(command)
    
    return commands