from flask import Flask,session,request,redirect,render_template,url_for
import mysql.connector
from werkzeug.security import generate_password_hash,check_password_hash

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
@app.route('/',methods=['GET','POST'])
def login():
    if request.method=='POST':
        username=request.form['username']
        password=request.form['password']
        hash_password = generate_password_hash(password)
        res=con.cursor()
        sql='select * from login where username=%s and password=%s'
        value=(username,hash_password)
        res.execute(sql,value)
        user=res.fetchone()

        #Login functions
        if user and check_password_hash(user['password'],password):
            session[user] = username
            return redirect(url_for('home'))
        else:
            return 'Invaild username or password'
    return render_template('login.html')


if __name__=="__main__":
    app.secert_key="Ajith123"
    app.run(debug=True,port=6000)