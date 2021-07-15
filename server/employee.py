import sqlite3 as db 
conn=db.connect('employee.db')
mycursor=conn.cursor()

mycursor.execute("""CREATE TABLE official (id INT NOT NULL PRIMARY KEY, name VARCHAR(255) NOT NULL, join_date DATE NOT NULL, designation VARCHAR(255) NOT NULL, department VARCHAR(255) NOT NULL, monthly_salary DECIMAL(9,2) NOT NULL, email VARCHAR(255) NOT NULL, phone_num VARCHAR(255) NOT NULL);""")
mycursor.execute("""CREATE TABLE salary (emp_id INT NOT NULL, monthly_salary DECIMAL(9,2) NOT NULL, bonus DECIMAL(9,2) NOT NULL DEFAULT 0,deduction DECIMAL(9,2) NOT NULL DEFAULT 0, FOREIGN KEY (emp_id) REFERENCES official(id));""")
mycursor.execute("""CREATE TABLE attendance (emp_id INT NOT NULL, entry_time TIME, exit_time TIME, FOREIGN KEY (emp_id) REFERENCES official(id));""")
mycursor.execute("""CREATE TABLE leaves (emp_id INT NOT NULL, leaves_allowed INT NOT NULL, leaves_taken INT NOT NULL, leaves_left INT NOT NULL, FOREIGN KEY (emp_id) REFERENCES official(id));""")
mycursor.execute("""CREATE TABLE admin_login (admin_id INT NOT NULL, admin_username VARCHAR(255) NOT NULL PRIMARY KEY, admin_password VARCHAR(255) NOT NULL, FOREIGN KEY (admin_id) REFERENCES official(id));""")
mycursor.execute("""CREATE TABLE emp_login (emp_id INT NOT NULL, emp_username VARCHAR(255) NOT NULL PRIMARY KEY, emp_password VARCHAR(255) NOT NULL, FOREIGN KEY (emp_id) REFERENCES official(id));""")

#mycursor.execute("SHOW TABLES")

#for x in mycursor:
#  print(x)

mycursor.execute("INSERT INTO official VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (101,"Druvin Sharma","20-03-19", "Officer","Sales", 25000,"druvin@gmail.com","9263836610") )                                        #employee
mycursor.execute("INSERT INTO official VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (102,"Rajeev Kumar","22-01-17", "Officer","HR",50000,"rajeev@gmail.com","80261196307"))
mycursor.execute("INSERT INTO official VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (103,"Rakesh Jain","01-01-20", "Officer","Finance", 15000,"rakesh@gmail.com","7291640091"))
mycursor.execute("INSERT INTO official VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (104,"Tanya Chawla","20-03-16", "Officer","HR", 50000,"tanya@gmail.com","9901532367"))
mycursor.execute("INSERT INTO official VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (105,"Tanuj Mahajan","20-03-19", "Officer","R&D", 75000,"tanuj@gmail.com","8804729581"))  

mycursor.execute("INSERT INTO official VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (1101,"Samar Patel","01-03-10", "Admin","HR", 75000,"j@gmail.com","9320122854"))                                                    #admin

#mycursor.execute("UPDATE official SET monthly_salary=25000.00 WHERE department='Sales'")

#mycursor.execute("SELECT * FROM official")

#myresult = mycursor.fetchall()

#for x in myresult:
#  print(x)
mycursor.execute("INSERT INTO salary (emp_id,monthly_salary,bonus) VALUES ('%s', '%s', '%s')" % (101,25000,5000))        
mycursor.execute("INSERT INTO salary (emp_id,monthly_salary) VALUES ('%s', '%s')" % (102,50000))  
mycursor.execute("INSERT INTO salary (emp_id,monthly_salary,bonus) VALUES ('%s', '%s', '%s')" % (103,15000,2500))  
mycursor.execute("INSERT INTO salary (emp_id,monthly_salary,bonus) VALUES ('%s', '%s', '%s')" % (104,50000,2500))  
mycursor.execute("INSERT INTO salary (emp_id,monthly_salary,bonus) VALUES ('%s', '%s', '%s')" % (105,75000,1000))  


mycursor.execute("INSERT INTO attendance VALUES ('%s', '%s', '%s')" % (101,'08:00:54','17:30:00'))
mycursor.execute("INSERT INTO attendance VALUES ('%s', '%s', '%s')" % (102,'08:15:38','18:10:11'))
mycursor.execute("INSERT INTO attendance VALUES ('%s', '%s', '%s')" % (103,'07:30:43','17:15:15'))

mycursor.execute("INSERT INTO leaves VALUES ('%s', '%s', '%s', '%s')" % (101,20,7,13))
mycursor.execute("INSERT INTO leaves VALUES ('%s', '%s', '%s', '%s')" % (102,20,5,15))
mycursor.execute("INSERT INTO leaves VALUES ('%s', '%s', '%s', '%s')" % (103,20,18,2))
mycursor.execute("INSERT INTO leaves VALUES ('%s', '%s', '%s', '%s')" % (104,40,21,19))
mycursor.execute("INSERT INTO leaves VALUES ('%s', '%s', '%s', '%s')" % (105,15,5,10))

mycursor.execute("INSERT INTO admin_login VALUES ('%s', '%s', '%s')" % (1101,'samar','sp_password'))

mycursor.execute("INSERT INTO emp_login VALUES ('%s', '%s', '%s')" % (101,'druvin','ds_password'))
mycursor.execute("INSERT INTO emp_login VALUES ('%s', '%s', '%s')" % (102,'rajeev','rk_password'))
mycursor.execute("INSERT INTO emp_login VALUES ('%s', '%s', '%s')" % (103,'rakesh','rj_password'))
mycursor.execute("INSERT INTO emp_login VALUES ('%s', '%s', '%s')" % (104,'tanya','tc_password'))
mycursor.execute("INSERT INTO emp_login VALUES ('%s', '%s', '%s')" % (105,'tanuj','tm_password'))

mycursor.close()
conn.commit()
conn.close()
