import mysql.connector

connection=mysql.connector.connect(
    host="localhost",
    user="root",
    password="sirwalls63",
    database="classicmodels",
    port=3306
)
print("dhdhd")
if(connection.is_connected()):
    print("yipee!! DBis connected o")
else:
    print("DB could not be connected to")



