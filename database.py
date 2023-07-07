import mysql.connector as db
from functions import create_db_connection,exe_query,read_query
from mysql.connector import Error


def customer_menu(name):
    print(f"Hello {name}\nChoose from following:\n1.)Show products\n2.)Add to cart\n3.)Show cart details\n4.)Edit Cart\n5.)Checkout\n6.)My orders\n7.)Exit")
def showstat():
    print("Choose from following:\n1.)data of product's name and category with total stock\n2.)data of product's name and category with stock in cube\n3.)data of different billing types with address\n4.)data of different billing types with address in cube\n5.)Return")
    ch=int(input())
    if ch==1:
        q="select Category,ProductName,sum(Stock) from products group by Category,ProductName with rollup"
        connection=create_db_connection("localhost","root",pw,dbname)
        results=read_query(connection,q)
        for result in results:
            print(result)
        connection.close()
    if ch==2:
        q="select Category,ProductName,sum(Stock) from products group by Category,ProductName with rollup union select Category,ProductName,sum(Stock) from products group by ProductName,Category with rollup"
        connection=create_db_connection("localhost","root",pw,dbname)
        results=read_query(connection,q)
        for result in results:
            print(result)
        connection.close()
        
    if ch==3:
        q="select b.payment,c.address,avg(c.amount) from billing as b inner JOIN cart as c on b.refcartid=c.idcart group by b.payment,c.address with rollup"
        connection=create_db_connection("localhost","root",pw,dbname)
        results=read_query(connection,q)
        for result in results:
            print(result)
        connection.close()
    if ch==4:
        q="select b.payment,c.address,avg(c.amount) from billing as b inner JOIN cart as c on b.refcartid=c.idcart group by b.payment,c.address with rollup union select b.payment,c.address,avg(c.amount) from billing as b inner join cart as c on b.refcartid=c.idcart group by c.address,b.payment with rollup"
        connection=create_db_connection("localhost","root",pw,dbname)
        results=read_query(connection,q)
        for result in results:
            print(result)
        connection.close()
    if ch==5:
        return
def showproducts():
    q="select idProducts,ProductName,Stock,Price,Discount from products"
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
    updatecartamt(cartid)
    q=f"Select distinct(p.ProductName),cwp.quantity,p.idProducts from cartwithproducts as cwp inner join products as p on cwp.prodref_id=p.idProducts where cwp.cartref_id={cartid} and cwp.quantity>0"
    # print("(Product Name,Amount)")
    results=read_query(connection,q)
    if(results is None):
        return
    for result in results:
        print(result[0]," ",result[1]," ",result[2])
        print()
    q=f"select amount from cart where idcart={cartid}"
    connection=create_db_connection("localhost","root",pw,dbname)
    results=read_query(connection,q)
    amount=int(results[0][0])
    print(f"Amount is : {amount}")
def showvend(id):
    q1=f"select idvendor,vendorname,venphno,Address from vendor where ref_adminid={id}"
    connection=create_db_connection("localhost","root",pw,dbname)
    results=read_query(connection,q1)
    if(results is None):
        return
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
    # print(f"Hello {name}\nChoose from following:\n1.)Show all vendors\n2.)Delete vendors\n3.)Instantaneous analysis of data\n4.)Exit")
    print(f"Hello {name}\nChoose from following:\n1.)Show all vendors under me\n2.)Add new vendor\n3.)Delete vendors\n4.)Instantaneous analysis of data\n5.)Exit")
    
def vendor_menu(name):
    print(f"Hello {name}\nChoose from following:\n1.)Add new product\n2.)Show my products\n3.)Delete product\n4.)Exit")    
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
        if len(results)>0:
            if results[0][0]==password:
                return True
    if cat==2:
        q1=f"select Password from vendor where ref_username='{username}';"
        connection=create_db_connection("localhost","root",pw,dbname)
        results=read_query(connection,q1)
        if len(results)>0:
            if results[0][0]==password:
                return True
    if cat==3:
        q1=f"select Password from customer where ref_name='{username}';"
        connection=create_db_connection("localhost","root",pw,dbname)
        results=read_query(connection,q1)
        if len(results)>0:
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

