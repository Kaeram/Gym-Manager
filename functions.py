import mysql.connector as sql
import tabulate as tb




#Connection
con=sql.connect(host='localhost',user='root',password='root')
def concheck():
    if con.is_connected():
        print('Connection Successful')
    else:
        print("Connection Failed")
cu=con.cursor() #Creating Cursor


#Functions

def authenticate():
        UserID=input("Enter User_ID: ")
        
        
        if UserID=="Kaushike.R" or UserID=="Amrit.N" or UserID=="Shourya.H" or UserID=="admin":
            return(True)
            
        else:
            print("Access Denied")

def create_table_Meminfo():
    '''Function to create table in MySQL to store Member information'''
    try:    
        query='''
        Create table if not exists Mem_Info
        (
            Mem_ID int primary key,
            Mem_Name varchar(30),
            age int,
            Phone_No char(10),
            DOJ date
            )
            '''
        cu.execute(query)
    except Exception as e:
        print("Error:",e)    


def emp_table():
    '''function to create table in MySQL to store trainer/employee details'''
    try:
        query='''
        Create table if not exits emp_table
        (
            emp_id int,
            emp_name varchar(30),
            gender char(1),
            DOB date,
            designation varchar(30),
            mob_no char(10)
            address varchar(100)
            )
            '''
    except Exception as e:
        print("Error:",e)


def package_data():

    '''Function to create table in MySQL to store package info'''
  
    query1='''
        create table if not exists package
        (
            P_ID int primary key,
            P_name varchar(30),
            Trainer_Availability char(1),
            Price_per_month int
        )
             '''
    cu.execute(query1)  
        
    query2='''insert into package values(1,'Beginner','Y',1000)'''
    query3='''insert into package values(2,'Amatuer','Y',1500)'''
    query4='''insert into package values(3,'Experienced','N',3000)'''
    cu.execute(query2)
    cu.execute(query3)
    cu.execute(query4)

def insert_into_table_Meminfo():
    '''Function to insert data into Meminfo'''
    try:
        Mem_ID=input("Enter Membership ID:  ")
        Mem_Name=input("Enter Member Name:  ")
        Phone_No=int(input("Enter Phone number:  "))
        DOJ=input("Enter date of joining (YY-MM-DD):  ")
        Gender=input("Gender (M/F/O):  ")
        Weight=int(input("Enter weight: "))
        Address=input("Enter residential address: ")
        query='''insert into Mem_Info(Mem_ID,Mem_Name,Phone_No,DOJ)Values(%s,%s,%s,%s)'''
        val=(Mem_ID,Mem_Name,Phone_No,DOJ)
        cu.execute(query,val)
        con.commit()
        print("Data Entered Successfully")
    except sql.Error as er:
        print('Error:',er)   

def delete_MemInfo_entry():
    '''Function to delete an entry in Mem_Info table'''
    try:
        del_ID=input("Insert Mem_ID to delete:  ")
        query='''delete from Mem_Info where Mem_ID=del_ID'''  
        cu.execute(query)
        con.commit()
        print("Deleted Successfully")
    except sql.Error as er:
        print('Error:',er)

def cleanslate():
    '''for testing purposes'''
    query=('''drop table mem_info''')
    cu.execute(query)
    print('database cleared')

def insert_into_emp():
    '''Function to insert data into employee table'''
    try:
        emp_id=input("Enter Employee ID:  ")
        emp_name=input("Enter Employee Name:  ")
        sex=input("(M/F/O):")
        dob=input("Enter date of birth (yy-mm-dd):  ")
        desig=input("Enter designation:  ")
        mob_no=input("Enter phone number:  ")
        address=input("Enter Residential address:")
        query='''
        insert into emp_table(emp_id,emp_name,gender,DOB,designation,mob_no,address)
        values(%s,%s,%s,%s,%s,%s,%s)
        val=(emp_id,emp_name,sex,dob,desig,mob_no,address)'''
        print('data entered successfully!')
    except Exception as e:
        print('Error:',e)

def display_package():
    query="select * from package"
    cu.execute(query)
    print(tb.tabulate(cu,headers=['ID','Name','Trainer Availability','Price_per_month'],tablefmt='psql'))

def display_allmem():
    cu.execute("select * from mem_info")
    print(tb.tabulate(cu,headers=['ID','Name','Age','Mobile_no','DOJ'],tablefmt='psql'))
    result=cu.fetchall()
    for i in result:
             print(i)

def display_allemp():
    cu.execute("select * from emp_tablex`")
    print(tb.tabulate(cu,headers=['ID','Name','gender','DOB','designation','Mobile_no','address'],tablefmt='psql'))
    result=cu.fetchall()
    for i in result:
             print(i)