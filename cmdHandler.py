from typeHandler import isStr, isList, isNum, isFloat
from fileHandler import get_table_columns
from sys import exit, stdin
from queries import SELECT, DELETE, UPDATE, INSERT, VALUES, WHERE, ORDER, JOIN, FROM, INTO, DESC, ASC, SET

# Global variable to save columns listed in INSERT INTO query
INSERT_COLUMNS = []

# Check if given query is valid
def isQuery(query: str) -> bool:
    return query in [SELECT, DELETE, UPDATE, INSERT, VALUES, WHERE, ORDER, JOIN, FROM, INTO, SET]

# Get command lines
def get_terminal_lines() -> list:
    lines = stdin.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i][:-1]
    return lines

# Get proper data: splitted by a comma
def get_proper_data(item: str) -> list or str:
    if ',' in item:
        item = item[:-1] if item[-1] == ',' else item.strip().split(',')
    return item

# Get proper data values: stripped
def get_proper_data_values(values: list, item: list or str) -> list:
    if isList(item):
        for item in item:
            values.append(item.strip())
    
    elif isStr(item):
        values.append(item)

    return values

# Get separated values: by comma
def get_separated_values(data: list) -> list:
    values = []
    
    for i in range(len(data)):
        data[i] = get_proper_data(data[i])
        values = get_proper_data_values(values, data[i])
    
    return values

# Get item values: [key: value]
def get_item_values(data: list) -> list:
    values = ' '.join(data).split(',')
            
    for i in range(len(values)):
        item = values[i].split('=')
        attribute = item[0].strip()
        criteria = item[1].strip()
        criteria = criteria[1:-1] if criteria[0] == '\'' and criteria[-1] == '\'' else int(criteria)
        values[i] = [attribute, criteria]
    
    return values

# Print error message and quit
def error(message: str):
    print(message)
    exit()

# Main function to process the command line
def process_cmd() -> dict:
    lines = get_terminal_lines()
    commands = {}

    # Save all the actions
    commands['actions'] = []
    
    for line in lines:
        line = line.split(' ')
        query = line[0].upper()

        # check if the query is valid
        if not isQuery(query):
            error('ERROR: Unknown query "%s"' % query)
        
        # add the query into the list
        commands['actions'].append(query)
        
        # SELECT query
        if query == SELECT or query == DELETE:
            commands[query] = get_separated_values(line[1:])

        # WHERE query
        elif query == WHERE:
            if not (SELECT in commands or UPDATE in commands or DELETE in commands):
                error('ERROR: No SELECT, UPDATE or DELETE query was found')
            
            commands[WHERE] = get_item_values(line[1:])
        
        # FROM query
        elif query == FROM:
            if not (SELECT in commands or DELETE in commands):
                error('ERROR: No SELECT or DELETE query was found')
            
            commands[FROM] = get_separated_values(line[1:])

        # UPDATE query
        elif query == UPDATE:
            commands[UPDATE] = line[1]

        # SET
        elif query == SET:
            if UPDATE not in commands:
                error('ERROR: No UPDATE query was found')
            
            values = get_item_values(line[1:])
            hashValues = {}

            for item in values:
                hashValues[item[0]] = item[1]

            commands[SET] = hashValues

        # INSERT INTO query
        elif query == INSERT:
            if line[1].upper() != INTO:
                error('ERROR: cannot find "INTO" statement for INSERT INTO query')
            
            if len(line) < 3:
                error('ERROR: cannot find the table name')

            table_columns = get_table_columns(line[2])
            
            if len(line) > 3:
                line[3] = line[3][1:]
                line[-1] = line[-1][:-1]
                INSERT_COLUMNS = get_separated_values(line[3:])
                
                for i in range(len(INSERT_COLUMNS)):
                    INSERT_COLUMNS[i] = INSERT_COLUMNS[i][1:-1]
                    if INSERT_COLUMNS[i] not in table_columns:
                        error('ERROR: cannot find column "%s" in "%s" table' % (INSERT_COLUMNS[i], line[2]))
            else:
                INSERT_COLUMNS = table_columns

            commands[INSERT] = line[2]
        
        # VALUES for INSERT INTO query
        elif query == VALUES:
            if len(line) == 1:
                error('ERROR: no values were found for INSERT INTO query')

            values = get_separated_values(line[1:])
            values[0] = values[0][1:]
            values[-1] = values[-1][:-1]

            if len(values) != len(INSERT_COLUMNS):
                error('ERROR: invalid number of arguments for VALUES')

            hashValues = {}
            for i in range(len(values)):
                if isNum(values[i]):
                    values[i] = float(values[i]) if isFloat(values[i]) else int(values[i])
                else:
                    values[i] = values[i][1:-1]
                hashValues[INSERT_COLUMNS[i].upper()] = values[i]
            
            commands[VALUES] = hashValues

        # JOIN ON query
        elif query == JOIN:
            if line[1].upper() != 'ON':
                error('ERROR: cannot find "ON" statement for JOIN ON query')

            if SELECT not in commands:
                error('No SELECT query was found')

            values = ' '.join(line[2:]).split('=')
            for i in range(len(values)):
                item = values[i].strip()
                item = item.split('.')
                values[i] = item

            commands[JOIN] = [values[0][1], values[1][0], values[1][1]]
        
        # ORDER BY query
        elif query == ORDER:
            if line[1].upper() != 'BY':
                error('ERROR: cannot find statement "BY" for ORDER BY query')

            if SELECT not in commands:
                error('No SELECT query was found')
            
            commands[ORDER] = [DESC, line[2]] if len(line) > 3 and line[3].upper() == DESC else [ASC, line[2]]
    
    return commands