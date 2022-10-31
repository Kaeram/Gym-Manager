import mysql.connector as sq
import tabulate as t
def connection():
    try:
      con=sq.connect(host="localhost",user="root",password="1234",database="hospital_management_system")
      if con.is_connected()==True:
          return con
          
      else:
          print("Couldn't connect")
    except Exception as e:
      print(e)

##Doctor Information      
def create_table_doctors():
    try:
        con=connection()
        cur=con.cursor()
        query='''create table if not exists doctors
                (name varchar(20),
                id int,
                age int,
                date_of_birth date,
                mobile_no varchar(20),
                specialization varchar(20),
                fees int,
                years_of_experience int)'''
        cur.execute(query)
    except Exception as e:
        print(e)
    
def insertion():
    try:
        con=connection()#creating connection object
        cur=con.cursor()#Creating cursor object
        create_table_doctors()

        name=input("Enter name of doctors : ")
        id=int(input("Enter id of doctors: "))
        age=int(input("Enter age of doctors:"))
        date_of_birth=input("Enter date of birth of doctors: ")
        mobile_no=input("Enter mobile no of doctors: ")
        specialization=input("Enter specialization of doctors:")
        fees=int(input("Enter fees of doctors: "))
        years_of_experience=int(input("Enter years of experience: "))
        cur.execute("insert into doctors(name,id,age,date_of_birth,mobile_no,specialization,fees,years_of_experience)values('{}',{},{},'{}','{}','{}',{},{})".format(name,id,age,date_of_birth,mobile_no,specialization,fees,years_of_experience))
        print()
        print("Data inserted successfully")
        con.commit()
    except sq.Error as er:
        print(er)
        
def updation():
    try:
        con=connection()
        cur=con.cursor()
        #name=input("Enter name of doctors:")
        Id=int(input("Enter id of doctor whose record is to be modified:"))
        query="select * from doctors where id={}".format(Id)
        cur.execute(query)
        rec=cur.fetchone()
        c=cur.rowcount
        if c==0:
            print("No record exists for doctor with id :",Id)
        else:
            a,b,c,d,e,f,g=rec[0],rec[2],rec[3],rec[4],rec[5],rec[6],rec[7]
            print("Name :",rec[0])
            print("Id : ",rec[1])
            print("Age :",rec[2])
            print("DOB :",rec[3])
            print("Mob.No. :",rec[4])
            print("Specialization :",rec[5])
            print("Fees :",rec[6])
            print("Years of experience :",rec[7])
            print("-"*10)
            print("Type value to modify below or just press Enter for no change")
            x=input("Enter Name:")
            if len(x)>0:
                a=x
            x=input("Enter Age:")
            if len(x)>0:
                b=int(x)
            x=input("Enter DOB:")
            if len(x)>0:
                c=x
            x=input("Enter Mob.No.:")
            if len(x)>0:
                d=x
            x=input("Enter Specialization.:")
            if len(x)>0:
                e=x
            x=input("Enter Fees:")
            if len(x)>0:
                f=int(x)
            x=input("Enter Years of experience:")
            if len(x)>0:
                g=int(x)
            cur.execute("update doctors set name='%s',age=%d, date_of_birth='%s', mobile_no='%s', specialization='%s', fees=%d,years_of_experience=%d where id= %d"%(a,b,c,d,e,f,g,Id))
            con.commit()
            print("Data updated successfully")          
    except sq.Error as er:
        print(er)
        
def deletion():
    try:
        con=connection()
        cur=con.cursor()
        Id=int(input("Enter id of doctors whose record you want to delete :"))
        cur.execute("delete from doctors where id= %d"%(Id))
        con.commit()
        c=cur.rowcount
        if c>0:
            print("Record Deleted successfully ")
        else:
            print("Doctor with id ",Id," not found")
        
    except sq.Error as er:
        print(er)
def delete_all():
    try:
        con=connection()
        cur=con.cursor()
        ch=input("Do you want to delete all the records (y/n) ")
        if ch=='y' or ch=="Y":
            cur.execute("delete from doctors")
            con.commit()
            print("All records deleted ")
            
    except Exception as e:
        print(e)
    
        
