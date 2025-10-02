#
# 24/06/2022 COMPUTER SCIENCE MYSQL-PYTHON CONNECTIVITY CODE
#
def delay(str):
    for i in str:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0)
def _Intro(data):
    if any(data):
        delay('''
╔═══════════════════════════════════════════════════════════════╦═══╗
║ WELCOME TO EBS                                                ║ X ║
╠═══════════════════════════════════════════════════════════════╩═══╣
║                                                                   ║
║ > EASY BILL PAYMENT WITH SIMPLE UNIQUE CODE.                      ║
║ > Enter the VALID details to get payment details.                 ║
║ > THE CUSTOMER CAN MAKE PAYMENTS IN AN EASY WAY!                  ║
║ > JUST FOLLOW THE SIMPLE STEPS BELOW!                             ║
║                                                                   ║
║ -:CREDITS!:-                                                      ║
║ > LOGO-ASCII: https://www.ascii-art-generator.org                 ║
║ > ERROR SUPPORT-WHERE DEVS LEARN, SHARE AND BUILD CAREERS:        ║
║   https://stackoverflow.com/                                      ║
║ > ERROR SUPPORT-GOOGLE:- https://www.google.com/                  ║
║                                                                   ║
╚═══════════════════════════════════════════════════════════════════╝
''')
        delay("""
╔═══════════════════════════════════════════════════════════════╦═══╗
║ SYSTEM MESSAGE                                                ║ X ║
╠═══════════════════════════════════════════════════════════════╩═══╣
║                                                                   ║
║ 1.ACCOUNT SETTINGS                                                ║
║ 2.TRANSACTION                                                     ║
║ 3.VIEW CUSTOMER DETAILS                                           ║
║ 4.GRAPHICAL REPRESENTATION                                        ║
║ 5.EXIT                                                            ║
║                                                                   ║
╚═══════════════════════════════════════════════════════════════════╝
""")
        print()
        choice2=int(input('ENTER YOUR CHOICE: '))
        if choice2==1:
            delay('''
╔═══════════════════════════════════════════════════════════════╦═══╗
║ SYSTEM MESSAGE                                                ║ X ║
╠═══════════════════════════════════════════════════════════════╩═══╣
║                                                                   ║
║ 1.NEW CUSTOMER                                                    ║
║ 2.DELETE EXISTING ACCOUNT                                         ║
║ 3.Go back                                                         ║
║ 4.Exit                                                            ║
║                                                                   ║
╚═══════════════════════════════════════════════════════════════════╝
''')
            choice12=int(input('ENTER YOUR CHOICE: '))
            if choice12==1:
                newcustomer()
                _Intro(data)
            elif choice12==2:
                deletecustomer()
                _Intro(data)
            elif choice12==3:
                _Intro(data)
            elif choice12==4:
                exit()
            else:
                delay("""
╔═══════════════════════════════════════════════════════════════╦═══╗
║ Invalid Input                                                 ║ X ║
╚═══════════════════════════════════════════════════════════════╩═══╝
""")
                _Intro()
        elif choice2==2:
            transaction()
            _Intro(data)
        elif choice2==3:
            viewcustomerdetails()
            _Intro(data)
        elif choice2==4:
            graph()
            _Intro(data)
        elif choice2==5:
            delay("""
╔═══════════════════════════════════════════════════════════════╦═══╗
║ Thank you! Visit Again!                                       ║ X ║
╚═══════════════════════════════════════════════════════════════╩═══╝
""")
            VAR_1=('yes')
            exit()
        else:
            error1()
    else:
        delay("""
╔═══════════════════════════════════════════════════════════════╦═══╗
║ Thank you! Visit Again!                                       ║ X ║
╚═══════════════════════════════════════════════════════════════╩═══╝
""")
        VAR_1='no'
def databasecreation1():
    cursor.execute("create database if not exists EBS;")
    
