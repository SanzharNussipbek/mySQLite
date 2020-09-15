from my_sqlite_request import MySqliteRequest
import sys

def run():
    accountsFile = './test/accounts.csv'
    transactionsFile = './test/transactions.csv'
    
    request = MySqliteRequest()
    request = request._from(transactionsFile)

    request = request.join('customerId', accountsFile, 'customerId')
    
    request.run()
    
if __name__ == '__main__':
    n = len(sys.argv) 
    print("Total arguments passed:", n) 
    
    # Arguments passed 
    print("\nName of Python script:", sys.argv[0]) 
    
    print("\nArguments passed:", end = " ") 
    for i in range(1, n): 
        print(sys.argv[i], end = " ") 