# Running this file will show the tables in the database

import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="yourpassword", database="sample")

mycursor = mydb.cursor()


# This is used to show the table
mycursor.execute("Show tables")

for tb in mycursor:
    print(tb)