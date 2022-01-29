from collections import namedtuple
import csv
import os
EmployeeRecord = namedtuple('EmployeeRecord', 'name, age, title, department, paygrade')

currentDir = os.getcwd()
csv_path = currentDir + "\list\employees.csv"
employee_list = []
csv_reader = csv.reader(open(csv_path, "r"))
next(csv_reader)
for emp in map(EmployeeRecord._make, csv_reader):
    employee_list.append(emp)


import sqlite3
conn = sqlite3.connect('commanydata.db')

cur = conn.cursor()
try:
    cur.execute("create table employees (name, age, title, department, paygrade)")
except:
    pass

cur.executemany("insert into employees values (?, ?, ?, ?, ?)", employee_list)
conn.commit()

# And this is the named style:
for row in cur.execute('SELECT * FROM employees ORDER BY age'):
    print(row)

conn.close()