def display_idoctor():
    try:
        con=connection()
        cur=con.cursor()
        Id=int(input("Enter id of the doctor whose record is to be displayed:"))
        query="select * from doctors where id={}".format(Id)        
        cur.execute(query)
        rec=cur.fetchone()
        c=cur.rowcount
        if c==0:
            print("Nothing to display")
        else:
            
            for i in rec:
                print(i,end=" | ")
            print()   
    except Exception as e:
        print(e)
        
def display():
    try:
        con=connection()
        cur=con.cursor()
        cur.execute("select * from doctors")
        print(t.tabulate(cur,headers=['Name','Id','Age','Date_of_Birth','Mobile_no','Specialization','Fees','Years_of_experience'],tablefmt='psql'))
        result=cur.fetchall()
        for i in result:
                print(i)
           # print()
    except sq.Error as er:
        print(er)




##Patient Info@@@@@@@@@@
        
def create_table_patients():
    try:
        con=connection()
        cur=con.cursor()
        query='''create table if not exists patients
                (patient_ID int PRIMARY KEY,
                name varchar(20),
                age int,
                gender char(1),
                address varchar(20),
                contact_no varchar(20),
                date_of_birth date,
                consultant_name varchar(20),
                date_of_consultancy date,
                department varchar(20),
                consultancy_fees int
                )'''
        cur.execute(query)
    except Exception as e:
        print(e)       
        
def insertion1():
    try:
        con=connection()
        cur=con.cursor()
        patient_ID=int(input("Enter id of patient:"))
        name=input("Enter name of patient:")
        age=int(input("Enter age of patient:"))
        gender=input("Enter gender of patient (M/F)")
        address=input("Enter address of patient:")
        contact_no=input("Enter contact no of patient:")
        date_of_birth=input("Enter date of birth of patient:")
        consultant_name=input("Enter consultant name of patient: ")
        date_of_consultancy=input("Enter date of consultancy of patient:")
        department=input("Enter department of patient:")
        consultancy_fees=int(input("Enter consultancy fees of patient :"))
        cur.execute("insert into patients( patient_ID,name,age,gender,address,contact_no,date_of_birth,consultant_name,date_of_consultancy,department,consultancy_fees)values(%d,'%s',%d,'%s','%s','%s','%s','%s','%s','%s',%d)"%( patient_ID,name,age,gender,address,contact_no,date_of_birth,consultant_name,date_of_consultancy,department,consultancy_fees))
        print()
        print("Data inserted successfully")
        con.commit()
    except sq.Error as er:
        print(er)
        
       
def updation1():
    try:
        con=connection()
        cur=con.cursor()
        patient_ID=int(input("Enter id of patient whose record is to be modified:"))
        query="select * from patients where patient_ID={}".format(patient_ID)
        cur.execute(query)
        rec=cur.fetchone()
        c=cur.rowcount
        if c==0:
            print("No record exists for patient with id :",patient_ID)
        else:
            a1,a2,a3,a4,a5,a6,a7,a8,a9,a10=rec[1],rec[2],rec[3],rec[4],rec[5],rec[6],rec[7],rec[8],rec[9],rec[10]
            print("Name :",rec[1])
            print("Age :",rec[2])
            print("Gender :",rec[3])
            print("Address :",rec[4])
            print("Contact No. :",rec[5])
            print("Date_of_birth :",rec[6])
            print("Consultant name :",rec[7])
            print("Date_of_consultancy  :",rec[8])
            print("Department :",rec[9])
            print("Consultancy Fees :",rec[10])
            print("-"*10)
            print("Type value to modify below or just press Enter for no change")
            x=input("Enter Name:")
            if len(x)>0:
                a1=x
            x=input("Enter Age:")
            if len(x)>0:
                a2=int(x)
            x=input("Enter Gender:")
            if len(x)>0:
                a3=x
            x=input("Enter Address:")
            if len(x)>0:
                a4=x
            x=input("Enter Contact No.:")
            if len(x)>0:
                a5=x
            x=input("Enter Date_of_birth:")
            if len(x)>0:
                a6=x
            x=input("Enter Consultant name :")
            if len(x)>0:
                a7=x
            x=input("Enter Date_of_consultancy :")
            if len(x)>0:
                a8=x
            x=input("Enter Department :")
            if len(x)>0:
                a9=x
            x=input("Enter Consultancy Fees  :")
            if len(x)>0:
                a10=int(x)
            cur.execute("update patients set name='%s',age=%d ,gender='%s',address='%s',contact_no='%s',date_of_birth='%s',consultant_name='%s',date_of_consultancy='%s',department='%s',consultancy_fees=%d where patient_ID= %d"%(a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,patient_ID))
            print()
            con.commit()
            print("Data updated successfully")
    except sq.Error as er:
        print(er)

