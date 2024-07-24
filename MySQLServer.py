import mysql.connector
from mysql.connector import errorcode

try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="ONEDIRECTION210410@9461"
    )
    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
    print("Database 'alx_book_store' created successfully!")
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    else:
        print(f"Error: {err}")
finally:
    if (mydb.is_connected()):
        mycursor.close()
        mydb.close()
