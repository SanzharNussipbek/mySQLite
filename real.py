import sqlite3, csv
from fileHandler import read_csv_file, print_dict

conn = sqlite3.connect('db.db')
c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS data""")

# data = read_csv_file('./test/grades.csv')
# c.executemany("INSERT INTO data VALUES (?, ?)", data)

a_file = open("./test/grades.csv")
rows = csv.reader(a_file)
c.executemany("INSERT INTO data VALUES (?, ?)", rows)

c.execute("SELECT * FROM data")
print(c.fetchall())

conn.commit()
conn.close()