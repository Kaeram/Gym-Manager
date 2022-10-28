from functions import *
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





