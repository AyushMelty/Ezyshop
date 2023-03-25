import mysql.connector as db
from functions import create_db_connection,exe_query,read_query
from mysql.connector import Error

def check(uname):
    q1=f"select Username from login where Username='{uname}'"
    connection=create_db_connection("localhost","root",pw,dbname)
    results=read_query(connection,q1)
    if uname==results[0][0]:
        return True
    else:
        return False
    
def menu1():
    print("WELCOME TO EZYSHOP\n1.)Admin\n2.)Vendor\n3.)Customer\n4.)Exit\nEnter as?")
def menu2():
    print("WELCOME TO EZYSHOP\n1.)Login\n2.)SignUp\n3.)Exit") 
def login(cat,username,password):
    flag=0
    if cat==1:
        q1=f"select Password from admin where admin_username='{username}';"
        connection=create_db_connection("localhost","root",pw,dbname)
        results=read_query(connection,q1)
        if results[0][0]==password:
            return True
    if cat==2:
        q1=f"select Password from vendor where ref_username='{username}';"
        connection=create_db_connection("localhost","root",pw,dbname)
        results=read_query(connection,q1)
        if results[0][0]==password:
            return True
    if cat==3:
        q1=f"select Password from customer where ref_name='{username}';"
        connection=create_db_connection("localhost","root",pw,dbname)
        results=read_query(connection,q1)
        if results[0][0]==password:
            return True
    return False
def signup_admin():
    q1="select max(idAdmin) from admin"
    connection=create_db_connection("localhost","root",pw,dbname)
    results=read_query(connection,q1)
    # print(type(results))
    num=int(results[0][0])
    num+=1
    print("Enter you name:")
    name=input()
    print("Enter you username:")
    uname=input()
    print("Enter password:")
    p=input()
    if check(uname)==True:
        return
    q1=f"insert into login values(1,'{uname}','{p}');"
    connection=create_db_connection("localhost","root",pw,dbname)
    exe_query(connection,q1)
    q1=f"insert into admin values({num},'{name}','{p}','{uname}');"
    connection=create_db_connection("localhost","root",pw,dbname)
    exe_query(connection,q1)
def signup_vendor():
    q1="select max(idvendor) from vendor"
    connection=create_db_connection("localhost","root",pw,dbname)
    results=read_query(connection,q1)
    # print(type(results))
    num=int(results[0][0])
    num+=1
    print("Enter your name:")
    name=input()
    print("Enter your phone no. :")
    phno=input()
    print("Enter your address:")
    addr=input()
    print("Enter your username:")
    uname=input()
    print("Enter your password:")
    p=input()
    q1=f"insert into login values(2,'{uname}',{p})"
    # connection=create_db_connection("localhost","root",pw,dbname)
    if check(uname)==True:
        return
    exe_query(connection,q1)
    q1=f"insert into vendor values({num},'{name}','{phno}','{addr}','{uname}',,'{p}')"
    # connection=create_db_connection("localhost","root",pw,dbname)
    exe_query(connection,q1)
def signup_customer():
    q1="select max(idcustomer) from customer"
    connection=create_db_connection("localhost","root",pw,dbname)
    results=read_query(connection,q1)
    num=int(results[0][0])
    num+=1
    print("Enter your fname:")
    fname=input()
    print("Enter your lname:")
    lname=input()
    print("Enter your street no. :")
    sno=input()
    print("Enter your city:")
    city=input()
    print("Enter your state:")
    state=input()
    print("Enter your pincode:")
    pincode=input()
    print("Enter your date of birth(dd/mm/yyyy):")
    dob=input()
    print("Enter your your username:")
    uname=input()
    print("Enter your password")
    p=input()
    if check(uname)==True:
        return
    q1=f"insert into login values(3,'{uname}','{p}')"
    connection=create_db_connection("localhost","root",pw,dbname)
    exe_query(connection,q1)
    q1=f"insert into customer values({num},'{fname}','{lname}','{sno}','{city}','{state}','{pincode}','{dob}','{p}','{uname}',0)"
    connection=create_db_connection("localhost","root",pw,dbname)
    exe_query(connection,q1)











pw="googlemelty@2003"
dbname="ezyshop"
# q1="""
# select * from cartwithproducts;
# """
# connection=create_db_connection("localhost","root",pw,dbname)
# results=read_query(connection,q1)
# for result in results:
#     print(result)
# q1="""
# update products set Discount=Discount+10 where Stock>500 and Discount<40;"""
# connection=create_db_connection("localhost","root",pw,dbname)
# exe_query(connection,q1)
menu2()
n=int(input())
while n!=3:
    if n==1:
        print("Enter category\n1 for Admin\n2 for Vendor\n3 for Customer")
        cat=int(input())
        print("Enter Username:")
        name=input()
        print("Enter Password:")
        password=input()
        if login(cat,name,password)==False:
            print("Wrong username/password")
        else:
            if cat==1:
                pass
            if cat==2:
                pass
            if cat==3:
                pass


    if n==2:
        print("Enter category\n1 for Admin\n2 for Vendor\n3 for Customer")
        cat=int(input())
        if cat==1:
            signup_admin()
        if cat==2:
            signup_vendor()
        if cat==3:
            signup_customer()
    menu2()
    n=int(input())   






   

   