def tablecreation_newcustomer():
    cursor.execute("""
    create table if not exists newcustomer
    (Accountno int not null primary key,
    Bankname varchar(35),
    Name varchar(35),
    Address varchar(100),
    contact int not null)""")
    
def tablecreation_signup():
    cursor.execute("""
    create table if not exists signup
    (usename varchar(35) primary key,
    _pass varchar(35),
    confirmpass varchar(35))""")
    
def tablecreation_transaction():
    cursor.execute("""
    create table if not exists transaction
    (accountno int,
    unit int,
    todays varchar(25),
    amtwithoutvat int,
    vat float(12,2),
    amtwithvat int,
    PAID varchar(25),
    foreign key(accountno) references newcustomer(accountno));""")
    
def error1():
    delay('''
╔═══════════════════════════════════════════════════════════════╦═══╗
║ EBS Error                                                     ║ X ║
╠═══════════════════════════════════════════════════════════════╩═══╣
║                                                                   ║
║ Oops! Something went wrong!                                       ║                                       
║ Try:                                                              ║                                                              
║ 1. Re-entering the username/password                              ║                         
║ 2. or The account doesnt exist > Try signup again                 ║
║ 3. or Try restarting the program                                  ║
║                                                                   ║
╚═══════════════════════════════════════════════════════════════════╝
''')
    opt=int(input("Enter your Option: "))
    if opt==1:
        VAR_1=input("Do you want to continue?(yes/no): ")
        login()
    elif opt==2:
        delay("""
╔═══════════════════════════════════════════════════════════════╦═══╗
║ Entering signup page! Please wait.....                        ║ X ║
╚═══════════════════════════════════════════════════════════════╩═══╝
""")
        signup()
    elif opt==3:
        delay("Exiting programme! Please wait.....")
        delay("""
╔═══════════════════════════════════════════════════════════════╦═══╗
║ Thank you! Visit Again!                                       ║ X ║
╚═══════════════════════════════════════════════════════════════╩═══╝
""")
        exit()
    else:
        delay("Invalid option! Try again!")
        delay("""
╔═══════════════════════════════════════════════════════════════╦═══╗
║ Entering EBS Registration page! please wait...                ║ X ║
╚═══════════════════════════════════════════════════════════════╩═══╝
""")
        VAR_1="yes"
        
def signup(): #
    delay('''
╔═══════════════════════════════════════════════════════════════╦═══╗
║ EBS SIGN UP PAGE                                              ║ X ║
╚═══════════════════════════════════════════════════════════════╩═══╝
''')
    username=input("Enter Username: ")
    _pass=getpass("Enter Password: ")
    confirmpass=getpass("Confirm Password: ")
    print(" \n")
    if _pass==confirmpass:
        i1="insert into signup values('{}','{}','{}')".format(username,_pass,confirmpass)
        c1.execute(i1)
        VAR_1=input("Do you want to continue?(yes/no): ")
    else:
        delay("""
╔═══════════════════════════════════════════════════════════════╦═══╗
║ your confirm password is incorrect! Try Again!                ║ X ║
╚═══════════════════════════════════════════════════════════════╩═══╝
""")
        VAR_1=input("Do you want to re-enter Username/Password?(yes/no): ")
        if VAR_1=="yes":
            signup()
        else:
            delay("""
╔═══════════════════════════════════════════════════════════════╦═══╗
║ Thank you! Visit Again!                                       ║ X ║
╚═══════════════════════════════════════════════════════════════╩═══╝
""")
            
