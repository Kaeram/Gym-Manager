import mysql.connector as sql
from functions import *

con=sql.connect(host='localhost',user='root',password='root',database='Gym')

if con.is_connected():
    print("sucessfully connected")
cu=con.cursor()

print("Creating prerequisites...")
print("Creating Tables...")
print("Hacking NASA... ;)")
create_table_Meminfo()
emp_table()
package_data()
query2='''insert into package values(1,'Beginner','Y',1000)'''
query3='''insert into package values(2,'Amatuer','Y',1500)'''
query4='''insert into package values(3,'Experienced','N',3000)'''
cu.execute(query2)
cu.execute(query3)
cu.execute(query4)
con.commit()
print("DONE...Safe to exit")