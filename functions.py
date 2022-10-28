import mysql.connector as sql
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
        DOJ=input("Enter date of joining (YY-MM-DD):  ")
        Gender=input("M/F? ")
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

        

       

#def update_MemInfo():
  #  '''Funtion to update member info in Mem_Info'''
 #   try:
   #     ID=int(input("Enter ID of the Member to be updated;  "))
    #    query='''update table'''        