def deletion1():
    try:
        con=connection()
        cur=con.cursor()
        patient_ID=int(input("Enter id of patients whose record you want to delete: "))
        cur.execute("delete from patients where patient_ID= %d"%(patient_ID))
        con.commit()
        c=cur.rowcount
        if c>0:
            print("Record Deleted successfully ")
        else:
            print("Patient with id ",patient_ID," not found")
        
    except sq.Error as er:
        print(er)
        
def delete_all1():
    try:
        con=connection()
        cur=con.cursor()
        ch=input("Do you want to delete all the records (y/n) ")
        if ch=='y' or ch=="Y":
            cur.execute("delete from patients")
            con.commit()
            print("All records deleted ")
            
    except Exception as e:
        print(e)
    
def display1():
    try:
        con=connection()
        cur=con.cursor()
        cur.execute("select * from patients")
        print(t.tabulate(cur,headers=['Patient_Id','Name','Age','Gender','Address','Contact_no','Date_of_Birth','consultant_name','date_of_consultancy','Department','consultancy_fees '],tablefmt='psql'))
        rec=cur.fetchall()
        for i in rec:
            print(i)
    except sq.Error as er:
        print(er)
def display_ipatient():
    try:
        
        con=connection()
        cur=con.cursor()
        Id=int(input("Enter id of the Patient whose record is to be displayed:"))
        query="select * from patients where patient_ID ={}".format(Id)        
        cur.execute(query)
        rec=cur.fetchone()
        c=cur.rowcount
        if c==0:
            print("Nothing to display")
        else:
            
            for i in rec:
                print(i,end=" | ")
            print() 
    except Exception as e:
        print(e)



##Room INFO  %%%%%%     
def create_table_room_info():
    try:
        con=connection()
        cur=con.cursor()
        query='''create table if not exists room_info
                (room_no int,
                room_type varchar(20),
                room_charges_per_day  int,
                room_status  varchar(10),
                patient_name varchar(20)
                )'''
        cur.execute(query)
    except Exception as e:
        print(e)        
def insertion2():
    try:
        con=connection()
        cur=con.cursor()
        create_table_room_info()
        room_no=int(input("Enter room no:"))             
        room_type=input("Enter room type :")            
        room_charges_per_day=int(input("Enter room charges per day:")) 
        room_status=input("Enter room status (Booked/Not Booked):")       
        patient_name=input("Enter patient name :")
        cur.execute("insert into room_info(room_no,room_type,room_charges_per_day,room_status,patient_name)values(%d,'%s',%d,'%s','%s')"%(room_no,room_type,room_charges_per_day,room_status,patient_name ))
        print()
        print("Data inserted successfully")
        con.commit()
    except sq.Error as er:
        print(er)
        
def updation2():
    try:
        con=connection()
        cur=con.cursor()
        room_no=int(input("Enter room no. of patient whose record is to be modified:"))
        query="select * from room_info where room_no ={}".format(room_no)
        cur.execute(query)
        rec=cur.fetchone()
        c=cur.rowcount
        if c==0:
            print("No record exists for room no.:",room_no)
        else:
            r1,r2,r3,r4=rec[1],rec[2],rec[3],rec[4]
            #print("Room No :",rec[0])
            print("Room Type :",rec[1])
            print("Room_charges_per_day  :",rec[2])
            print("Room_status  :",rec[3])
            print("Patient_name    :",rec[4])
            
            print("-"*10)
            print("Type value to modify below or just press Enter for no change")
            x=input("Enter Room Type:")
            if len(x)>0:
                r1=x
            x=input("Enter Room_charges_per_day :")
            if len(x)>0:
                r2=int(x)
            x=input("Enter Room_status  :")
            if len(x)>0:
                r3=x
            x=input("Enter Patient_name :")
            if len(x)>0:
                r4=x
            cur.execute("update room_info set room_type='%s',room_charges_per_day=%d,room_status='%s',patient_name='%s'where room_no= %d"%(r1, r2, r3, r4, room_no))
            print()
            con.commit()
            print("Data updated successfully")
    except sq.Error as er:
        print(er)
        
