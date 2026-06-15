from flask import Flask,session
import mysql.connector

app=Flask(__name__)

#MySQL database Connection
con=mysql.connector.connect(
    host='localhost',
    user='root',
    password='@Ajith@9751',
    database='library_mangement'
)
if con.is_connected:
    print("Database connect Successfully")
else:
    print("Database Connection Fails")

#login Page

if __name__=="__main__":
    app.secert_key="Ajith123"
    app.run(debug=True,port=6000)