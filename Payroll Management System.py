import mysql.connector as m
from datetime import datetime
from tabulate import tabulate
import os
from fpdf import FPDF
db = input("Enter the Database which you want to use:")
mydb = m.connect(host = "localhost",user = "root",password = "sricheechu_2005",database =db)
if mydb.is_connected() == True:
    print("Connection Successful")
else:
    print("Error Connecting to Mysql Database")
mycursor = mydb.cursor()
mycursor.execute("USE PAYROLL")
query="CREATE TABLE PAY(EMPNO INT,NAME CHAR(15),JOB CHAR(15),BASICSALARY INT,DA FLOAT,HRA FLOAT,GROSSSALARY FLOAT,TAX FLOAT,NETSALARY FLOAT)"
print("Table PAY is created successfully..!")
while True:
    print('\n\n\n')
    print("*"*95)  
    print("\t\t\t\t\tMENU DRIVEN PROGRAM")
    print("*"*95)
    print('\t\t\t\t1. Create a new Employee')
    print('\t\t\t\t2. View All Employee Records')
    print('\t\t\t\t3. View an Employee Payroll')
    print('\t\t\t\t4. Search Employee by Name')         
    print('\t\t\t\t5. Amend an Employee Detail')
    print('\t\t\t\t6. View Salary Slip of an Employee')
    print('\t\t\t\t7. Delete an Employee')
    print('\t\t\t\t8. Generate Monthly Payroll')
    print('\t\t\t\t9. Download Salary Slip as PDF')
    print('\t\t\t\t10. Exit')
    choice = int(input("Enter your choice:"))

    if choice == 1:
        os.system('cls')
        try:
            mydb = m.connect(host = "localhost",user = "root",password = "sricheechu_2005",database =db)
            if mydb.is_connected() == True:
                print("Connection Successful")
            else:
                print("Error Connecting to Mysql Database")
            mycursor = mydb.cursor()
            mycursor.execute("USE PAYROLL")
            print("Enter Employee Details")
            empno = int(input("Enter Employee No:"))
            name  = input("Enter Employee name:")
            job = input("Enter Employee Job:")
            basic = float(input("Enter Basic Salary of Employee:"))
            if job.lower() == 'md':
                da = basic*0.5
                hra = basic*0.35
                tax = basic*0.25
            elif job.lower() == 'engineer':
                da = basic*0.45
                hra = basic*0.30
                tax = basic*0.20
            elif job.lower() == 'hr':
                da = basic*0.40
                hra = basic*0.25
                tax = basic*0.15
            elif job.lower() == 'clerk':
                da = basic*0.35
                hra = basic*0.15
                tax = basic*0.10
            else:
                da = basic*0.30
                hra = basic*0.10
                tax = basic*0.5
            gross = basic+da+hra
            net = gross-tax
            query = "INSERT INTO PAY VALUES("+str(empno)+",'"+name+"','"+job+"',"+str(basic)+","+str(da)+","+str(hra)+","+str(gross)+","+str(tax)+","+str(net)+")"
            mycursor.execute(query)
            mydb.commit()
            mydb.close()
            print("Records are Inserted Successfully..!")
        except Exception as ex: 
                print("Oops!Something Went Wrong!",ex)

    elif choice == 2:
        os.system('cls')
        try:
            mydb = m.connect(host = "localhost",user = "root",password = "sricheechu_2005",database =db)
            mycursor = mydb.cursor()
            query = 'SELECT * FROM PAY'
            mycursor.execute(query)
            print(tabulate(mycursor,headers = ['EMPNO','NAME','JOB','BASIC SALARY','DA','HRA','GROSS SALARY','TAX','NET SALARY']))
            myrecords = mycursor.fetchall()
            for rec in myrecords:
                print(rec)
            mydb.close()
        except Exception as ex:
            print("Oops!Something Went Wrong!",ex)

    elif choice == 3:
        os.system('cls')
        try:
            mydb = m.connect(host = "localhost",user = "root",password = "sricheechu_2005",database =db)
            if mydb.is_connected() == True:
                print("Connection Successful")
            else:
                print("Error Connecting to Mysql Database")
            mycursor = mydb.cursor()
            eno = input("Enter Employee Number of the Record to be searched and displayed:")
            query = "SELECT * FROM PAY WHERE EMPNO="+eno
            mycursor.execute(query)
            print(tabulate(mycursor,headers = ['EMPNO','NAME','JOB','BASIC SALARY','DA','HRA','GROSS SALARY','TAX','NET SALARY']))
            myrecord = mycursor.fetchone()
            print('\n\nRecord Of Employee Number:'+eno)
            print(myrecord)
            c = mycursor.rowcount
            if c == -1:
                print("Sorry..! Nothing to be display..!")
            mydb.close()
        except Exception as ex:
            print("Oops!Something Went Wrong!",ex)

    elif choice == 4:
        os.system('cls')
        try:
            mydb = m.connect(host = "localhost",user = "root",password = "sricheechu_2005",database =db)
            if mydb.is_connected() == True:
                print("Connection Successful")
            else:
                print("Error Connecting to Mysql Database")
            mycursor = mydb.cursor()
            ename = input("Enter Employee Name to Search:")
            query = "SELECT * FROM PAY WHERE NAME LIKE '%"+ename+"%';"
            mycursor.execute(query)
            print(tabulate(mycursor,headers = ['EMPNO','NAME','JOB','BASIC SALARY','DA','HRA','GROSS SALARY','TAX','NET SALARY']))
            myrecord = mycursor.fetchmany()
            print(tabulate(myrecord))
            c = mycursor.rowcount
            if c == -1:
                print("Sorry..! Nothing to be display..!")
            mydb.close()
        except Exception as ex:
            print("Oops!Something Went Wrong!",ex)

    elif choice == 5:
        os.system('cls')
        try:
            mydb = m.connect(host = "localhost",user = "root",password = "sricheechu_2005",database =db)
            if mydb.is_connected() == True:
                print("Connection Successful")
            else:
                    print("Error Connecting to Mysql Database")
            mycursor = mydb.cursor()
            eno = input("Enter the Employee Number to Modify:")
            query = "SELECT * FROM PAY WHERE EMPNO="+eno
            mycursor.execute(query)
            myrecord = mycursor.fetchone()
            c = mycursor.rowcount
            if c <= 0:
                print("Employee Number"+eno+"does not exist.!!")
            else:
                mname = myrecord[1]
                mjob = myrecord[2]
                mbasic = myrecord[3]
                print("empno:",myrecord[0])
                print("name:",myrecord[1])
                print("Job:",myrecord[2])
                print("Basic:",myrecord[3])
                print("DA:",myrecord[4])
                print("HRA:",myrecord[5])
                print("Gross:",myrecord[6])
                print("Tax:",myrecord[7])
                print("Net:",myrecord[8])
                print("-"*95)
                print("Type the Required value to Modify below or Just Press Enter Button for no change:")
                ename = input("Enter Name:")
                if len(ename) > 0:
                    query = "UPDATE PAY SET NAME ='"+ename+"' WHERE EMPNO ="+eno
                    mycursor.execute(query)
                job = input("Enter Job:")
                if len(job) > 0:
                    query = "UPDATE PAY SET JOB ='"+job+"' WHERE EMPNO ="+eno
                    mycursor.execute(query)
                ebasic = input("Enter Basic Salary:")
                if  len(ebasic) > 0:
                    query = "UPDATE PAY SET BASICSALARY = "+str(float(ebasic))+" WHERE EMPNO ="+eno
                    mycursor.execute(query)
                mydb.commit()
                print("Record Modified Successfully...!")
                mydb.close() 
        except Exception as ex:
            print("Oops!Something Went Wrong!",ex)
    
    elif choice == 6:
        try:
            mydb = m.connect(host = "localhost",user = "root",password = "sricheechu_2005",database =db)
            if mydb.is_connected() == True:
                print("Connection Successful")
            else:
                    print("Error Connecting to Mysql Database")
            mycursor = mydb.cursor()
            eno = int(input("Enter the Employee Number whose Pay Slip you want to retrieve:"))
            query = "SELECT * FROM PAY WHERE EMPNO="+str(eno)
            mycursor.execute(query)
            now = datetime.now()
            print("\n\n\n\t\t\t\tSALARY SLIP")
            print("Current Date and Time:",end = " ")
            print(now.strftime("%Y-%m-%d %H:%M:%S"))
            print(tabulate(mycursor,headers = ["EMPNO","NAME","JOB","BASIC SALARY","DA","HRA","GROSS","TAX","NET"]))
            mydb.close()
        except Exception as ex:
            print("Oops!Something Went Wrong!",ex)
    
    elif choice == 7:
        os.system('cls')
        try:
            mydb = m.connect(host = "localhost",user = "root",password = "sricheechu_2005",database =db)
            if mydb.is_connected() == True:
                print("Connection Successful")
            else:
                print("Error Connecting to Mysql Database")
            mycursor = mydb.cursor()
            eno = input("Enter Employee Number to Delete:")
            query = 'DELETE FROM PAY WHERE EMPNO='+eno
            mycursor.execute(query)
            mydb.commit()
            c = mycursor.rowcount
            if c>0:
                print("Deletion Successful")
            else:
                print("Employee Number",eno,"is Not Found..!")
            mydb.close()
        except Exception as ex:
            print("Oops!Something Went Wrong!",ex)

    elif choice == 8:
        os.system('cls')
        try:
            mydb = m.connect(host = "localhost",user = "root",password = "sricheechu_2005",database =db)
            if mydb.is_connected() == True:
                print("Connection Successful")
            else:
                print("Error Connecting to Mysql Database")
            mycursor = mydb.cursor()
            mycursor.execute("USE PAYROLL")
            print("Enter Employee Details")
            empno = input("Enter Employee No:")
            query = "SELECT * FROM PAY WHERE EMPNO="+empno
            mycursor.execute(query)
            myrecord = mycursor.fetchone()
            monthlyquery = "SELECT * FROM MONTHLYPAYROLL WHERE EMPNO="+empno+" AND MONTH = "+str(datetime.now().month)+" AND YEAR = "+str(datetime.now().year)
            mycursor.execute(monthlyquery)
            monthlyrecord = mycursor.fetchone()
            c = mycursor.rowcount
            if c <= 0:
                gross = (myrecord[3]/30)+(myrecord[4]/30)+(myrecord[5]/30)
                unpaidlv = int(input("Enter the number of Unpaid Leave:"))
                deductamt = (gross/30)*unpaidlv
                net = (gross-(myrecord[7]/30)-deductamt)
                query = "INSERT INTO MONTHLYPAYROLL VALUES("+empno+",'"+str(datetime.now().month)+"','"+str(datetime.now().year)+"',"+str(myrecord[3]/30)+","+str(myrecord[4]/30)+","+str(myrecord[5]/30)+","+str(gross)+","+str(deductamt)+","+str(myrecord[7]/30)+","+str(net)+")"
                mycursor.execute(query)
                mydb.commit()
            mydb.close()
            print("Records are Inserted Successfully..!")
        except Exception as ex: 
                print("Oops!Something Went Wrong!",ex)

    elif choice == 9:
        os.system('cls')
        try:
            mydb = m.connect(host = "localhost",user = "root",password = "sricheechu_2005",database =db)
            if mydb.is_connected() == True:
                print("Connection Successful")
            else:
                    print("Error Connecting to Mysql Database")
            mycursor = mydb.cursor()
            eno = input("Enter the Employee Number to Display Payroll:")
            payquery = "SELECT * FROM PAY WHERE EMPNO="+eno
            mycursor.execute(payquery)
            payrecord = mycursor.fetchone()
            query = "SELECT * FROM MONTHLYPAYROLL WHERE EMPNO="+eno
            mycursor.execute(query)
            myrecord = mycursor.fetchone()
            c = mycursor.rowcount
            if c == -1:
                print("Employee Number"+ eno +"does not exist.!!")
            else:
                pdf = FPDF()
                pdf.add_page()
                pdf.set_font("Arial", size = 15)
                pdf.cell(200,10, txt = "Salary Slip for "+str(datetime.now().month)+"/"+str(datetime.now().year),ln = 1, align = 'C')
                pdf.ln()
                pdf.ln()
                pdf.ln()
                pdf.cell(200,10,txt = "Employee NO   : "+ str(payrecord[0]),ln = 5, align = 'L')
                pdf.cell(200,10,txt = "Employee Name : "+ payrecord[1],ln = 6, align = 'L')
                pdf.cell(200,10,txt = "Employee JOB  : "+ payrecord[2],ln = 7, align = 'L')
                pdf.ln()
                pdf.ln()
                pdf.ln()
                pdf.cell(200,10,txt = "---------------------------------------------------------------",ln = 11,align = 'L')
                pdf.cell(200,10,txt = "Basic Salary  : "+ str(myrecord[3]),ln = 12, align = 'L')
                pdf.cell(200,10,txt = "DA            : "+ str(myrecord[4]),ln = 13, align = 'L')
                pdf.cell(200,10,txt = "HRA           : "+ str(myrecord[5]),ln = 14, align = 'L')
                pdf.cell(200,10,txt = "Gross Salary  : "+ str(myrecord[6]),ln = 15, align = 'L')
                pdf.cell(200,10,txt = "Unpaid Leave  : "+ str(myrecord[7]),ln = 16, align = 'L')
                pdf.cell(200,10,txt = "Tax           : "+ str(myrecord[8]),ln = 17, align = 'L')
                pdf.cell(200,10,txt = "---------------------------------------------------------------",ln = 18,align = 'L')
                pdf.cell(200,10,txt = "Net Salary    : "+ str(myrecord[9]),ln = 19, align = 'L')
                pdf.cell(200,10,txt = "---------------------------------------------------------------",ln = 20,align = 'L')
                pdf.output("D:\\"+eno+"-"+str(datetime.now().month)+"-"+str(datetime.now().year)+".pdf")
                os.startfile("D:\\"+eno+"-"+str(datetime.now().month)+"-"+str(datetime.now().year)+".pdf")
                mydb.close() 
        except Exception as ex:
            print("Oops!Something Went Wrong!",ex)
    elif choice == 10:
        os.system('cls')
        try:
            mydb = m.connect(host = "localhost",user = "root",password = "sricheechu_2005",database =db)
            if mydb.is_connected() == True:
                print("Connection Successful")
            else:
                    print("Error Connecting to Mysql Database")
            mycursor = mydb.cursor()
            payquery = "SELECT * FROM PAY;"
            mycursor.execute(payquery)
            payrecord = mycursor.fetchall()
            for record in payrecord:
                mycursor = mydb.cursor()
                query = "SELECT * FROM MONTHLYPAYROLL WHERE EMPNO="+str(record[0])
                mycursor.execute(query)
                myrecord = mycursor.fetchone()
                c = mycursor.rowcount
                if c <= 0:
                    print("Employee Number"+str(record[0])+"does not exist.!!")
                else:
                    pdf = FPDF()
                    pdf.add_page()
                    pdf.set_font("Arial", size = 15)
                    pdf.cell(200,10, txt = "Salary Slip for "+str(datetime.now().month)+"/"+str(datetime.now().year),ln = 1, align = 'C')
                    pdf.ln()
                    pdf.ln()
                    pdf.ln()
                    pdf.cell(200,10,txt = "Employee NO   : "+ str(record[0]),ln = 5, align = 'L')
                    pdf.cell(200,10,txt = "Employee Name : "+ record[1],ln = 6, align = 'L')
                    pdf.cell(200,10,txt = "Employee JOB  : "+ record[2],ln = 7, align = 'L')
                    pdf.ln()
                    pdf.ln()
                    pdf.ln()
                    pdf.cell(200,10,txt = "---------------------------------------------------------------",ln = 11,align = 'L')
                    pdf.cell(200,10,txt = "Basic Salary  : "+ str(myrecord[3]),ln = 12, align = 'L')
                    pdf.cell(200,10,txt = "DA            : "+ str(myrecord[4]),ln = 13, align = 'L')
                    pdf.cell(200,10,txt = "HRA           : "+ str(myrecord[5]),ln = 14, align = 'L')
                    pdf.cell(200,10,txt = "Gross Salary  : "+ str(myrecord[6]),ln = 15, align = 'L')
                    pdf.cell(200,10,txt = "Unpaid Leave  : "+ str(myrecord[7]),ln = 16, align = 'L')
                    pdf.cell(200,10,txt = "Tax           : "+ str(myrecord[8]),ln = 17, align = 'L')
                    pdf.cell(200,10,txt = "---------------------------------------------------------------",ln = 18,align = 'L')
                    pdf.cell(200,10,txt = "Net Salary    : "+ str(myrecord[9]),ln = 19, align = 'L')
                    pdf.cell(200,10,txt = "---------------------------------------------------------------",ln = 20,align = 'L')
                    pdf.output("D:\\"+str(record[0])+"-"+str(datetime.now().month)+"-"+str(datetime.now().year)+".pdf")
                    os.startfile("D:\\"+str(record[0])+"-"+str(datetime.now().month)+"-"+str(datetime.now().year)+".pdf")
            mydb.close() 
        except Exception as ex:
                print("Oops!Something Went Wrong!",ex)

    elif choice == 11:
        os.system('cls')
        print("Please Enter a Valid Choice")
    else:
        os.system('cls')
        break