def login(): #
    delay('''
╔═══════════════════════════════════════════════════════════════╦═══╗
║ EBS LOGIN PAGE                                                ║ X ║
╚═══════════════════════════════════════════════════════════════╩═══╝
''')
    username=input('Enter your username: ')
    _pass=getpass('Enter your password: ')
    info02="select * from signup where username='{}' and _pass='{}'".format(username,_pass)
    c1.execute(info02)
    data=c1.fetchall()
    if len(data)==0:
        delay("""
╔═══════════════════════════════════════════════════════════════╦═══╗
║ Account not found!                                            ║ X ║
╚═══════════════════════════════════════════════════════════════╩═══╝
""")
        VAR_1=input("Do you want to re-enter Username/Password?(yes/no): ")
        if VAR_1=="yes":
            login()
        else:
            print("1.")
            VAR_1=input("Do you want to continue?(yes/no)")
            if VAR_1.lower()=="no":
                quit()
    else:
        print("2.")
        _Intro(data)
    #info02="select * from signup where username='{}' and _pass='{}'".format(username,_pass)
    #c1.execute(info02)
        
def newcustomer():
    delay('''
╔═══════════════════════════════════════════════════════════════╦═══╗
║ EBS ADD NEW CUSTOMER PAGE                                     ║ X ║
╚═══════════════════════════════════════════════════════════════╩═══╝
''')
    accountno=random.randrange(10000,99999,5)
    print("Your account number: ",accountno)
    bankname=input('Enter Bank name: ')
    name=input('Enter your name: ')
    address=input('Enter your address: ')
    phoneno=(input('Enter your Phone number: '))
    print(" \n")
    info2="insert into newcustomer values({},'{}','{}','{}',{})".format(accountno,bankname,name,address,phoneno)
    c1.execute(info2)
    con.commit()
    VAR_2=input("Do you want to continue?(yes/no): ")
    if VAR_2.lower()=='no':
        delay("""
╔═══════════════════════════════════════════════════════════════╦═══╗
║ Thank you! Visit Again!                                       ║ X ║
╚═══════════════════════════════════════════════════════════════╩═══╝
""")
        exit()
    else:
        print()

def deletecustomer():
    delay('''
╔═══════════════════════════════════════════════════════════════╦═══╗
║ EBS DELETE CUSTOMER PAGE                                      ║ X ║
╚═══════════════════════════════════════════════════════════════╩═══╝
''')
    acc=input("Enter your account number: ")
    use=input("Enter your username: ")
    info6=c1.execute("delete from Transaction where accountno='{}'".format(acc))
    info7=c1.execute("delete from newcustomer where accountno='{}'".format(acc))
    info8=c1.execute("delete from Signup where username='{}'".format(use))
    c1.execute(info6, info7, info8)
    con.commit()
    delay('''
╔═══════════════════════════════════════════════════════════════╦═══╗
║ Account is Successfully Deleted! Thank you! Visit again!      ║ X ║
╚═══════════════════════════════════════════════════════════════╩═══╝
''')
    VAR_2=input("Do you want to continue?(yes/no): ")
    if VAR_2=='yes':
        VAR_2="yes"
        pass
    else:
        exit()
        
