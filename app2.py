import sqlite3 as sql
from flask import Flask, render_template, redirect, request, url_for, session, flash
#import bcrypt
e_id=0
app2 = Flask(__name__,template_folder='login_template\colorlib-regform-16',static_folder='login_template\colorlib-regform-16\static')
app2.secret_key = "abc"  
@app2.route('/')
def home():
    return render_template("registration.html")

@app2.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        global e_id
        e_id = request.form['e_id']
        username = request.form['username']
        password = request.form['password']
        role = request.form['role']
        con=sql.connect("employee.db")
        with sql.connect("employee.db") as con:
            cur=con.cursor()
            if role=='Employee':
                cur.execute("SELECT * FROM emp_login WHERE emp_id = ? and emp_username=? and emp_password=?", (e_id,username,password))
                data=cur.fetchall()
                if len(data)!=1:
                    return redirect(url_for('registration'))
                else:
                    return redirect(url_for('sepm'))
            elif role=='Admistrator':
                cur.execute("SELECT * FROM admin_login WHERE admin_id = ? and admin_username=? and admin_password=?", (e_id,username,password))
                data=cur.fetchall()
                if len(data)!=1:
                    return redirect(url_for('registration'))
                else:
                    return redirect(url_for('sepm'))
            #else:
                #flash("Format of the Employee ID is incorrect") 
            con.commit()
        return redirect(url_for('login'))
    else:
        return render_template('login.html')
@app2.route('/registration', methods=['GET', 'POST'])
def registration():
    if request.method == 'POST':
        global e_id
        e_id = request.form['e_id']
        username = request.form['username']
        password = request.form['password']
        role = request.form['role']
        con=sql.connect("employee.db")
        with sql.connect("employee.db") as con:
            cur=con.cursor()
            if role=='Employee':
                cur.execute("INSERT INTO emp_login VALUES (?, ?, ?)" , (e_id,username,password))
                #flash("You are successfuly registered!")  
            elif role=='Admistrator':
                cur.execute("INSERT INTO admin_login VALUES (?, ?, ?)" , (e_id,username,password))
                #flash("You are successfuly registered!") 
            #else:
                #flash("Format of the Employee ID is incorrect") 
            con.commit()
        return redirect(url_for('login'))
    else:
        return render_template('registration.html')

@app2.route('/sepm', methods=['GET', 'POST'])
def sepm():
    if request.method == 'POST':
        return render_template('index.html')
    else:
        return render_template('index.html')

@app2.route('/salary',methods=['GET','POST'])
def salary():
    if request.method == 'POST':
        return render_template('salary.html')
    else:
        global e_id
        con=sql.connect("employee.db")
        con.row_factory = sql.Row
        cur=con.cursor()
        cur.execute("select * from salary where emp_id = ?", (e_id,))
        rows = cur.fetchall()
        return render_template("salary.html", rows = rows)

@app2.route('/attendance', methods=['GET', 'POST'])
def attendance():
    if request.method == 'POST':
        return render_template('attendance.html')
    else:
        global e_id
        con=sql.connect("employee.db")
        con.row_factory = sql.Row
        cur=con.cursor()
        cur.execute("select * from attendance where emp_id = ?", (e_id,))
        rows = cur.fetchall()
        return render_template("attendance.html", rows = rows)

@app2.route('/leaves', methods=['GET', 'POST'])
def leaves():
    if request.method == 'POST':
        return render_template('leaves.html')
    else:
        global e_id
        con=sql.connect("employee.db")
        con.row_factory = sql.Row
        cur=con.cursor()
        cur.execute("select * from leaves where emp_id = ?", (e_id,))
        rows = cur.fetchall()
        return render_template("leaves.html", rows = rows)

@app2.route('/login_cred', methods=['GET', 'POST'])
def login_cred():
    if request.method == 'POST':
        return render_template('login_cred.html')
    else:
        global e_id
        con=sql.connect("employee.db")
        con.row_factory = sql.Row
        cur=con.cursor()
        cur.execute("select * from emp_login where emp_id = ?", (e_id,))
        rows = cur.fetchall()
        return render_template("login_cred.html", rows = rows)