def deletion2():
    try:
        con=connection()
        cur=con.cursor()
        room_no=int(input("Enter room no from Room_Info whose record you want to delete :"))
        cur.execute("delete from room_info where room_no= %d"%(room_no))
        con.commit()
        c=cur.rowcount
        if c>0:
            print("Record Deleted successfully ")
        else:
            print("No record found for Room no: ",room_no)
       
    except sq.Error as er:
        print(er)
def delete_all2():
    try:
        con=connection()
        cur=con.cursor()
        ch=input("Do you want to delete all the records (y/n) ")
        if ch=='y' or ch=="Y":
            cur.execute("delete from room_info")
            con.commit()
            print("All records deleted ")
            
    except Exception as e:
        print(e)
    

def display2():
    try:
        con=connection()
        cur=con.cursor()
        cur.execute("select * from room_info")
        print(t.tabulate(cur,headers=['Room_No','Room_type','Room_charges_per_day ','Room_status ','Patient_name'],tablefmt='psql'))
        rec=cur.fetchall()
        for i in rec:
                print(i)
        
    except sq.Error as er:
        print(er)

def display_iroom():
    try:
        
        con=connection()
        cur=con.cursor()
        rno=int(input("Enter Room no :"))
        query="select * from room_info where room_no ={}".format(rno)        
        cur.execute(query)
        rec=cur.fetchone()
        c=cur.rowcount
        if c==0:
            print("Nothing to display")
        else:
            
            for i in rec:
                print(i,end=" | ")
            print() 
    except Exception as e:
        print(e)
    

#Bill Info        
def create_table_bill_details():
    try:
        con=connection()
        cur=con.cursor()
        query='''create table if not exists bill_details
                (bill_no  int,
                bill_date date,
                name varchar(20),room_type varchar(20),
                room_charges int,
                pathology_fees int,
                doctor_fees int,
                total_amount int)'''
        cur.execute(query)
    except Exception as e:
        print(e)          
def insertion3():
    try:
        con=connection()
        cur=con.cursor()
        create_table_bill_details()
        bill_no=int(input("Enter bill no.: "))            
        bill_date=input("Enter bill date:")      
        name=input("Enter name :")
        room_type=input("Enter room type :")         
        room_charges=int(input("Enter room charges :"))    
        pathology_fees=int(input("Enter pathology fees :")) 
        doctor_fees=int(input("Enter doctor fees :"))    
        total_amount=room_charges+pathology_fees+doctor_fees  
        cur.execute("insert into bill_details( bill_no, bill_date, name ,room_type, room_charges, pathology_fees, doctor_fees, total_amount )values(%d,'%s','%s','%s',%d,%d,%d,%d)"%( bill_no, bill_date, name, room_type, room_charges, pathology_fees, doctor_fees, total_amount ))
        print()
        print("Data inserted successfully")
        con.commit()
    except sq.Error as er:
        print(er)

def display_ibill():
    try:
        
        con=connection()
        cur=con.cursor()
        bno=int(input("Enter Bill no. :"))
        query="select * from bill_details where bill_no  ={}".format(bno)        
        cur.execute(query)
        rec=cur.fetchone()
        c=cur.rowcount
        if c==0:
            print("Nothing to display")
        else:
            
            for i in rec:
                print(i,end=" | ")
            print() 
    except Exception as e:
        print(e)
        
def display3():
    try:
        con=connection()
        cur=con.cursor()
        cur.execute("select * from bill_details")
        print(t.tabulate(cur,headers=['Bill_No','Bill_date  ','Patient_Name ','Room_type ','Room_charges','Pathology_fees ','Doctor_fees','Total_amount' ],tablefmt='psql'))
        rec=cur.fetchall()
        c=cur.rowcount
        if c==0:
            print("No records to display")
        else:
            for i in rec:
                print(i)
    except sq.Error as er:
        print(er)