def transaction(): # Enter transaction, View transaction
    delay('''
╔═══════════════════════════════════════════════════════════════╦═══╗
║ EBS TRANSACTION PAGE                                          ║ X ║
╚═══════════════════════════════════════════════════════════════╩═══╝
''')
    accountno=int(input('Enter your account number: '))
    info10="select * from newcustomer where accountno="+str(accountno)
    c1.execute(info10)
    data3=c1.fetchall()
    VAR_01="select * from transaction where accountno="+str(accountno)
    c1.execute(VAR_01)
    VAR_02=c1.fetchall()
    print(data3)
    if len(data3)==0:
        delay('''
╔═══════════════════════════════════════════════════════════════╦═══╗
║ Dear customer, No Accounts Found!                             ║ X ║
╚═══════════════════════════════════════════════════════════════╩═══╝
''')
        VAR_2=input("Do you want to continue?(yes/no): ")
    else:
        paid = ""
        delay('''
╔═══════════════════════════════════════════════════════════════╦═══╗
║ ...Checking, If the bill has been paid... please wait!...     ║ X ║
╚═══════════════════════════════════════════════════════════════╩═══╝
''')
        for row in VAR_02:
            paid=row[6]
            print('''
╔═══════════════════════════════════════════════════════════════╦═══╗
║ The bill has been paid: ''' ,paid, """                        ║ X ║
╚═══════════════════════════════════════════════════════════════╩═══╝
""")
        if paid.lower()=='yes':
            delay('''
╔═══════════════════════════════════════════════════════════════╦═══╗
║ -:Bill has been already paid:-                                ║ X ║
╚═══════════════════════════════════════════════════════════════╩═══╝
''')
        else:
            unit=random.randint(0,500)
            print("""
╔═══════════════════════════════════════════════════════════════╦═══╗
║ SYSTEM MESSAGE                                                ║ X ║
╠═══════════════════════════════════════════════════════════════╩═══╣
║                                                                   ║
║ Dear customer, you have consumed """,unit,"""units of electricity ║
║ Note: UNIT PRICE = 30 FILS; VAT = 5%                              ║
║ DEADLINE FOR PAYMENT = 30/31TH OF EVERY MONTH; FINE = 2 AED       ║
║                                                                   ║
╚═══════════════════════════════════════════════════════════════════╝
""")
            amount=0.3*unit
            Todays=dt.date.today()
            VAR_03 = Todays.replace(day = 1)
            deadline = VAR_03 + relativedelta(months = 1) #https://www.khaleejtimes.com/uae/uae-grace-period-to-pay-electricity-bills-extended
            VAT=0.00
            #deadline=dt.date(2022,1,30) # yyyy,mm,dd
            if deadline<Todays:
                fine=(Todays-deadline)*2
                print("Fine due on deadline: ", deadline)
                print("Fine is of: ", fine)
                #totamt=amount+fine
                amount1 = amount + fine
                print("Final amount to payup: ", amount1)
                print('you have delayed for ',Todays-deadline,'days. The fine per day is 2 AED. \n')
                VAT=(5/100)*amount1
                totalamt=amount1+VAT
                paid="yes"
            else:
                totamt=0
                VAT=(5/100)*amount
                totalamt=amount+VAT
            print('Pleae payup ',totalamt,'AED inclding VAT \n')
            payment=input("Please Enter YES to transact: ")
            if payment.lower()=="yes":
                delay("""
╔═══════════════════════════════════════════════════════════════╦═══╗
║ Transaction successful!                                       ║ X ║
╚═══════════════════════════════════════════════════════════════╩═══╝
""")
                paid="yes"
            else:
                delay("""
╔═══════════════════════════════════════════════════════════════╦═══╗
║ PLEASE PAY BEFORE THE DEADLINE                                ║ X ║
╚═══════════════════════════════════════════════════════════════╩═══╝
""")              
                paid="no"
            print(" \n")
            print(accountno,unit,Todays,amount,VAT,totalamt,paid)
            info3="insert into Transaction values({},{},'{}',{},{},{},'{}')".format(accountno,unit,Todays,amount,VAT,totalamt,paid)
            c1.execute(info3)
            con.commit()
            VAR_2=input("Do you want to continue?(yes/no): ")
            if VAR_2=="yes":
                print()
            else:
                delay("""
╔═══════════════════════════════════════════════════════════════╦═══╗
║ Thank you! Visit Again!                                       ║ X ║
╚═══════════════════════════════════════════════════════════════╩═══╝
""")
                exit()
                