@app2.route('/official', methods=['GET', 'POST'])
def official():
    if request.method == 'POST':
        return render_template('official.html')
    else:
        global e_id
        con=sql.connect("employee.db")
        con.row_factory = sql.Row
        cur=con.cursor()
        cur.execute("select * from official where id = ?", (e_id,))
        rows = cur.fetchall()
        return render_template("official.html", rows = rows)

@app2.route('/editusername', methods=['GET', 'POST'])
def edit_uname():
    if request.method == 'GET':
        return render_template('login_cred.html')
    else:
        global e_id
        e_id=request.form['e_id']
        username=request.form['username']
        con=sql.connect("employee.db")
        con.row_factory = sql.Row
        cur=con.cursor()
        cur.execute("UPDATE emp_login SET emp_username= ? where emp_id = ?", (username,e_id,))
        con.commit()
        return redirect(url_for('login_cred'))

@app2.route('/editpwd', methods=['GET', 'POST'])
def edit_pwd():
    if request.method == 'GET':
        return render_template('login_cred.html')
    else:
        global e_id
        e_id=request.form['e_id']
        password=request.form['password']
        con=sql.connect("employee.db")
        con.row_factory = sql.Row
        cur=con.cursor()
        cur.execute("UPDATE emp_login SET emp_password= ? where emp_id = ?", (password,e_id,))
        con.commit()
        return redirect(url_for('login_cred'))

@app2.route('/update_entry', methods=['GET', 'POST'])
def entry_time():
    if request.method == 'GET':
        return render_template('attendance.html')
    else:
        global e_id
        e_id=request.form['e_id']
        entry=request.form['entry']
        con=sql.connect("employee.db")
        con.row_factory = sql.Row
        cur=con.cursor()
        cur.execute("UPDATE attendance SET entry_time= ? where emp_id = ?", (entry,e_id,))
        con.commit()
        return redirect(url_for('attendance'))

@app2.route('/update_exit', methods=['GET', 'POST'])
def exit_time():
    if request.method == 'GET':
        return render_template('attendance.html')
    else:
        global e_id
        e_id=request.form['e_id']
        exittime=request.form['exittime']
        con=sql.connect("employee.db")
        con.row_factory = sql.Row
        cur=con.cursor()
        cur.execute("UPDATE attendance SET exit_time= ? where emp_id = ?", (exittime,e_id,))
        con.commit()
        return redirect(url_for('attendance'))

@app2.route('/edit_name', methods=['GET', 'POST'])
def name():
    if request.method == 'GET':
        return render_template('official.html')
    else:
        global e_id
        e_id=request.form['e_id']
        name2=request.form['name']
        con=sql.connect("employee.db")
        con.row_factory = sql.Row
        cur=con.cursor()
        cur.execute("UPDATE official SET name= ? where id = ?", (name2,e_id,))
        con.commit()
        return redirect(url_for('official'))

@app2.route('/edit_email', methods=['GET', 'POST'])
def emailid():
    if request.method == 'GET':
        return render_template('official.html')
    else:
        global e_id
        e_id=request.form['e_id']
        email=request.form['email']
        con=sql.connect("employee.db")
        con.row_factory = sql.Row
        cur=con.cursor()
        cur.execute("UPDATE official SET email= ? where id = ?", (email,e_id,))
        con.commit()
        return redirect(url_for('official'))

@app2.route('/edit_phone', methods=['GET', 'POST'])
def phonenum():
    if request.method == 'GET':
        return render_template('official.html')
    else:
        global e_id
        e_id=request.form['e_id']
        phone=request.form['phone']
        con=sql.connect("employee.db")
        con.row_factory = sql.Row
        cur=con.cursor()
        cur.execute("UPDATE official SET phone_num= ? where id = ?", (phone,e_id,))
        con.commit()
        return redirect(url_for('official'))

if __name__=="__main__":
    app2.run(debug=True)