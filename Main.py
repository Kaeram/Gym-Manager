from functions import *
import tabulate as tb





def menu():
    print("*"*10,"Fitness Centre Management System","*"*10)
    print("Welcome User, Enter appropriate choice")
    print("1.Main")
    print("2.Admin tools")
    print ("Type 'Quit' or 'Exit' to exit")
    ch=str(input("Enter your choice: "))
    if ch=='1': #Main
        main()
    elif ch=='2': #Admin tools
        admin()
    
    elif ch=='quit' or 'Quit' or 'exit' or 'Exit':
            print("Developed by Kaushike Ramanathan, Amrit Nigam and Shourya Hedaoo as Investigatory Project")
            quit()
                 
def main():
    print ('*'*15,'Gym Management System','*'*15)
    print ('Hello User, Select a command')
    print ("M1. Add Customer")
    print ("M2. Show all packages")
    print ("M3. Show all customers")
    print ("M4. Delete Member Record")
    print ("Type 'Quit' or 'Exit' to exit")
    ch=str(input("Enter your choice:"))
    if ch=='M1'or ch=="m1":
        insert_into_table_Meminfo()
        menu()
 

    elif ch=='M2'or ch=='m2':
        display_package()
        menu()  

    elif ch=='M3' or ch=='m3':
        display_allmem()
        menu() 

    elif ch=='M4' or ch=='m4':
        del_mem_rec()     
    
    
    elif ch=="cleanslate":
         cleanslate()
         menu()
         
    elif ch=='quit' or 'Quit' or 'exit' or 'Exit':
            print("Developed by Kaushike Ramanathan, Amrit Nigam and Shourya Hedaoo as Investigatory Project")
            quit()
                  

def admin():
            print("*"*45)
            print ('Hello User, Select a command')
            print("Type 'concheck' to check connection")
            print("Type 'cleanslate' to clear database")
            print("A1.Add Employee")
            print("A2.Show All Employees")
            print("A3.Delete Employee Record")
            ch=str(input("Enter choice:  "))
            if ch=='concheck':
                concheck()
                menu()
            elif ch=='cleanslate':  
                cleanslate()
                menu()
            
            elif ch=='A1' or ch=='a1' :
                insert_into_emp()
                menu()

            elif ch=="A2" or ch=="a2":
                display_allemp()
                main() 

            elif ch=='A3' or ch=='a3':
                del_emp_rec()

            elif ch=='quit' or 'Quit' or 'exit' or 'Exit':
                print("Developed by Kaushike Ramanathan, Amrit Nigam and Shourya Hedaoo as Investigatory Project")
                quit()

            
           



        
#main
while authenticate() is True:
    menu()
 