def viewcustomerdetails():
    delay("""
╔═══════════════════════════════════════════════════════════════╦═══╗
║ EBS VIEW CUSTOMER DETAILS                                     ║ X ║
╚═══════════════════════════════════════════════════════════════╩═══╝
""")
    accountno=int(input('Enter your account number: '))
    info4="select * from newcustomer where accountno = " + str(accountno)
    c1.execute(info4)
    data1=c1.fetchall()
    if data1==None:
        delay("""
╔═══════════════════════════════════════════════════════════════╦═══╗
║ Account number wrong!!                                        ║ X ║
╚═══════════════════════════════════════════════════════════════╩═══╝
""")
        VAR_2=input("Do you want to continue?(yes/no): ")
    else:
        for row in data1:
            print("Account Number: ", row[0])
            print("bankname: ",row[1])
            print("Name: ",row[2])
            print("Address: ",row[3])
            print("Phone number: ",row[4])
            print("\n")
        info5=("select * from Transaction where accountno = " + str(accountno))
        c1.execute(info5)
        data2=c1.fetchall()
        for row in data2:
            print("Unit: ",row[1])
            print("paid on: ",row[2])
            print("Amount to be paid without VAT: ",row[3])
            print("VAT= 5%", row[4])
            print("amount to be paid With VAT: ",row[5])
            print("\n")
        VAR_2=input("Do you want to continue?(yes/no): ")
        if VAR_2=='yes':
            print()
        else:
            delay("""
╔═══════════════════════════════════════════════════════════════╦═══╗
║ Thank you! Visit Again!                                       ║ X ║
╚═══════════════════════════════════════════════════════════════╩═══╝
""")
            exit()
            
def graph():
    delay("""
╔═══════════════════════════════════════════════════════════════╦═══╗
║ EBS Graphical representation page                             ║ X ║
╚═══════════════════════════════════════════════════════════════╩═══╝
""")
    accountno=int(input('Enter your account number: '))
    info4="select * from newcustomer where accountno = " + str(accountno)
    c1.execute(info4)
    data1=c1.fetchall()
    if data1==None:
        print("Account number wrong!!")
        VAR_2=input("Do you want to continue?(yes/no): ")
    else:
        info9="select " + str(accountno) + ", amtwithvat from Transaction"
        c1.execute(info9)
        L1,L2,=[],[]
        for i in c1.fetchall():
            L1.append(i[0])
            L2.append(i[1])
        plt.bar(L1,L2)
        plt.title("GRAPH")
        plt.show()
        VAR_2=input("Do you want to continue?(yes/no): ")
        if VAR_2=='yes':
            print()
        else:
            delay("""
╔═══════════════════════════════════════════════════════════════╦═══╗
║ Thank you! Visit Again!                                       ║ X ║
╚═══════════════════════════════════════════════════════════════╩═══╝
""")
            exit()
            
