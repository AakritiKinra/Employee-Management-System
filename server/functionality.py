#functionality queries

import mysql.connector

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="aakriti",
  database="employee"
)

mycursor = mydb.cursor(buffered=True)

#login
#take username, password and role as input
'''
uname="rthth"
pword="htrh"
role="Thtrh"
if role=="Employee":
  #check if credentials are correct from emp_login
  #go to employee dashboard and only display details of that employee
else:
  #check if credentials are correct from admin_login
  #go to admin dashboard
'''
#employee dashboard

#official details
'''
id=101
sql="SELECT * FROM official WHERE id = %s"                                             #view official details
val=(id,)
mycursor.execute(sql,val)
myresult = mycursor.fetchall()
print(myresult)
print(myresult[0][0])       #id
print(myresult[0][1])       #name
print(myresult[0][2])       #join date
print(myresult[0][3])       #designation
print(myresult[0][4])       #department
print(myresult[0][5])       #monthly salary
print(myresult[0][6])       #email id
print(myresult[0][7])       #phone number

id=101                                                                                 #edit name
nameinput='Druvin Sharma'
sql="UPDATE official SET name= %s WHERE id = %s"
val=(nameinput,id)
mycursor.execute(sql,val)
mydb.commit()

id=101                                                                                 #edit email
emailinput='druvin@gmail.com'
sql="UPDATE official SET email= %s WHERE id = %s"
val=(emailinput,id)
mycursor.execute(sql,val)
mydb.commit()

id=101                                                                                #edit phone number
phoneinput='9263836610'
sql="UPDATE official SET phone_num= %s WHERE id = %s"
val=(phoneinput,id)
mycursor.execute(sql,val)
mydb.commit()
'''
#enter entry and exit time
#use datetime.now to enter the date and time at that particular time of entering data in the table
'''
sql="INSERT INTO attendance (emp_id, entry_time) VALUES (%s, %s)"                     #enter entry time
val=(104,'08:00:54')
mycursor.execute(sql, val)
mydb.commit()

sql="INSERT INTO attendance (emp_id, exit_time) VALUES (%s, %s)"                      #enter exit time
val=(104,'08:00:54')
mycursor.execute(sql, val)
mydb.commit()

id=101
sql="SELECT * FROM attendance WHERE emp_id = %s"                                     #view entry exit time
val=(101,)
mycursor.execute(sql,val)
myresult = mycursor.fetchall()
print(myresult)
print(myresult[0][0])       #emp_id
print(myresult[0][1])       #entry
print(myresult[0][2])       #exit
'''
#view leaves
'''
id=101
sql="SELECT * FROM leaves WHERE emp_id = %s"
val=(101,)
mycursor.execute(sql,val)
myresult = mycursor.fetchall()
print(myresult)
print(myresult[0][0])       #emp_id
print(myresult[0][1])       #allowed
print(myresult[0][2])       #taken
print(myresult[0][3])       #left
'''
#view salary details
'''
id=101
sql="SELECT * FROM salary WHERE emp_id = %s"
val=(103,)
mycursor.execute(sql,val)
myresult = mycursor.fetchall()
print(myresult)
print(myresult[0][0])       #emp_id
print(myresult[0][1])       #monthly salary
print(myresult[0][2])       #bonus
print(myresult[0][3])       #deduction
'''
#username and password
'''
id=101
userinput='druvin'
sql="UPDATE emp_login SET emp_username= %s WHERE emp_id = %s"                         #change username
val=(userinput,id)
mycursor.execute(sql,val)
mydb.commit()

id=101
pwdinput='hello'
sql="UPDATE emp_login SET emp_password= %s WHERE emp_id = %s"                         #change password
val=(pwdinput,id)
mycursor.execute(sql,val)
mydb.commit()

sql="SELECT * FROM emp_login WHERE emp_id = %s"                                       #view username and password
val=(101,)
mycursor.execute(sql,val)
myresult = mycursor.fetchall()
print(myresult)
print(myresult[0][0])       #emp_id
print(myresult[0][1])       #username
print(myresult[0][2])       #password
'''

#admin dashboard

