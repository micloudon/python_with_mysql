# Running this file will connect and log us into mysql

import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="yourpassword")

print(mydb)

if(mydb):
    print("Connection successful")

else:
    print("Connection failed")