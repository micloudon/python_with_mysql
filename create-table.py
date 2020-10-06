# Running this file will create tables in our database

import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="yourpassword", database="sample")

mycursor = mydb.cursor()


# This is used to create the table
mycursor.execute("Create table cars(make varchar(200), model varchar(200))")

mycursor.execute("Show tables")

for tb in mycursor:
    print(tb)

