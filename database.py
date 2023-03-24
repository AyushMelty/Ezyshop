import mysql.connector as db
from mysql.connector import Error
# import pandas as pd
def create_db_connection(host_name,user_name,user_password,db_name):
    connection=None
    try:
        connection=db.connect(host=host_name,user=user_name,passwd=user_password,database=db_name)
        print("MySql db connection successfull")
    except Error as err:
        print(f"Error:'{err}'")
    return connection
def exe_query(connection,query):
    cursor=connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("query executed successfully!")
    except Error as err:
        print(f"Error: '{err}'")
def read_query(connection,query):
    cursor=connection.cursor()
    result=None
    try:
        cursor.execute(query)
        result=cursor.fetchall()
        return result
    except Error as err:
        print(f"Error: '{err}'")

pw="googlemelty@2003"
dbname="ezyshop"
q1="""
select * from cartwithproducts;
"""
connection=create_db_connection("localhost","root",pw,dbname)
results=read_query(connection,q1)
for result in results:
    print(result)
# q1="""
# update products set Discount=Discount+10 where Stock>500 and Discount<40;"""
# connection=create_db_connection("localhost","root",pw,dbname)
# exe_query(connection,q1)