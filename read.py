# Running this file will display the data in the database

import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="yourpassword", database="sample")

mycursor = mydb.cursor()
mycursor.execute("Select * from cars")

myresult = mycursor.fetchall()

for row in myresult:
    print(row)
