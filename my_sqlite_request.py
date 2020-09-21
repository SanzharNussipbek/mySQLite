from fileHandler import read_csv_file, print_dict
from typeHandler import isList, isStr, isNum, transpose, valid_order, validate_values
from operator import itemgetter
from cmdHandler import error
from sys import exit

class MySqliteRequest():

    # initialize the object with filename if is given
    def __init__(self, filename = None):
        self.data = None if not filename else read_csv_file(filename)
        self.response = self.data

    # FROM query
    def _from(self, filename: str) -> object:
        self.data = read_csv_file(filename)
        self.response = self.data
        return self

    # get values of the given column from the table
    def get_column_values(self, column: str) -> list:
        values = []
        for item in self.response:
            val = {column : item[column]}
            values.append(val)
        return values

    # SELECT query
    # Accepts one or many columns
    # Also accepts '*' to select all columns
    def select(self, column_names: list or str) -> object:
        if column_names[0] != '*':
            if isList(column_names):
                columns = []
                for name in column_names:
                    name = name.strip().upper()
                    values = self.get_column_values(name)
                    columns.append(values)
                
                columns = transpose(columns)
                
                self.response = columns
            
            elif isStr(column_names):
                column_names = column_names.strip().upper()
                values = self.get_column_values(column_names)
                for i in range(len(values)):
                    values[i] = [values[i]]
                self.response = values
        
        return self

    # WHERE query
    def where(self, column_name: str, criteria: any) -> object:
        result = []
        data = self.data
        column_name = column_name.strip().upper()
        criteria = criteria.strip().upper() if type(criteria) == str else criteria

        if type(data[0][column_name]) != type(criteria):
            error('ERROR: Invalid criteria value type')
        
        for i in range(len(data)):
            if type(data[i][column_name]) == str:

                if data[i][column_name].upper() == criteria:
                    result.append(self.response[i])
            
            else:
                if data[i][column_name] == criteria:
                    result.append(self.response[i])

        self.response = result
        return self

    # JOIN ON query to join two tables on one column
    def join(self, column1: str, filename: str, column2: str) -> object:
        filename = filename.strip()
        column1 = column1.strip().upper()
        column2 = column2.strip().upper()
        
        data = self.data
        data2 = read_csv_file(filename)

        if type(data[0][column1]) != type(data2[0][column2]):
            error('ERROR: Columns %s and %s have different data types' % (column1, column2))
        
        for X in data:
            for Y in data2:
                if X[column1] == Y[column2]:
                    for key, value in Y.items():
                        if key not in X:
                            X[key] = value
                    continue
        
        self.data = data
        self.response = data
        
        return self

    # ORDER BY query to sort the result in ASC or DESC order
    def order(self, order: str, column_name: str) -> object:
        if not valid_order(order.strip()):
            error('ERROR: Invalid value for ORDER BY')

        self.data.sort(reverse = True if order.upper() == 'DESC' else False, key = itemgetter(column_name.strip().upper()))
        self.response = self.data
        
        return self

    # INSERT INTO query
    def insert(self, filename: str) -> object:
        return self._from(filename.strip())

    # VALUES for INSERT INTO query
    def values(self, item: dict) -> object:
        for key in item:
            key = key.upper()

        if not validate_values(self.data[0], item):
            exit()
        
        self.data.append(item)
        self.response = self.data
        return self

    # UPDATE query
    def update(self, filename: str) -> object:
        return self._from(filename.strip())

    # SET for UPDATE query
    def set(self, data: dict) -> object:
        table = self.response

        keys = list(data.keys())
        for i in range(len(keys)):
            keys[i] = keys[i].upper()

        values = list(data.values())

        for i in range(len(table)):
            for j in range(len(keys)):
                if isNum(table[i][keys[j]]) and not isNum(values[j]):
                    error('ERROR: Invalid data type for SET query: %s must be a number' % values[j])
                
                table[i][keys[j]] = values[j]
        
        self.response = table
        return self

    # DELETE query
    def delete(self) -> object:
        for item in self.response:
            self.data.remove(item)
        
        self.response = self.data
        return self

    # run all the queries and save the result into the csv file
    def run(self, pretty=False):
        if pretty:
            for item in self.response:
                if len(item) == 1:
                    item = item[0]
                for key, value in item.items():
                    print(key,':',value)
                if len(item.items()) != 1:
                    print()
            return
        
        for item in self.response:
            print(item)