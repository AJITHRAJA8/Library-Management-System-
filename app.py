from flask import Flask
import mysql.connector
from werkzeug.security import generate_password_hash,check_password_hash

app=Flask(__name__)


if(__name__=='__main__'):
    app.run(debug=True)