def isList(var: str or list) -> bool:
    return type(var) == list

def isStr(var: str or list) -> bool:
    return type(var) == str

def isNum(var: str) -> bool:
    if type(var) == int: return True
    if var.isnumeric(): return True
    
    counter = 0
    for ch in var:
        if ch.isnumeric() or ch == '.':
            counter += 1
    return counter == len(var)

def isFloat(var: str) -> bool:
    return '.' in var

def transpose(data: list) -> list:
    data = list(zip(*data))
    for i in range(len(data)):
        data[i] = list(data[i])
        item = data[i][0]
        for hash in data[i][1:]:
            item.update(hash)
        data[i] = item
    return data

def valid_order(order: str) -> bool:
    return order.upper() == 'ASC' or order.upper() == 'DESC'

def print_hash(item: dict):
    for key, value in item.items():
            print(key,':',value)