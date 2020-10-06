# Deletes Table from db

import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="yourpassword", database="mickeydb")

mycursor = mydb.cursor()

sql = "DROP TABLE employee"

mycursor.execute(sql)

mydb.commit()