def logo():
    print("""
╔════════════════════════════════════════════════════════════════════════════════════════╦═══╗
║ EBS LOGO                                                                               ║ X ║
╠════════════════════════════════════════════════════════════════════════════════════════╩═══╣
║                                                                                            ║
║                                           cO0Oc                                            ║
║                                           dNWNo                                            ║
║                                           oNMNo                                            ║
║                     ;c;                   lXMXl                  ;cc;                      ║
║                    ;kNXx:                 c0W0:                 o0WXo                      ║
║                     :xXWKd;            ;:cldkdlc:;            lONNOl                       ║
║                       ;dKN0o      coxOKXXXXKKKXXXK0Oxl:     ckNNkc                         ║
║                          o0Xk: cx0XKOdlc;;     ;;cox0XXOd: oKKx;                           ║
║                            coxOXKxc                  ;lkXXkdl                              ║
║                            :kNKo                        ;xXKd;                             ║
║                           lKNk                  :;        c0NO:                            ║
║                          lKNx                 ;lc          :0WO:                           ║
║                         ;OWO;               ;:ol            cXNd                           ║
║                         lXNo              ;codo;             kW0:                          ║
║            ;::::;;;;    dNXc             :ldddc              dWKc    ;;;:::::              ║
║           ;kNNNXXXKKK0d;dNXc            coddxo: ;;;          dWKc:k0KKXXXXNNXd             ║
║            :ooollcccc:; lXNo          ;lddddddooodd:         kWO; ;:ccclllool;             ║
║                         ;OWk;        cdkkkkxddddxo;         cKNd                           ║
║                          lXNd        ;::::lddddxc          ;OWO;                           ║                                       
║                           oXXd            :odxd:          :ON0:                            ║                                       
║                            lKNk:         :oxxo           l0NO:                             ║                                       
║                             ;kNKd;      ;odc           :kNXd                               ║                                       
║                            ;;;lKN0l     lo;          ;dXNk: ;                              ║                                       
║                          :dK0c  dXXx;  ;c           cONKl  dKOo;                           ║                                       
║                        cxXNO:    cKNk;             lKNk;    lKN0d:                         ║                                       
║                      lONW0l       cKWx            :0Wk        dXWKx:                       ║                                       
║                     xNWKo          oNXl           xWK:         ;xNWKl                      ║                                       
║                     :ol            cKWKxxxxxxxxxxkXWk            :ol;                      ║                                       
║                                     lxkkkkkkkkkkxxkxc                                      ║                                       
║                                      ldddddddddddddc                                       ║                                      
║                                     ;oxxxxxxxxxxxxxl;                                      ║                                    
║                                     ;oxxxxxxxxxxxxxl;                                      ║                                      
║                                     ;oxxdxxxdxxxxxdc;                                      ║                                      
║                                     ;dxxxxxxxxxxxxxl;                                      ║                                       
║                                      looddddddddoooc                                       ║                                       
║                                          lxkkkd:                                           ║                                       
║                                           :llc;                                            ║                                      
║                   __        __   _                            _                            ║                                          
║                   \ \      / /__| | ___ ___  _ __ ___   ___  | |_ ___                      ║                                       
║                    \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \                     ║                                       
║                     \ V  V /  __/ | (_| (_) | | | | | |  __/ | || (_) |                    ║
║                      \_/\_/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/                     ║
║                                                                                            ║ 
║                                                                                            ║ 
║             █▀▀ █░░ █▀▀ █▀▀ ▀█▀ █▀█ █ █▀▀ █ ▀█▀ █▄█   █▄▄ █ █░░ █░░ █ █▄░█ █▀▀             ║  
║             ██▄ █▄▄ ██▄ █▄▄ ░█░ █▀▄ █ █▄▄ █ ░█░ ░█░   █▄█ █ █▄▄ █▄▄ █ █░▀█ █▄█             ║ 
║                                                                                            ║
║                                   █▀ █▄█ █▀ ▀█▀ █▀▀ █▀▄▀█                                  ║
║                                   ▄█ ░█░ ▄█ ░█░ ██▄ █░▀░█                                  ║
║                                                                                            ║
║                                                                                            ║
╚════════════════════════════════════════════════════════════════════════════════════════════╝

\n""")


import mysql.connector as m, random, datetime as dt
import matplotlib.pyplot as plt
from getpass import getpass
import sys, time
from dateutil.relativedelta import relativedelta
con = m.connect(host='localhost',user='root',password='root')
cursor=con.cursor()
c1=con.cursor()
if con.is_connected():
    delay("""
╔═══════════════════════════════════════════════════════════════╦═══╗
║ SYSTEM MESSAGE                                                ║ X ║
╠═══════════════════════════════════════════════════════════════╩═══╣
║ Mysql - Python connection, Successful                             ║
╚═══════════════════════════════════════════════════════════════════╝
""") #success

