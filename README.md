# MySQLite

This project is made as a part of studying in [Qwant.kz](http://qwant.kz/) & Qwasar Silicon Valley Coding school. It is an implementation of SQLite3 using Python, with Command Line Interface support

## Structure:

1. `my_sqlite_request.py`
    - File with `MySqliteRequest` class to handle the queries
    - Supported queries:
        1. SELECT
        2. UPDATE
        3. INSERT INTO
        4. DELETE
        5. WHERE
        6. FROM
        7. ORDER BY
        8. JOIN ON
2. `my_sqlite_cli.py`
    - Main file to be run
    - Receives the command lines and executes them
3. `cmdHandler.py`
    - Handles all command line features
    - process_cmd() function processes the command lines and returns the hash with queries and their corresponding values, which are then used in execute() function in `my_sqlite_cli.py`file
4. `fileHandler.py`
    - Reads the content of the csv file
    - Writes the result of queries to a new csv file
5. `typeHandler.py`
    - Contains useful functions lie: isStr, isList, isNum, isFloat and other functions to transpose an array of validate the values of a query
6. `queries.py`
    - Contains variables for all the queries used in the project
    - Needed to avoid typos throughout the project
7. `Test files:` 
    - *biostats.csv*
    - *grades.csv*
    - *transactions.csv*
    - *accounts.csv*
    - transactions.csv and accounts.csv can be used to test `JOIN ON` query

## Features:

- The result of the query will be saved as *<filename>_new.csv.*
- All methods, except `run`, will return an instance of `my_sqlite_request`. The request is built by progressive calls and is executed by calling run.

## Limitations:

- Currently supports only 1 `WHERE` and 1 `JOIN ON` query

## How to use the program?

**Example 1**:

```
request = MySqliteRequest()
request = request._from('biostats')
request = request.select('name')
request = request.where('sex', 'F')
request.run()

Output: {'NAME': 'Elly'}
				{'NAME': 'Fran'}
				{'NAME': 'Gwen'}
				{'NAME': 'Kate'}
				{'NAME': 'Myra'}
				{'NAME': 'Page'}
				{'NAME': 'Ruth'}
```

**Example 2**:

```
MySqliteRequest('biostats').select('name').where('sex', 'F').run()
Output: {'NAME': 'Elly'}
				{'NAME': 'Fran'}
				{'NAME': 'Gwen'}
				{'NAME': 'Kate'}
				{'NAME': 'Myra'}
				{'NAME': 'Page'}
				{'NAME': 'Ruth'}
```

Using CLI:

```sql
// WARNING: need to press Command+D/Ctrl+D to run the query

// You can copy and paste the lines below to command line

SELECT name
FROM biostats
WHERE sex='F'
Output: {'NAME': 'Elly'}
				{'NAME': 'Fran'}
				{'NAME': 'Gwen'}
				{'NAME': 'Kate'}
				{'NAME': 'Myra'}
				{'NAME': 'Page'}
				{'NAME': 'Ruth'}

SELECT name, sex, age
FROM biostats
WHERE sex='M'
ORDER BY age DESC
Output: {'NAME': 'Ivan', 'SEX': 'M', 'AGE': 53}
				{'NAME': 'Bert', 'SEX': 'M', 'AGE': 42}
				{'NAME': 'Alex', 'SEX': 'M', 'AGE': 41}
				{'NAME': 'Dave', 'SEX': 'M', 'AGE': 39}
				{'NAME': 'Omar', 'SEX': 'M', 'AGE': 38}
				{'NAME': 'Neil', 'SEX': 'M', 'AGE': 36}
				{'NAME': 'Luke', 'SEX': 'M', 'AGE': 34}
				{'NAME': 'Carl', 'SEX': 'M', 'AGE': 32}
				{'NAME': 'Jake', 'SEX': 'M', 'AGE': 32}
				{'NAME': 'Hank', 'SEX': 'M', 'AGE': 30}
				{'NAME': 'Quin', 'SEX': 'M', 'AGE': 29}

UPDATE biostats
SET name='Sanzhar'
WHERE age=41
Output: {'NAME': 'Sanzhar', 'SEX': 'M', 'AGE': 41, 'HEIGHT': 74, 'WEIGHT': 170}

INSERT INTO biostats
VALUES ('Sanzhar', 'M', 20, 100, 100)
Output: {'NAME': 'Alex', 'SEX': 'M', 'AGE': 41, 'HEIGHT': 74, 'WEIGHT': 170}
				{'NAME': 'Bert', 'SEX': 'M', 'AGE': 42, 'HEIGHT': 68, 'WEIGHT': 166}
				{'NAME': 'Carl', 'SEX': 'M', 'AGE': 32, 'HEIGHT': 70, 'WEIGHT': 155}
				{'NAME': 'Dave', 'SEX': 'M', 'AGE': 39, 'HEIGHT': 72, 'WEIGHT': 167}
				{'NAME': 'Elly', 'SEX': 'F', 'AGE': 30, 'HEIGHT': 66, 'WEIGHT': 124}
				{'NAME': 'Fran', 'SEX': 'F', 'AGE': 33, 'HEIGHT': 66, 'WEIGHT': 115}
				{'NAME': 'Gwen', 'SEX': 'F', 'AGE': 26, 'HEIGHT': 64, 'WEIGHT': 121}
				{'NAME': 'Hank', 'SEX': 'M', 'AGE': 30, 'HEIGHT': 71, 'WEIGHT': 158}
				{'NAME': 'Ivan', 'SEX': 'M', 'AGE': 53, 'HEIGHT': 72, 'WEIGHT': 175}
				{'NAME': 'Jake', 'SEX': 'M', 'AGE': 32, 'HEIGHT': 69, 'WEIGHT': 143}
				{'NAME': 'Kate', 'SEX': 'F', 'AGE': 47, 'HEIGHT': 69, 'WEIGHT': 139}
				{'NAME': 'Luke', 'SEX': 'M', 'AGE': 34, 'HEIGHT': 72, 'WEIGHT': 163}
				{'NAME': 'Myra', 'SEX': 'F', 'AGE': 23, 'HEIGHT': 62, 'WEIGHT': 98}
				{'NAME': 'Neil', 'SEX': 'M', 'AGE': 36, 'HEIGHT': 75, 'WEIGHT': 160}
				{'NAME': 'Omar', 'SEX': 'M', 'AGE': 38, 'HEIGHT': 70, 'WEIGHT': 145}
				{'NAME': 'Page', 'SEX': 'F', 'AGE': 31, 'HEIGHT': 67, 'WEIGHT': 135}
				{'NAME': 'Quin', 'SEX': 'M', 'AGE': 29, 'HEIGHT': 71, 'WEIGHT': 176}
				{'NAME': 'Ruth', 'SEX': 'F', 'AGE': 28, 'HEIGHT': 65, 'WEIGHT': 131}
				{'NAME': 'Sanzhar', 'SEX': 'M', 'AGE': 20, 'HEIGHT': 100, 'WEIGHT': 100}

SELECT *
FROM transactions, accounts
JOIN ON transactions.customerId = accounts.customerId
Output: {'TRANSACTIONID': 807, 'TRANSACTIONSTATUS': 'On review', 'CUSTOMERID': 0, 'BILL_TYPE': 'Deposit', 'STATUS': 'Active'}
				{'TRANSACTIONID': 872, 'TRANSACTIONSTATUS': 'Invalid', 'CUSTOMERID': 1, 'BILL_TYPE': 'Deposit', 'STATUS': 'Blocked'}
				{'TRANSACTIONID': 486, 'TRANSACTIONSTATUS': 'Invalid', 'CUSTOMERID': 2, 'BILL_TYPE': 'Credit', 'STATUS': 'Blocked'}
				{'TRANSACTIONID': 780, 'TRANSACTIONSTATUS': 'Approved', 'CUSTOMERID': 3, 'BILL_TYPE': 'Credit', 'STATUS': 'Blocked'}
				{'TRANSACTIONID': 337, 'TRANSACTIONSTATUS': 'Approved', 'CUSTOMERID': 4, 'BILL_TYPE': 'Wallet', 'STATUS': 'Active'}
				{'TRANSACTIONID': 197, 'TRANSACTIONSTATUS': 'Invalid', 'CUSTOMERID': 5, 'BILL_TYPE': 'Credit', 'STATUS': 'Blocked'}
				{'TRANSACTIONID': 855, 'TRANSACTIONSTATUS': 'Approved', 'CUSTOMERID': 6, 'BILL_TYPE': 'Wallet', 'STATUS': 'Active'}
				{'TRANSACTIONID': 175, 'TRANSACTIONSTATUS': 'Waiting', 'CUSTOMERID': 7, 'BILL_TYPE': 'Credit', 'STATUS': 'Active'}
```