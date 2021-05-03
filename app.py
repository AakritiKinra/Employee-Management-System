from flask import Flask, render_template, redirect, request, url_for, session
#from flask_mysqldb import MySQL , MySQLdb
import mysql.connector
import bcrypt

app = Flask(__name__,template_folder='login_template\colorlib-regform-16',static_folder='login_template\colorlib-regform-16\static')
#app.config['MYSQL_HOST'] = '127.0.0.1'
#app.config['MYSQL_USER'] = 'root'
#app.config['MYSQL_PASSWORD'] = 'aakriti'
#app.config['MSQL_DB'] = 'employee'
#app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
#mysql = MySQL(app)

mydb=mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='aakriti',
    database='employee'
)

@app.route('/')
def home():
    return render_template("registration.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return redirect(url_for('registration'))
    return render_template('login.html')

@app.route('/registration', methods=['GET', 'POST'])
def registration():
    if request.method == 'GET':
        return render_template('registration.html')
    else:
        e_id = request.form['e_id']
        username = request.form['username']
        password = request.form['password'].encode('utf-8')
        role = request.form['meal_preference']
        hash_password = bycrypt.hashpw(password, bycrpt.gensalt())
        
        mycursor=mydb.cursor()
        #cur = mysql.conection.cursor()
        if role=='Employee':
            sql="INSERT INTO emp_login (emp_id,emp_username,emp_password) VALUES (%s,%s,%s)"
            val=(e_id,username,hash_password)
            mycursor.execute(sql,val)
        else:
            sql="INSERT INTO admin_login (admin_id,admin_username,admin_password) VALUES (%s,%s,%s)"
            val=(e_id,username,hash_password)
            mycursor.execute(sql,val)
        mydb.commit()
        mycursor.close()
        mydb.close()
        #session['e_id'] = e_id
        #session['username'] = username
        #session['role'] = role
        return redirect(url_for('login'))
        
if __name__=="__main__":
    app.run(debug=True)