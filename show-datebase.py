# Running this file will show us the different databases that we have in mysql

import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="yourpassword")

mycursor = mydb.cursor()

mycursor.execute("Show databases")

for db in mycursor:
    print(db)