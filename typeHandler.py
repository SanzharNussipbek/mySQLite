def isList(var: str or list) -> bool:
    return type(var) == list

def isStr(var: str or list) -> bool:
    return type(var) == str

def transpose(data: list) -> list:
    data = list(zip(*data))
    for i in range(len(data)):
        data[i] = list(data[i])
    return data

def valid_order(order: str) -> bool:
    return order.upper() == 'ASC' or order.upper() == 'DESC'