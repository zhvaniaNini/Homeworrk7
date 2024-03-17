import sqlite3

connection = sqlite3.connect('employee.db')
c = connection.cursor()

c.execute("CREATE TABLE IF NOT EXISTS employee(id INTEGER PRIMARY KEY AUTOINCREMENT, first_name TEXT, last_name TEXT, "
          "age INTEGER)")
