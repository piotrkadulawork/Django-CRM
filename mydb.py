#wywalalo blad z haslem dlatego uzywam mydb2.py
import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = '7FdsYLq3T7Bo!'
    )

#prepare a cursor object
cursorObject = dataBase.cursor()

#create a database
cursorObject.execute("CREATE DATABASE elderco")

print("All done")


