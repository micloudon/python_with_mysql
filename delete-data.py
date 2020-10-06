# Running this file will delete data from the database, the ford mustang is deleted from the database

import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="yourpassword", database="sample")

mycursor = mydb.cursor()

sql = "DELETE FROM cars WHERE make='Ford'"

mycursor.execute(sql)

mydb.commit()