def updation3():
    try:
        con=connection()
        cur=con.cursor()
        bno=int(input("Enter Bill no. to be modified:"))
        query="select * from bill_details where bill_no={}".format(bno)
        cur.execute(query)
        rec=cur.fetchone()
        c=cur.rowcount
        if c==0:
            print("No record exists  with bill no. :",bno)
        else:
            a1,a2,a3,a4,a5,a6=rec[1],rec[2],rec[3],rec[4],rec[5],rec[6]
            print("Bill_date   :",rec[1])
            print("Name :",rec[2])
            print("Room_type:",rec[3])
            print("Room_charges :",rec[4])
            print("Pathology fees :",rec[5])
            print("Doctor_fees  :",rec[6])
            print("-"*10)
            print("Type value to modify below or just press Enter for no change")
            x=input("Enter Bill_date:")
            if len(x)>0:
                a1=x
            x=input("Enter Name:")
            if len(x)>0:
                a2=int(x)
            x=input("Enter Room type:")
            if len(x)>0:
                a3=x
            x=input("Enter Room_charges:")
            if len(x)>0:
                a4=int(x)
            x=input("Enter Pathology fees.:")
            if len(x)>0:
                a5=int(x)
            x=input("Enter Doctor_fees:")
            if len(x)>0:
                a6=int(x)
            total_amount =a4+a5+a6
            
            cur.execute("update bill_details set bill_date='%s', name='%s', room_type='%s', room_charges=%d, pathology_fees=%d, doctor_fees=%d, total_amount=%d where bill_no= %d"%(a1,a2,a3,a4,a5,a6,total_amount,bno))
            print()
            con.commit()
            print("Data updated successfully")
    except sq.Error as er:
        print(er)
        
def deletion3():
    try:
        con=connection()
        cur=con.cursor()
        bill_no=int(input("Enter bill no from bill_ details whose record you want to delete:"))
        cur.execute("delete from bill_details where bill_no= %d"%(bill_no))
        con.commit()
        c=cur.rowcount
        if c>0:
            print("Record Deleted successfully ")
        else:
            print("Bill with no ",bill_no," not found")
        
    except sq.Error as er:
        print(er)
def deleteall3():
    try:
        con=connection()
        cur=con.cursor()
        ch=input("Do you want to delete all the records (y/n) ")
        if ch=='y' or ch=="Y":
            cur.execute("delete from bill_details")
            con.commit()
            print("All records deleted ")
            
    except Exception as e:
        print(e)

