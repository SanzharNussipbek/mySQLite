from my_sqlite_request import MySqliteRequest
import sys

ACCOUNTS = './test/accounts.csv'
TRANSACTIONS = './test/transactions.csv'
GRADES = './test/grades.csv'
BIOSTATS = './test/biostats.csv'

def test_grades(request: MySqliteRequest):
    print("\nSELECT 'First name' FROM grades:")
    request = request._from(GRADES)
    request = request.select('First name')
    request.run(pretty = False)

    print("\nSELECT 'First name', 'Last name', 'Grade' FROM grades:")
    request = request._from(GRADES)
    request = request.select(['First name', 'Last name', 'Grade'])
    request.run(pretty=False)

    print("\nSELECT 'First name', 'Last name', 'Final', 'Grade' FROM grades ORDER BY 'Final':")
    request = request._from(GRADES)
    request = request.order('ASC', 'Final')
    request = request.select(['First name', 'Last name', 'Final', 'Grade'])
    request.run(pretty=False)

    print("\nSELECT 'First name', 'Last name', 'Final', 'Grade' FROM grades ORDER BY 'Final' DESC:")
    request = request._from(GRADES)
    request = request.order('DESC', 'Final')
    request = request.select(['First name', 'Last name', 'Final', 'Grade'])
    request.run(pretty=False)


def test_biostats(request: MySqliteRequest):
    print("\nSELECT * FROM biostats WHERE sex='M'")
    request = request._from(BIOSTATS)
    request = request.select(['Name', 'Sex'])
    request = request.where('Sex', 'M')
    request.run(pretty=False)
    
    print("\nDELETE FROM biostats where sex='F'")
    print("SELECT * FROM biostats")
    request = request._from(BIOSTATS)
    request = request.where('Sex', 'F')
    request = request.delete()
    request = request.select(['Name', 'Sex'])
    request.run(pretty=False)

    print("\nUPDATE biostats SET Name='Sanzhar', Sex='M', Age=20 WHERE Name='Ruth'")
    request = request.update(BIOSTATS)
    request = request.where('Name', 'Ruth')
    request = request.set({'Name': 'Sanzhar', 'Sex': 'M', 'Age': '20'})
    request = request.select(['Name', 'Sex', 'Age'])
    request.run(pretty=False)

def test_join(request: MySqliteRequest):
    print("\nTransactions:")
    request = request._from(TRANSACTIONS)
    request.run(pretty=False)

    print("\nAccounts:")
    request = request._from(ACCOUNTS)
    request.run(pretty=False)

    print("\nSELECT * FROM transactions T, accounts A JOIN ON T.customerId=A.customerId")
    request = request._from(TRANSACTIONS)
    request = request.join('customerId', ACCOUNTS, 'customerId')
    request.run(pretty=False)

def test():
    request = MySqliteRequest()
    test_grades(request)
    test_biostats(request)
    test_join(request)


def run():
    accountsFile = './test/accounts.csv'
    transactionsFile = './test/transactions.csv'
    
    request = MySqliteRequest()
    request = request._from(transactionsFile)

    request = request.join('customerId', accountsFile, 'customerId')
    
    request.run()

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

    # for key, value in data.items():
    #     print(key, ':', value)
    
    # for key, value in data.items():
    #     if key == 'MySqliteRequest' and value[0][-4:] != '.csv':
    #         value[0] += '.csv'
    
    request = MySqliteRequest()
    for key, value in data.items():
        if key == 'MySqliteRequest':
            request = request._from(value[0])
        elif key == 'select':
            request = request.select(value[0])
        elif key == 'where':
            request = request.where(value[0], value[1])
        
    request.run(True)

    # for key, value in data.items():
    #     print(key, ':', value)
    
if __name__ == '__main__':
    # n = len(sys.argv) 
    # print("Total arguments passed:", n) 
    
    # # Arguments passed 
    # print("\nName of Python script:", sys.argv[0]) 
    
    # print("\nArguments passed:", end = " ") 
    # for i in range(1, n): 
    #     print(sys.argv[i], end = " ") 
    # test()

    values = get_request(sys.argv[1])
