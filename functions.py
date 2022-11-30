import mysql.connector as sql
import tabulate as tb




#Connection
con=sql.connect(host='localhost',user='root',password='root',database='Gym')
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
            Phone_No char(10),
            DOJ date,
            Gender char(1),
            Weight int,
            Address varchar(150)
            )
            '''
        cu.execute(query)
    except Exception as e:
        print("Error:",e)    


def emp_table():
    '''function to create table in MySQL to store trainer/employee details'''
    query='''
        Create table if not exists emp_table
        (
            emp_id int,
            emp_name varchar(30),
            gender char(1),
            DOB date,
            designation varchar(30),
            mob_no char(10),
            address varchar(100)
            )
            '''
    cu.execute(query)
 
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
        

def insert_into_table_Meminfo():
    '''Function to insert data into Meminfo'''
    try:
        Mem_ID=input("Enter Membership ID:  ")
        Mem_Name=input("Enter Member Name:  ")
        Phone_No=int(input("Enter Phone number:  "))
        #dob=input("Enter date of joining(YY-MM-DD):")
        doj=input("Enter date of joining (YY-MM-DD):  ")
        Gender=input("Gender (M/F/O):  ")
        Weight=int(input("Enter weight: "))
        Address=input("Enter residential address: ")
        query='''insert into Mem_Info(Mem_ID,Mem_Name,Phone_No,DOJ,Gender,Weight,Address)Values(%s,%s,%s,%s,%s,%s,%s)'''
        val=(Mem_ID,Mem_Name,Phone_No,doj,Gender,Weight,Address)
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
        gender=input("(M/F/O):")
        dob=input("Enter date of birth (yy-mm-dd):  ")
        desig=input("Enter designation:  ")
        mob_no=input("Enter phone number:  ")
        address=input("Enter Residential address:")
        query='''
        insert into emp_table(emp_id,emp_name,gender,DOB,designation,mob_no,address)values(%s,%s,%s,%s,%s,%s,%s)
        '''
        
        val=(emp_id,emp_name,gender,dob,desig,mob_no,address)
        cu.execute(query,val)
        con.commit()
        print('data entered successfully!')
    except Exception as e:
        print('Error:',e)

def display_package():
    query="select * from package"
    cu.execute(query)
    print(tb.tabulate(cu,headers=['ID','Name','Trainer Availability','Price_per_month'],tablefmt='psql'))

def display_allmem():
    cu.execute("select * from mem_info")
    print(tb.tabulate(cu,headers=['ID','Name','Mobile_no','DOJ','Gender','Weight','Address'],tablefmt='psql'))
    result=cu.fetchall()
    for i in result:
             print(i)

def display_allemp():
    cu.execute("select * from emp_table")
    print(tb.tabulate(cu,headers=['ID','Name','gender','DOB','designation','Mobile_no','address'],tablefmt='psql'))
    result=cu.fetchall()
    for i in result:
            print(i)

def del_mem_rec():
        Mem_ID=int(input("Enter id of member whose record you want to delete :"))
        cu.execute("delete from mem_info where Mem_ID= %d"%(Mem_ID))
        con.commit()
        c=cu.rowcount
        if c>0:
            print("Record Deleted successfully ")
        else:
            print("Member with id ",Mem_ID," not found")    

def del_emp_rec():
    emp_id=int(input("Enter id of employee whose record you want to delete :"))
    cu.execute("delete from emp_table where emp_id= %d"%(emp_id))
    con.commit()
    c=cu.rowcount
    if c>0:
        print("Record Deleted successfully ")
    else:
       print("Member with id ",emp_id," not found")    
 