def menu():
    try:
        while True:
            print(95*'*')
            print("WELCOME TO HOSPITAL MANAGEMENT SYSTEM".center(90))
            print(95*'*')
            print()
            print("Select Your Choice From The Given Alternatives")
            print("1.Doctor Information".center(90))
            print("2.Patients Information".center(90))
            print("3.Rooms Information".center(90))
            print("4.Billing Information".center(90))
            print("5.Exit".center(90))
            ch=input("Enter Your Choice: ")
            if ch=="1":
                while True:
                    print('''
                      D1.Add Record Of Doctors
                      D2.Update Record Of Existing Doctors
                      D3.Delete Record Of Particular Doctors
                      D4.Delete Record of All doctors
                      D5.Access record of particular Doctor
                      D6.Access All The Records Of Doctors
                      D7.Exit'''.center(90))
                    a=input("Enter Your Choice: ")
                    if a=="D1":
                        insertion()
                        print()
                        print("Do You Want To Insert More Records?\nType Yes To Insert More Records And No To Stop")
                        a=input("Enter Your Choice: ")
                        if a=='Yes':
                            insertion()
                        else:
                            print("Okay")
                    elif a=="D2":
                        updation()
                        print("Do You Want To Update More Records?\nType Yes To Update More Records And No To Stop")
                        b=input("Enter Your Choice: ")
                        if b=='Yes':
                            updation()
                        else:
                            print("Okay")
                   
                    elif a=="D3":
                        deletion()
                        print("Do You Want To Delete More Records")
                        c=input("Enter Your Choice: ")
                        if c=='Yes':
                            deletion()
                        else:
                            print("okay")
                    elif a=="D4":
                        delete_all()
                    elif a=="D5":
                        display_idoctor()
                    elif a=="D6":
                        display()
                    elif a=="D7":
                        break
                    else:
                        print("Invalid choice:")
                        
                        
            elif ch=="2":
                while True:
                    print('''
                      P1.Add Record Of patients
                      P2.Update Record Of Existing patients
                      P3.Delete Record Of Particular patients
                      P4.Delete Record Of all patients
                      P5.Access the Record Of particular patients
                      P6.Access All The Records Of patients
                      P7.Exit'''.center(90))
                    a=input("Enter Your Choice: ")
                    if a=="P1":
                        insertion1()
                        print("Do You Want To Insert More Records?\nType Yes To Insert More Records And No To Stop")
                        d=input("Enter Your Choice: ")
                        if d=='Yes':
                            insertion1()
                        else:
                            print("Okay")
                    elif a=="P2":
                        updation1()
                        print("Do You Want To Update More Records?\nType Yes To Update More Records And No To Stop")
                        b=input("Enter Your Choice: ")
                        if b=='Yes':
                            updation1()
                        else:
                            print("Okay")
                   
                    elif a=="P3":
                        deletion1()
                        print("Do You Want To Delete More Records")
                        c=input("Enter Your Choice: ")
                        if c=='Yes':
                            deletion1()
                        else:
                            print("okay")
                    elif a=="P4":
                        delete_all1()
                    elif a=="P5":
                        display_ipatient()
                    elif a=="P6":
                        display1()
                    elif a=="P7":
                        break
                    else:
                        print("Invalid choice:")
                    
                
            elif ch=="3":
                while True:
                    print('''
                      R1.Add Record Of Room 
                      R2.Update Record Of Existing room 
                      R3.Delete Record Of Particular room
                      R4.Delete Record Of All rooms 
                      R5.Access All The Records Of room 
                      R6.Access  The Record Of Particular room 
                      R7.Exit'''.center(90))
                    a=input("Enter Your Choice: ")
                    if a=="R1":
                        insertion2()
                        print("Do You Want To Insert More Records?\nType Yes To Insert More Records And No To Stop")
                        d=input("Enter Your Choice: ")
                        if d=='Yes':
                            insertion2()
                        else:
                            print("Okay")
                    elif a=="R2":
                        updation2()
                        print("Do You Want To Update More Records?\nType Yes To Update More Records And No To Stop")
                        b=input("Enter Your Choice: ")
                        if b=='Yes':
                            updation2()
                        else:
                            print("Okay")
                   
                    elif a=="R3":
                        deletion2()
                        print("Do You Want To Delete More Records")
                        c=input("Enter Your Choice: ")
                        if c=='Yes':
                            deletion2()
                        else:
                            print("okay")
                    elif a=="R4":
                        delete_all2()
                    elif a=="R5":
                        display2()
                    elif a=="R6":
                        display_iroom()
                        
                    elif a=="R7":
                        break
                    else:
                        print("Invalid choice:")


                    
            elif ch=="4":
                while True:
                    print('''
                      B1.Add Records Of bill details
                      B2.Update Record Of Existing bill details
                      B3.Delete Record Of Particular bill
                      B4.Delete All Bill Records
                      B5.Access   Particular bill Records
                      B6.Access All bill Records 
                      B7.Exit'''.center(90))
                    a=input("Enter Your Choice: ")
                    if a=="B1":
                        insertion3()
                        print("Do You Want To Insert More Records?\nType Yes To Insert More Records And No To Stop")
                        d=input("Enter Your Choice: ")
                        if d=='Yes':
                            insertion3()
                        else:
                            print("Okay")
                    elif a=="B2":
                        updation3()
                        print("Do You Want To Update More Records?\nType Yes To Update More Records And No To Stop")
                        b=input("Enter Your Choice: ")
                        if b=='Yes':
                            updation3()
                        else:
                            print("Okay")
                   
                    elif a=="B3":
                        deletion3()
                        print("Do You Want To Delete More Records")
                        c=input("Enter Your Choice: ")
                        if c=='Yes':
                            deletion3()
                        else:
                            print("Okay")
                    elif a=="B4":
                        deleteall3()
                    elif a=="B5":
                        display_ibill()
                    elif a=="B6":
                        display3()
                    elif a=="B7":
                        break
                    else:
                        print("Invalid choice:")
            elif ch=="5":
                break
            else:
                print("Invalid choice")
                    
            
    except sq.Error as er:
        print(er)
menu()


