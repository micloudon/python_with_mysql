# Running this file will insert data into the database

import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="yourpassword", database="sample")

mycursor = mydb.cursor()

sqlform = "insert into cars(make,model) values(%s,%s)"

cars = [("Ford", "Mustang"), ("Honda", "Civic"), ("Toyota", "Camary"), ]

mycursor.executemany(sqlform, cars)

mydb.commit()