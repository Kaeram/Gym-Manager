#MODULES
import mysql.connector as sql
import tkinter as ui


#Connection
con=sql.connect(host='localhost',user='root',password='root',database='Gym')
if con.is_connected():
    print('Connection Successful')
else:
    print("Connection Failed")
cu=con.cursor() #Creating Cursor

#FUNCTIONS
def create_table_Meminfo():
    '''Function to create table in MySQL to store Member information'''
    try:    
        query='''Create table if not exists Mem_Info(Mem_ID int primary key,Mem_Name varchar(30),Phone_No varchar(11),DOJ date)'''
        cu.execute(query)
    except Exception as e:
        print(e)    
create_table_Meminfo()

def insert_into_table_Meminfo():
    '''Function to insert data into Meminfo'''
    try:
        Mem_ID=input("Enter Membership ID:  ")
        Mem_Name=input("Enter Member Name:  ")
        Phone_No=int(input("Enter Phone number:  "))
        DOJ=input("Enter date of joining:  ")
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

       

#def update_MemInfo():
  #  '''Funtion to update member info in Mem_Info'''
 #   try:
   #     ID=int(input("Enter ID of the Member to be updated;  "))
    #    query='''update table'''        






#MAIN
while True:
    print ('*'*5,'Gym Management System','*'*5)
    print ('Hello User, Select a command')
    print ("1. Add Customer")
    print ("2. Delete Customer")
    print ("3. Show all packages")
    print ("4. Show all customers")
    print ("5. Find customer by name")
    print ("6. ")
    print ("7. ")
    print ("8. ")
    print ("9.Lucky Draw")
    print ("Type 'Quit' or 'Exit' to exit")
    ch=str(input("Enter your choice:"))
    if ch=='1':
        insert_into_table_Meminfo()
    elif ch=='2':
        delete_MemInfo_entry()
    elif ch=='quit' or 'Quit' or 'exit' or 'Exit':
        print("Developed by Kaushike Ramanathan, Amrit Nigam and Shourya Hedaoo as Investigatory Project")
        break   





