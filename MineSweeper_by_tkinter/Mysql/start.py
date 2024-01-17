import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'store8000',
    database = 'myPythonDatabase'
)

myCursor = mydb.cursor()

#myCursor.execute('CREATE TABLE customers (name VARCHAR(20), address VARCHAR(200))')

myCursor.execute("SHOW TABLES")
for x in myCursor:
  print(x)