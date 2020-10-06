# Running this file will update data that is already in the database

import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="yourpassword", database="sample")

mycursor = mydb.cursor()

sql = "UPDATE cars SET model='Prius' WHERE make='Toyata'"
mycursor.execute(sql)

mydb.commit()