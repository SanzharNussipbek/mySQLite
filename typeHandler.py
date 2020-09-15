def isList(var: str or list) -> bool:
    return type(var) == list

def isStr(var: str or list) -> bool:
    return type(var) == str

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