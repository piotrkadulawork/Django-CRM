import pymysql

dataBase = pymysql.connect(
    host='localhost',
    user='root',
    password='7FdsYLq3T7Bo!'
)

cursorObject = dataBase.cursor()
cursorObject.execute("CREATE DATABASE elderco")
print("All done")