#view official details of an employee
'''
id=101
sql="SELECT * FROM official WHERE id = %s"                                             #view official details
val=(id,)
mycursor.execute(sql,val)
myresult = mycursor.fetchall()
print(myresult)
print(myresult[0][0])       #id
print(myresult[0][1])       #name
print(myresult[0][2])       #join date
print(myresult[0][3])       #designation
print(myresult[0][4])       #department
print(myresult[0][5])       #monthly salary
print(myresult[0][6])       #email id
print(myresult[0][7])       #phone number
'''
#edit official details of existing employees
#edit name
'''
name="abcd"
id=101
sql="UPDATE official SET name= %s WHERE id = %s"           
val=(name,id)
mycursor.execute(sql,val)
mydb.commit()
'''
#edit join date
'''
join_date="20-03-19"
id=101
sql="UPDATE official SET join_date= %s WHERE id = %s"           
val=(join_date,id)
mycursor.execute(sql,val)
mydb.commit()
'''
#edit designation
'''
designation="junior"
id=101
sql="UPDATE official SET designation= %s WHERE id = %s"           
val=(designation,id)
mycursor.execute(sql,val)
mydb.commit()
'''
#edit department
'''
department="HR"
id=101
sql="UPDATE official SET department= %s WHERE id = %s"           
val=(department,id)
mycursor.execute(sql,val)
mydb.commit()
'''
#edit monthly salary
'''
monthly_salary=20000.00
id=101
sql="UPDATE official SET monthly_salary= %s WHERE id = %s"         
val=(monthly_salary,id)
mycursor.execute(sql,val)
sql2="UPDATE salary SET monthly_salary= %s WHERE emp_id = %s"             #change in salary table
val2=(monthly_salary,id)
mycursor.execute(sql2,val2)
mydb.commit()
'''
#edit email id
'''
email="ak@gmail.com"
id=101
sql="UPDATE official SET email= %s WHERE id = %s"           
val=(email,id)
mycursor.execute(sql,val)
mydb.commit()
'''
#edit phone number
'''
phone="748292750481"
id=101
sql="UPDATE official SET phone_num= %s WHERE id = %s"           
val=(phone,id)
mycursor.execute(sql,val)
mydb.commit()
'''
#add new employee to the database
'''
id=
name=
join_date=
designation=
department=
salary=
email=
phone=

sql="SELECT EXISTS(SELECT * from official WHERE id= %s )"
val=id
mycursor.execute(sql,val)
myresult=mycursor.fetchall()
print(myresult[0][0])

if(myresult[0][0]==0):
  sql="INSERT INTO official VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
  val=(id,name,join_date,designation,department,salary,email,phone)
  mycursor.execute(sql, val)
  mydb.commit()
  print("Official details for the employee have been added in the database")
else:
  print("Official details of this employee are already in the database")
'''
#salary of any employee
'''
id=101
sql="SELECT * FROM salary WHERE emp_id = %s"
val=(103,)
mycursor.execute(sql,val)
myresult = mycursor.fetchall()
print(myresult)
print(myresult[0][0])       #emp_id
print(myresult[0][1])       #monthly salary
print(myresult[0][2])       #bonus
print(myresult[0][3])       #deduction

id=101
salaryinput=50000.00
sql="UPDATE salary SET monthly_salary= %s WHERE emp_id = %s"                    #change monthly salary
val=(salaryinput,id)
mycursor.execute(sql,val)
sql2="UPDATE salary SET monthly_salary= %s WHERE emp_id = %s" 
val2=(salaryinput,id)
mycursor.execute(sql2,val2)                                                     #change in official table
mydb.commit()

id=101
bonusinput=2500.00
sql="UPDATE salary SET bonus= %s WHERE emp_id = %s"                             #change bonus
val=(bonusinput,id)
mycursor.execute(sql,val)
mydb.commit()

id=101
deductinput=1500.00
sql="UPDATE salary SET deduction= %s WHERE emp_id = %s"                         #change deduction
val=(deductinput,id)
mycursor.execute(sql,val)
mydb.commit()
'''
#view entry and exit time of employees
'''
id=101
sql="SELECT * FROM attendance WHERE emp_id = %s"
val=(101,)
mycursor.execute(sql,val)
myresult = mycursor.fetchall()
print(myresult)
print(myresult[0][0])       #emp_id
print(myresult[0][1])       #entry
print(myresult[0][2])       #exit
'''
#view and edit leaves of any employee
'''
id=101                                                                                 #view leaves
sql="SELECT * FROM leaves WHERE emp_id = %s"
val=(101,)
mycursor.execute(sql,val)
myresult = mycursor.fetchall()
print(myresult)
print(myresult[0][0])       #emp_id
print(myresult[0][1])       #allowed
print(myresult[0][2])       #taken
print(myresult[0][3])       #left
'''
#edit allowed number of leaves
'''
id=101
all_leaves=10
sql="UPDATE leaves SET leaves_allowed= %s WHERE emp_id = %s"                   
val=(all_leaves,id)
mycursor.execute(sql,val)
mydb.commit()
'''
#edit leaves taken and left
'''
id=101
leaves_taken=10
sql="UPDATE leaves SET leaves_taken=(leaves_taken+%s) WHERE emp_id = %s"                    #leaves taken       
val=(leaves_taken,id)
mycursor.execute(sql,val)


sql2="UPDATE leaves SET leaves_left=(leaves_left-%s) WHERE emp_id = %s"                     #leaves left
val2=(leaves_taken,id)
mycursor.execute(sql2,val2)

mydb.commit()
'''
#change username password of admin in admin_login table
'''
id=1101
userinput='samar'
sql="UPDATE admin_login SET admin_username= %s WHERE admin_id = %s"                         #change username
val=(userinput,id)
mycursor.execute(sql,val)
mydb.commit()

id=1101
pwdinput='sp_password'
sql="UPDATE admin_login SET admin_password= %s WHERE admin_id = %s"                         #change password
val=(pwdinput,id)
mycursor.execute(sql,val)
mydb.commit()

id=1101
sql="SELECT * FROM admin_login WHERE admin_id = %s"                                       #view username and password
val=(id,)
mycursor.execute(sql,val)
myresult = mycursor.fetchall()
print(myresult)
print(myresult[0][0])       #admin_id
print(myresult[0][1])       #username
print(myresult[0][2])       #password
'''
