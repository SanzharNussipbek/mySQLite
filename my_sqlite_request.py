from fileHandler import read_csv_file, print_dict
from typeHandler import isList, isStr, isNum, transpose, valid_order
from operator import itemgetter

class MySqliteRequest():
    def __init__(self):
        self.data = None
        self.response = None

    def _from(self, filename: str) -> object:
        self.data = read_csv_file(filename)
        self.response = self.data
        return self

    def get_column_values(self, column: str) -> list:
        values = []
        for item in self.data:
            val = {column : item[column]}
            values.append(val)
        return values

    def select(self, column_names: list or str) -> object:
        if isList(column_names):
            columns = []
            for name in column_names:
                name = name.strip()
                values = self.get_column_values(name)
                columns.append(values)
            
            columns = transpose(columns)
            
            self.response = columns
        
        elif isStr(column_names):
            values = self.get_column_values(column_names.strip())
            for i in range(len(values)):
                values[i] = [values[i]]
            self.response = values
        
        return self

    def where(self, column_name: str, criteria: any) -> object:
        result = []
        data = self.data
        
        for i in range(len(data)):
            if data[i][column_name.strip()] == criteria.strip():
                result.append(self.response[i])
        
        self.response = result
        return self

    def join(self, column1: str, filename2: str, column2: str) -> object:
        data = self.data
        data2 = read_csv_file(filename2.strip())
        
        for X in data:
            for Y in data2:
                if X[column1.strip()] == Y[column2.strip()]:
                    for key, value in Y.items():
                        if key not in X:
                            X[key] = value
                    continue
        
        self.data = data
        self.response = data
        
        return self

    def order(self, order: str, column_name: str) -> object:
        if not valid_order(order.strip()):
            return None

        self.data.sort(reverse = True if order.upper() == 'DESC' else False, key = itemgetter(column_name.strip()))
        self.response = self.data
        
        return self

    def insert(self, filename: str) -> object:
        return self._from(filename.strip())

    def values(self, item: dict) -> object:
        self.data.append(item)
        self.response = self.data
        return self

    def update(self, filename: str) -> object:
        return self._from(filename.strip())

    def set(self, data: dict) -> object:
        table = self.response

        keys = list(data.keys())
        values = list(data.values())

        for i in range(len(table)):
            for j in range(len(keys)):
                if isNum(table[i][keys[j]]) and not isNum(values[j]):
                    print('Invalid type for SET query: %s must be a number' % values[j])
                    quit
                # elif not isNum(table[i][keys[j]]) and isNum(values[j]):
                #     print('Invalid type for SET query: %d must be a string' % values[j])
                #     quit
                
                table[i][keys[j]] = values[j]
        
        self.response = table
        return self

    def delete(self) -> object:
        for item in self.response:
            if item in self.data:
                self.data.remove(item)
        self.response = self.data
        return self

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