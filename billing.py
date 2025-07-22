import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",password="vivek2211",database="biling")
cur=con.cursor()

#cur.execute("create table product (pid int primary key auto_increment ,pname varchar(40),ppr int not null)")

def add():
    pid=int(input("enter pid:"))
    pname=input("enter pnaame:")
    #eloc=input("enter location:")
    ppr=int(input("enter price:"))
                 
    q="insert into product (pid,pname,ppr)values(%s,%s,%s)"
    val=(pid,pname,ppr)

    cur.execute(q,val)

    con.commit()

def show():
    cur.execute("select * from product")
    data=cur.fetchall()
    print("pid    pname   ppr")
    print("--------------------")
    for x in data:
        print(x[0]," ",x[1]," ",x[2])



def delete():
    pid=int(input("enter pid for delete:"))
    q="delete from product where pid=%s"
    val=(pid,)
    cur.execute(q,val)
    con.commit()
    print("--------------deleted------------")

def update():
    ppr=int(input("enter price:"))
    pid=int(input("enter product id:"))
    q="update product set ppr=%s where pid=%s"
    val=(ppr,pid,)
    cur.execute(q,val)
    con.commit()
    print("----------------------updated--------------")


#def bill():
    
    

def admin():   
    ch=1
    while ch!=0:
        
        print("****************enter choice********************* ")
        print("1=>>>  add the product")
        print("2=>>>  show added product")
        print("3=>>>  delet product")
        print("4=>>>  update product")
        print("5=>>>  exit")

        ch=int(input())
        if(ch==1):
            add()
        elif(ch==2):
            show()
        elif(ch==3):
            delete()
        elif(ch==4):
            update()
        else:
            ch=0
    else:
        print("************task end**************")
def bill():
    pid=-1
    sum=0
    while pid!=0:
        print("-1=>> exit")
        pid=int(input("pic product from list:"))
        if(pid!=-1):
            qu=int(input("quantity:"))
            q="select * from product where pid=%s  "
            val=(pid,)
            cur.execute(q,val)
            data=cur.fetchall()
            
            for x in data:
                print(x[0]," ",x[1],"  ",x[2])
                tc=x[2]*qu
                sum=sum+tc
                #print("selected",pid)
        elif(pid==-1):
            
            pid=0
    return sum
ch=1
while ch!=0:            
    print("****************Welcome to billing System********************* ")
    print("1=>>>  Admin")
    show()
    print("3=>>>  select product ")
    print("4=>>>  exit")

    ch=int(input())
    if(ch==1):
        admin()
    elif(ch==2):
        show()
    elif(ch==3):
        total=bill()    
    else:
            ch=0
else:
    print("your total bill",total)
    print("************thanks for comming**************")
con.close

# 2025-07-02-0

# 2025-07-02-1

# 2025-07-02-2

# 2025-07-02-3

# 2025-07-03-0

# 2025-07-03-1

# 2025-07-03-2

# 2025-07-03-3

# 2025-07-03-4

# 2025-07-03-5

# 2025-07-04-0

# 2025-07-04-1

# 2025-07-04-2

# 2025-07-04-3

# 2025-07-04-4

# 2025-07-04-5

# 2025-07-04-6

# 2025-07-05-0

# 2025-07-05-1

# 2025-07-05-2

# 2025-07-05-3

# 2025-07-05-4

# 2025-07-06-0

# 2025-07-06-1

# 2025-07-06-2

# 2025-07-06-3

# 2025-07-07-0

# 2025-07-07-1

# 2025-07-07-2

# 2025-07-07-3

# 2025-07-07-4

# 2025-07-07-5

# 2025-07-08-0

# 2025-07-08-1

# 2025-07-08-2

# 2025-07-08-3

# 2025-07-08-4

# 2025-07-08-5

# 2025-07-08-6

# 2025-07-09-0

# 2025-07-09-1

# 2025-07-09-2

# 2025-07-09-3

# 2025-07-09-4

# 2025-07-09-5

# 2025-07-09-6

# 2025-07-10-0

# 2025-07-10-1

# 2025-07-10-2

# 2025-07-10-3

# 2025-07-10-4

# 2025-07-10-5

# 2025-07-11-0

# 2025-07-11-1

# 2025-07-11-2

# 2025-07-11-3

# 2025-07-11-4

# 2025-07-12-0

# 2025-07-12-1

# 2025-07-12-2

# 2025-07-12-3

# 2025-07-12-4

# 2025-07-12-5

# 2025-07-13-0

# 2025-07-13-1

# 2025-07-13-2

# 2025-07-13-3

# 2025-07-14-0

# 2025-07-14-1

# 2025-07-14-2

# 2025-07-14-3

# 2025-07-15-0

# 2025-07-15-1

# 2025-07-15-2

# 2025-07-15-3

# 2025-07-15-4

# 2025-07-15-5

# 2025-07-15-6

# 2025-07-15-7

# 2025-07-16-0

# 2025-07-16-1

# 2025-07-16-2

# 2025-07-16-3

# 2025-07-16-4

# 2025-07-16-5

# 2025-07-17-0

# 2025-07-17-1

# 2025-07-17-2

# 2025-07-17-3

# 2025-07-18-0

# 2025-07-18-1

# 2025-07-18-2

# 2025-07-18-3

# 2025-07-18-4

# 2025-07-18-5

# 2025-07-19-0

# 2025-07-19-1

# 2025-07-19-2

# 2025-07-19-3

# 2025-07-19-4

# 2025-07-19-5

# 2025-07-19-6

# 2025-07-19-7

# 2025-07-20-0

# 2025-07-20-1

# 2025-07-20-2

# 2025-07-20-3

# 2025-07-20-4

# 2025-07-20-5

# 2025-07-20-6

# 2025-07-21-0

# 2025-07-21-1

# 2025-07-21-2

# 2025-07-21-3

# 2025-07-21-4

# 2025-07-21-5

# 2025-07-22-0

# 2025-07-22-1

# 2025-07-22-2

# 2025-07-22-3

# 2025-07-22-4

# 2025-07-22-5

# 2025-07-22-6

# 2025-07-22-7
