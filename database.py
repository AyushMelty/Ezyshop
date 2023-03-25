import mysql.connector as db
from functions import create_db_connection,exe_query,read_query
from mysql.connector import Error


def customer_menu(name):
    print(f"Hello {name}\nChoose from following:\n1.)Show products\n2.)Add to cart\n3.)Show cart details\n4.)Exit")
def showproducts():
    q="select idProducts,ProductName,Stock,Price from products"
    connection=create_db_connection("localhost","root",pw,dbname)
    results=read_query(connection,q)
    for result in results:
        print(result)
    connection.close()
def showmycart(uname):
    q1=f"Select idcustomer from customer where ref_name='{uname}';"
    connection=create_db_connection("localhost","root",pw,dbname)
    results=read_query(connection,q1)
    custid=int(results[0][0])
    q6=f"Select idcart from cart where id={custid}"
    results_=read_query(connection,q6)
    cartid=int(results_[0][0])#cart id
    q=f"Select distinct(p.ProductName) from cartwithproducts as cwp inner join products as p on cwp.prodref_id=p.idProducts where cwp.cartref_id={cartid}"
    results=read_query(connection,q)
    for result in results:
        print(result[0])
        print()
    q=f"select amount from cart where idcart={cartid}"
    connection=create_db_connection("localhost","root",pw,dbname)
    results=read_query(connection,q)
    amount=int(results[0][0])
    print(amount)
def showvend(uname):
    q1=f"select vendorname,vendorphno,Address from vendor"
    connection=create_db_connection("localhost","root",pw,dbname)
    results=read_query(connection,q1)
    for result in results:
        print(result)

def addnewprod(uname):
    q2=f"select idvendor from vendor where ref_username='{uname}'"
    connection=create_db_connection("localhost","root",pw,dbname)
    results=read_query(connection,q2)
    idd=int(results[0][0])
    q1="select max(idProducts) from products"
    connection=create_db_connection("localhost","root",pw,dbname)
    results=read_query(connection,q1)
    # print(type(results))
    num=int(results[0][0])
    num+=1
    print("Enter the product name:")
    name=input()
    print("Enter stock:")
    stock=int(input())
    print("Enter price:")
    price=int(input())
    print("Enter available discount on product:")
    dis=int(input())
    print("Enter category of product:")
    category=input()
    q1=f"insert into products values({num},'{name}',{stock},{price},{dis},'{category}',{idd})"
    connection=create_db_connection("localhost","root",pw,dbname)
    exe_query(connection,q1)




def check(uname):
    q1=f"select Username from login where Username='{uname}'"
    connection=create_db_connection("localhost","root",pw,dbname)
    results=read_query(connection,q1)
    if len(results)!=0:
        return True
    else:
        return False
def admin_menu(name):
    print(f"Hello {name}\nChoose from following:\n1.)Show all vendors\n2.)Delete vendors\n3.)Exit")
def vendor_menu(name):
    print(f"Hello {name}\nChoose from following:\n1.)Add new product\n2.)Show my products\n3.)Update product\n4.)Delete product\n5.)Exit")    
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
    q1=f"insert into login values(2,'{uname}','{p}')"
    if check(uname)==True:
        print("same username exists")
        return
    connection=create_db_connection("localhost","root",pw,dbname)
    exe_query(connection,q1)
    q1=f"insert into vendor values({num},'{name}','{phno}','{addr}','{uname}',101,'{p}')"
    # q1=f"INSERT INTO `ezyshop`.`vendor` (`idvendor`, `vendorname`, `venphno`, `Address`, `ref_username`, `ref_adminid`, `Password`) VALUES ('{num}', '{name}', '{phno}', '{addr}', '{uname}', '101', '{p}');"
    connection=create_db_connection("localhost","root",pw,dbname)
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
        uname=input()
        print("Enter Password:")
        password=input()
        if login(cat,uname,password)==False:
            print("Wrong username/password")
        else:
            if cat==1:
                admin_menu(uname)
                m=int(input())
                while m!=3:
                    if m==1:
                        showvend(uname)
            if cat==2:
                vendor_menu(uname)
                m=int(input())
                while  m!=5:
                    if m==1:
                        addnewprod(uname)
                    vendor_menu(uname)
                    m=int(input())

            if cat==3:
                customer_menu(uname)
                m=int(input())
                while m!=4:
                    if m==1:
                        showproducts()
                        # q3="Select * from products;"
                        # connection1=create_db_connection("localhost","root",pw,dbname)
                        # results1=read_query(connection1,q3)
                        # for result in results1:
                        #     print(result)
                           
                        
                       
                    if m==2:
                    
                        connection1=create_db_connection("localhost","root",pw,dbname)
                        pr_id= int(input("Product id you want to add: "))
                        quantity=int(input("Enter the quantity: "))
                        q1=f"Select idcustomer from customer where ref_name='{uname}';"
                        reusult2=read_query(connection1,q1)
                        num2=int(reusult2[0][0])

                        q6=f"Select idcart from cart where id={num2}"
                        result4=read_query(connection1,q6)
                        num3=int(result4[0][0])#cart id
                        
                        q4=f"Select max(relation_id) from cartwithproducts;"
                        result3=read_query(connection1,q4)
                        num1=int(result3[0][0])
                        num1+=1

                        q5=f"Insert into cartwithproducts values({num3},{pr_id},{quantity},{num1})"
                        exe_query(connection1,q5)
                        connection1.close()
                    
                    if m==3:
                        showmycart(uname)
                    
                    customer_menu(uname)
                    m=int(input())
              
                


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





   

   

