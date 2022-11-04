import mysql.connector as sql
from functions import *

con = sql.connect(
  host="localhost",
  user="root",
  password="root"
)

if con.is_connected():
    print("sucessfully connected")

con.cursor().execute("CREATE DATABASE fitness")
print("Database Successfully Created")
con.cursor().execute("USE fitness")
con.cursor().execute('create table log_in(cust_name  varchar(65), account_no  int, password int)')
print("Log_in table created")
con.cursor().execute('create table customer_table(f_name varchar(65),price int,wieght int,cust_name varchar(65), phone_no bigint)')
print("Customer table created")
con.commit()

print("Creating prerequisites...")
create_table_Meminfo()
emp_table()
package_data()

print("DONE")