else:
    delay("""
╔═══════════════════════════════════════════════════════════════╦═══╗
║ SYSTEM MESSAGE                                                ║ X ║
╠═══════════════════════════════════════════════════════════════╩═══╣
║ Error! Try again!                                                 ║
╚═══════════════════════════════════════════════════════════════════╝
""")
VAR_1="yes"
VAR_2="yes"
try:
    sql3=("show databases;")
    cursor.execute(sql3)
    rs=cursor.fetchall()
    if "EBS" in rs:
        delay("""
╔═══════════════════════════════════════════════════════════════╦═══╗
║ SYSTEM MESSAGE                                                ║ X ║
╠═══════════════════════════════════════════════════════════════╩═══╣
║ If statement Database exists!                                     ║
╚═══════════════════════════════════════════════════════════════════╝
""")
    else:
        databasecreation1()
        #database creation or checking
        tablecreation_newcustomer()
        #newcustomer table creation or checking    
        tablecreation_signup()
        #signup table creation or checking
        tablecreation_transaction()
        #transaction table creation or checking
        delay("Else: Statement Database and tables created, Successful\n")
        con=m.connect(host='localhost',user='root',password='root',database="EBS")
        cursor=con.cursor()
        c1=con.cursor()
        if con.is_connected():
            delay("""
╔═══════════════════════════════════════════════════════════════╦═══╗
║ SYSTEM MESSAGE                                                ║ X ║
╠═══════════════════════════════════════════════════════════════╩═══╣
║ Mysql - Python connection, Successful                             ║
╚═══════════════════════════════════════════════════════════════════╝
""")
        else:
            delay("""
╔═══════════════════════════════════════════════════════════════╦═══╗
║ SYSTEM MESSAGE                                                ║ X ║
╠═══════════════════════════════════════════════════════════════╩═══╣
║ Mysql - Python connection, Failed                                 ║
╚═══════════════════════════════════════════════════════════════════╝
""")
        
except:
    con=m.connect(host='localhost',user='root',password='root',database="EBS")
    cursor=con.cursor()
    c1=con.cursor()
    if con.is_connected():
        delay("""
╔═══════════════════════════════════════════════════════════════╦═══╗
║ SYSTEM MESSAGE                                                ║ X ║
╠═══════════════════════════════════════════════════════════════╩═══╣
║ Except statement connection, Successful                           ║
╚═══════════════════════════════════════════════════════════════════╝
""") #success
    else:
        delay("""
╔═══════════════════════════════════════════════════════════════╦═══╗
║ SYSTEM MESSAGE                                                ║ X ║
╠═══════════════════════════════════════════════════════════════╩═══╣
║ Except statement connection, Failed                               ║
╚═══════════════════════════════════════════════════════════════════╝
""")
    VAR_1="yes"
    VAR_2="yes"
    logo()
    
if VAR_1.lower()=="yes":
    #admin priveledeges 
    delay("""
╔═══════════════════════════════════════════════════════════════╦═══╗
║ EBS Registration page                                         ║ X ║
╚═══════════════════════════════════════════════════════════════╩═══╝
""")
    delay('''
╔═══════════════════════════════════════════════════════════════╦═══╗
║ SYSTEM MESSAGE                                                ║ X ║
╠═══════════════════════════════════════════════════════════════╩═══╣
║'''dt.datetime.now()'''                                                         ║
║ 1. SIGN UP                                                        ║
║ 2. LOG IN                                                         ║
║ 3. EXIT                                                           ║
║                                                                   ║
╚═══════════════════════════════════════════════════════════════════╝
''') #1. New user , 2. Existing user, 3. break

    choice1=int(input(('ENTER YOUR CHOICE: ')))
    if choice1==1:
        signup()
        login()
        data=c1.fetchall()
    elif choice1==2:
        login()
        data=c1.fetchall()
    elif choice1==3:
        delay("""
╔═══════════════════════════════════════════════════════════════╦═══╗
║ Thank you! Visit Again!                                       ║ X ║
╚═══════════════════════════════════════════════════════════════╩═══╝
""")
        VAR_1='no'       
    else:
        delay("invalid choice \n")
        VAR_2=input("Do you want to continue?(yes/no): ")
else:
    delay("""
╔═══════════════════════════════════════════════════════════════╦═══╗
║ Thank you! Visit Again!                                       ║ X ║
╚═══════════════════════════════════════════════════════════════╩═══╝
""")
    VAR_1="no"
    exit()
if VAR_2.lower()=="yes":
    _Intro(data)
else:
    delay("""
╔═══════════════════════════════════════════════════════════════╦═══╗
║ Thank you! Visit Again!                                       ║ X ║
╚═══════════════════════════════════════════════════════════════╩═══╝
""")
    VAR_1="no"
    exit()
    
# Need to add List
'''
1. Sort
2. Admin priviledges
'''
