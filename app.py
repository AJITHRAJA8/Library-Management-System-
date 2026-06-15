from flask import Flask,request,render_template,redirect,url_for,session
import mysql.connector
from werkzeug.security import generate_password_hash,check_password_hash

app=Flask(__name__)

#mySQL Connection
con=mysql.connector.connect(
    host='localhost',
    user='root',
    password='@Ajith@9751',
    database='library_mangement'
)
if con.is_connected:
    print('Database is connect Successfully')
else:
    print("Database Connection Failed")

#Login Route
@app.route('/',methods=['GET','POST'])
def login():
    if request.method=='POST':
        username = request.form['username']
        password = request.form['password']

        res=con.cursor(dictionary=True)
        sql='select * from login where username=%s'
        value=(username,)
        res.execute(sql,value)
        user = res.fetchone()

        if user and check_password_hash(user['password'],password):
            session['user'] = username
            return redirect(url_for('home'))
        else:
            return 'invaild username or password'
    return render_template('login.html')

#register login
@app.route('/register',methods=['GET','POST'])
def register():
    if request.method=="POST":
        username=request.form['username']
        password=request.form['password']
        conform_password=request.form['conform_password']

        if password != conform_password:
            return 'Password does not Match'
        
        #hash_password
        hash_password=generate_password_hash(password)

        res=con.cursor(dictionary=True)
        sql='insert into login (username,password) values (%s,%s)'
        value=(username,hash_password)
        try:
            res.execute(sql,value)
            con.commit()
            return redirect(url_for('login'))
        except:
            return 'Invaild username or password'
    return render_template('register.html')

@app.route('/home')
def home():
    return render_template('home.html')


if(__name__=='__main__'):
    app.secret_key="Ajith123"
    app.run(debug=True)