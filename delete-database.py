# Deletes the entire database

import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="yourpassword")

mycursor = mydb.cursor()

sql = "DROP DATABASE mickeydb"

mycursor.execute(sql)

mydb.commit()