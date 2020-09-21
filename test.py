from my_sqlite_request import MySqliteRequest

ACCOUNTS = 'accounts.csv'
TRANSACTIONS = 'transactions.csv'
GRADES = 'grades.csv'
BIOSTATS = 'biostats.csv'

def test_grades(request: MySqliteRequest, pretty: bool):
    print("\nSELECT 'First name' FROM grades:")
    request = MySqliteRequest(GRADES).select('First name')
    request.run(pretty = pretty)

    print("\nSELECT 'First name', 'Last name', 'Grade' FROM grades:")
    request = request._from(GRADES).select(['First name', 'Last name', 'Grade'])
    request.run(pretty=pretty)

    print("\nSELECT 'First name', 'Last name', 'Final', 'Grade' FROM grades ORDER BY 'Final':")
    request = request._from(GRADES).order('ASC', 'Final').select(['First name', 'Last name', 'Final', 'Grade'])
    request.run(pretty=pretty)

    print("\nSELECT 'First name', 'Last name', 'Final', 'Grade' FROM grades ORDER BY 'Final' DESC:")
    request = request._from(GRADES)
    request = request.order('DESC', 'Final')
    request = request.select(['First name', 'Last name', 'Final', 'Grade'])
    request.run(pretty=pretty)


def test_biostats(request: MySqliteRequest, pretty: bool):
    print("\nSELECT * FROM biostats WHERE sex='M'")
    request = request._from(BIOSTATS)
    request = request.select(['Name'])
    request = request.where('Sex', 'M')
    request.run(pretty=pretty)
    
    print("\nDELETE FROM biostats where sex='F'")
    print("SELECT * FROM biostats")
    request = request._from(BIOSTATS)
    request = request.where('Sex', 'F')
    request = request.delete()
    request = request.select(['Name', 'Sex'])
    request.run(pretty=pretty)

    print("\nUPDATE biostats SET Name='Sanzhar', Sex='M', Age=20 WHERE Name='Ruth'")
    request = request.update(BIOSTATS)
    request = request.where('Name', 'Ruth')
    request = request.set({'Name': 'Sanzhar', 'Sex': 'M', 'Age': 20})
    request = request.select(['Name', 'Sex', 'Age'])
    request.run(pretty=pretty)

def test_join(request: MySqliteRequest, pretty: bool):
    print("\nTransactions:")
    request = request._from(TRANSACTIONS)
    request.run(pretty=pretty)

    print("\nAccounts:")
    request = request._from(ACCOUNTS)
    request.run(pretty=pretty)

    print("\nSELECT * FROM transactions T, accounts A JOIN ON T.customerId=A.customerId")
    request = request._from(TRANSACTIONS)
    request = request.join('customerId', ACCOUNTS, 'customerId')
    request.run(pretty=pretty)

def test(pretty: bool):
    request = MySqliteRequest()
    test_grades(request, pretty)
    test_biostats(request, pretty)
    test_join(request, pretty)