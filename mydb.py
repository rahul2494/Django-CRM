import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    #passwd = 'password123'
    passwd = 'rootpassword'
)

# prepare cursor object
cursorObj = dataBase.cursor()

# create a database
cursorObj.execute("CREATE DATABASE elderco")

print("All Done!")