def addvend(id):
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
        print("Same username exists")
        return
    connection=create_db_connection("localhost","root",pw,dbname)
    exe_query(connection,q1)
    q1=f"insert into vendor values({num},'{name}','{phno}','{addr}','{uname}',{id},'{p}')"
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
def showvendpro(uname):
    q=f"select idvendor from vendor where ref_username='{uname}'"
    connection=create_db_connection("localhost","root",pw,dbname)

    reusult2=read_query(connection,q)
    vendid=int(reusult2[0][0])
    q=f"select idProducts,ProductName,Stock,Price,Discount,Category from products where ref_userid={vendid}"
    connection=create_db_connection("localhost","root",pw,dbname)
    reusult2=read_query(connection,q)
    if(reusult2 is None):
        return
    for result in reusult2:
        print(result[0],result[1],result[2],result[3],result[4],result[5])
def addtocart(uname):
    # connection=create_db_connection("localhost","root",pw,dbname)
    
    pr_id= int(input("Product id you want to add: "))
    quantity=int(input("Enter the quantity: "))
    q1=f"Select idcustomer from customer where ref_name='{uname}'"
    qry=f"Select Stock from products where idProducts={pr_id}"
    connection=create_db_connection("localhost","root",pw,dbname)
    rts=read_query(connection,qry)
    total=int(rts[0][0])

    if quantity>total:
        print("Given quantity is greater than stock!!!")
        return

    reusult2=read_query(connection,q1)
    num2=int(reusult2[0][0])

    q6=f"Select idcart from cart where id={num2}"
    connection=create_db_connection("localhost","root",pw,dbname)
    result4=read_query(connection,q6)
    num3=int(result4[0][0])#cart id
    
    q4=f"Select max(relation_id) from cartwithproducts;"
    connection=create_db_connection("localhost","root",pw,dbname)

    result3=read_query(connection,q4)
    num1=int(result3[0][0])
    num1+=1

    q5=f"Insert into cartwithproducts values({num3},{pr_id},{quantity},{num1})"
    connection=create_db_connection("localhost","root",pw,dbname)

    exe_query(connection,q5)
    # q7=f"select Price from products where idProducts={pr_id}"
    # connection=create_db_connection("localhost","root",pw,dbname)
    # result5=read_query(connection,q7)
    # price=int(result5[0][0])
    # newamount=price*quantity
    # q8=f"update cart set amount=amount+{newamount} where idcart={num3}"
    # connection=create_db_connection("localhost","root",pw,dbname)
    # exe_query(connection,q8)
    # result5=read_query(connection)

def updatecartamt(cartid):
    q=f"Select distinct(p.ProductName),cwp.quantity,p.Price,p.Discount from cartwithproducts as cwp inner join products as p on cwp.prodref_id=p.idProducts where cwp.cartref_id={cartid} and cwp.quantity>0"
    connection=create_db_connection("localhost","root",pw,dbname)
    results=read_query(connection,q)
    ans=0
    q=f"update cart set amount=0 where idcart={cartid}"
    # if(results in None):
    #     return 
    for result in results:
        a=(int(result[1])*int(result[2]))
        b=(a*int(result[3])) /100
        a=a-b
        ans+=a
    q=f"update cart set amount={ans} where idcart={cartid}"
    connection=create_db_connection("localhost","root",pw,dbname)
    exe_query(connection,q)
    return ans


def delvend(id):

    vid=int(input("Enter vendor id you want to delete: "))
    q1=f"select ref_adminid from vendor where idvendor={vid}"
    connection=create_db_connection("localhost","root",pw,dbname)
    results=read_query(connection,q1)
    num=int(results[0][0])
    if num!=id:
        print("Given vendor is not under me!!!")
        return 
    else:
        q2=f"Delete from vendor where idvendor={vid}"
        exe_query(connection,q2)
def editcart(uname):
    pr_id=int(input("Enter the product ID:"))
    quantity=int(input("Enter new quantity:"))
    qry=f"Select Stock from products where idProducts={pr_id}"
    connection=create_db_connection("localhost","root",pw,dbname)
    rts=read_query(connection,qry)
    total=int(rts[0][0])

    if quantity>total:
        print("Given quantity is greater than stock!!!")
        return

    q=f"update cartwithproducts as cwp set cwp.quantity={quantity} where prodref_id={pr_id}"
    # connection=create_db_connection("localhost","root",pw,dbname)
    exe_query(connection,q)
    # updatecartamt(uname)

