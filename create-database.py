# Running this file will create a database named sample

import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="yourpassword")

mycursor = mydb.cursor()

mycursor.execute("Create database sample")