import csv

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

def isList(var: str or list) -> bool:
    return type(var) == list

def isStr(var: str or list) -> bool:
    return type(var) == str

class MySqliteRequest():
    def __init__(self):
        self.table = None
        self.response = None

    def _from(self, table_name: str) -> object:
        self.table = read_csv_file(table_name)
        self.response = self.table
        return self

    def get_column_values(self, index: int) -> list:
        values = []
        for row in self.table[1:]:
            values.append(row[index])
        return values

    def select(self, column_names: list or str) -> object:
        if isList(column_names):
            columns = []
            for name in column_names:
                index = self.table.index(name)
                values = self.get_column_values(index)
                columns.append(values)
            
            self.response = columns
        
        elif isStr(column_names):
            index = self.table.index(column_names)
            self.response = self.get_column_values(index)
        
        else:
            print('Invalid argument for SELECT query.\n')
            return None
        
        return self

    def where(self, column_name: str, criteria: any) -> object:
        result = []
        index = self.table.index(column_name)

        for row in self.table:
            if row[index] == criteria:
                result.append(self.response[index])
        self.response = result
        return self

    def join(self, column_on_db_a: str, filename_db_b: str, column_on_db_b: str):
        pass

    def order(self, order: str, column_name: str) -> object:
        pass

    def insert(self, table_name: str) -> object:
        pass

    def values(self, data) -> object:
        pass

    def update(self, table_name: str) -> object:
        pass

    def set(self, data) -> object:
        pass

    def delete(self) -> object:
        pass

    def run(self):
        pass