def delprod():
    a=int(input("Enter product id you want to delete: "))
    connection=create_db_connection("localhost","root",pw,dbname)
    q2=f"Delete from products where idProducts={a}"
    exe_query(connection,q2)

def checkout(uname):
    q1=f"Select idcustomer from customer where ref_name='{uname}';"
    connection=create_db_connection("localhost","root",pw,dbname)
    results=read_query(connection,q1)
    custid=int(results[0][0])
    q6=f"Select idcart from cart where id={custid}"
    results1=read_query(connection,q6)
    cartid=int(results1[0][0])#cart id

    q2="select max(orderid) from orders"
    # connection=create_db_connection("localhost","root",pw,dbname)
    results2=read_query(connection,q2)

    num=int(results2[0][0])
    num+=1
    amount=updatecartamt(cartid)
    print("Choose payment mode\n1.)COD\n2.)UPI\n3.)Debit Card\n4.)Credit Card\n5.)Netbanking")
    payment=input()
    q=f"insert into orders values ({num},'{payment}',{amount},{custid})"
    connection=create_db_connection("localhost","root",pw,dbname)
    exe_query(connection,q)
    q2="select max(deliveryid) from delivery"
    # connection=create_db_connection("localhost","root",pw,dbname)
    results2=read_query(connection,q2)

    prdel=int(results2[0][0])
    prdel+=1
    q=f"insert into delivery values ({prdel},0,{custid})"
    connection=create_db_connection("localhost","root",pw,dbname)
    exe_query(connection,q)
    q=f"delete from cartwithproducts where cartref_id={cartid}"
    exe_query(connection,q)
    updatecartamt(cartid)
    print("Do you want to rate us?: 1)Yes\n2)Later")
    a=int(input())
    if a==1:
        b=int(input("Give a rating between 1 and 5: "))
        q1=f"Insert into feedback values({custid},{b})"
        exe_query(connection,q1)



def myorders(uname):
    q1=f"Select idcustomer from customer where ref_name='{uname}';"
    connection=create_db_connection("localhost","root",pw,dbname)
    results=read_query(connection,q1)
    custid=int(results[0][0])
    q=f"Select orderid,payment,amount from orders where custid={custid}"
    results=read_query(connection,q)

    for result in results:
        print(result[0]," ",result[1]," ",result[2])




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
                connection1=create_db_connection("localhost","root",pw,dbname)
                q1=f"Select idAdmin from admin where admin_username='{uname}';"
                reusult2=read_query(connection1,q1)
                adm_id=int(reusult2[0][0])

                admin_menu(uname)                
                m=int(input())
                while m!=5:
                    if m==1:
                        showvend(adm_id)
                    elif m==2:
                        addvend(adm_id)
                    elif m==3:
                        delvend(adm_id)
                    elif m==4:
                        showstat()
                    admin_menu(uname)
                    m=int(input())

            if cat==2:
                vendor_menu(uname)
                m=int(input())
                while  m!=4:
                    if m==1:
                        addnewprod(uname)
                    if m==2:
                        showvendpro(uname)

                    if m==3:
                        delprod()
                    vendor_menu(uname)
                    m=int(input())

            if cat==3:
                customer_menu(uname)
                m=int(input())
                while m!=7:
                    if m==1:
                        showproducts()
                        # q3="Select * from products;"
                        # connection1=create_db_connection("localhost","root",pw,dbname)
                        # results1=read_query(connection1,q3)
                        # for result in results1:
                        #     print(result)
                           
                        
                       
                    if m==2:
                        addtocart(uname)
                    
                    if m==3:
                        showmycart(uname)
                    if m==4:
                        editcart(uname)
                    if m==5:
                        checkout(uname)
                    if m==6:
                        myorders(uname)

                    customer_menu(uname)
                    m=int(input())
              
                


    if n==2:
        print("Enter category\n1 for Admin\n2 for Vendor\n3 for Customer")
        cat=int(input())
        if cat==1:
            signup_admin()
        if cat==2:
            # signup_vendor()
            print("Only admin can add new vendors!!!!")

        if cat==3:
            signup_customer()
    menu2()
    n=int(input())   





   

   

