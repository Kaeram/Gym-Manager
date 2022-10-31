from functions import *
import tabulate as tb


while authenticate() is True:
    print("*"*10,"Fitness Centre Management System","*"*10)
    print("Welcome User, Enter appropriate choice")
    print("1.Main")
    print("2.Admin tools")
    print ("Type 'Quit' or 'Exit' to exit")
    ch=str(input("Enter your choice: "))
    if ch=='1': #Main
        print ('*'*5,'Gym Management System','*'*5)
        print ('Hello User, Select a command')
        print ("M1. Add Customer")
        print ("M2. Delete Customer")
        print ("M3. Show all packages")
        print ("M4. Show all customers")
        print ("M5. Find customer by name")
        print ("Type 'Quit' or 'Exit' to exit")
        ch=str(input("Enter your choice:"))
        
        if ch=='M1'or ch=="m1":
            insert_into_table_Meminfo()
    
        elif ch=="cleanslate":
            cleanslate()

        elif ch=='quit' or 'Quit' or 'exit' or 'Exit':
            print("Developed by Kaushike Ramanathan, Amrit Nigam and Shourya Hedaoo as Investigatory Project")
            break   
    elif ch=='2': #Admin tools
        
            print("Type 'concheck' to check connection")
            print("Type 'cleanslate' to clear database")
            print("1.Add Employee")
            ch=str(input("Enter choice:  "))
            if ch=='concheck':
                concheck()
            elif ch=='cleanslate':  
                cleanslate()
            elif ch=='1':
                insert_into_emp()    

            break
    elif ch=="3":
        delete_MemInfo_entry() 

    elif ch=='quit' or 'Quit' or 'exit' or 'Exit':
        print("Developed by Kaushike Ramanathan, Amrit Nigam and Shourya Hedaoo as Investigatory Project")
















    break


