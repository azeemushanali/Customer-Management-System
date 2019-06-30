import random 


#BLL
login_id = "azeem"
login_pwd = '123'
listid = []
listname = []
listage = []
listsalary = []
flag = 0



       
def getAge():
    global age
    while(1):
        #age = int(input("Enter Customer's Age"))
        age = input("Enter Customer Age")
        if(age.isnumeric()):
            if(int(age)<=110 and int(age)>=10):
                return int(age)            
            else:
                print("Enter age b/w 10 to 100")
        else:
                print("Enter age in Numeric Form")
                
                
def checkAge(age):
    age = str(age)
    while(1):
        if(age.isnumeric()):
            if(int(age)<=110 and int(age)>=10):
                return int(age)            
                break
            else:
                print("Enter age b/w 10 to 100")
                
        else:
            print("Enter age in Numeric Form")
                
                

        
                
def getName():
    global j
    while(1):
        name1 = input("Enter your name")
        name = chechalphabet(name1)
        if(j==0):
            return name
    
                
 
def chechalphabet(x):
    global j
    j=0
    for i in range(len(x)):
        if((x[i].isnumeric())):
            j+= 1
    if(j>0):
        print("Enter name in alphabets")
    else:
        return x
    

def genID(name,age):
    global generated_id
    while(1):
        id = random.randint(1,999)
        generated_id = name[:3] + str(id) +str(age)
        print("ID is",generated_id)
        if (id in listid):
            genID(name,age)
        else:
            return generated_id
            break
        
 

               
def addCust(generated_id,name,age):
    listid.append(generated_id)
    listname.append(name)
    listage.append(age)
    
def search_index_by_id(id):
    index = listid.index(id)
    return index
def search_index_by_name(name):
    index = listname.index(name)
    return index
def search_index_by_age(age):
    index = listage.index(age)
    return index
def modifyCust_id(id):
    listid[index] = id
def modifyCust_name(name):
    listname[index] = name
def modifyCust_age(age):
    listage[index] = age
def delCust(index):
    listid.pop(index)
    listname.pop(index)
    listage.pop(index)  
    
    
#PL v-0


def disCust(i):
    print(listname[i],"\t\t\t",listage[i],"\t\t\t",listid[i])


#PL
print("Welcome to my CMS Project,Be ready with your id and password!")
print("Feel free to exit by pressing Enter key in id or password section")
quit_program = 0
while(1):
    if(flag<=3):
        cms_id = input("Enter your CMS Login ID")
        cms_pwd = input("Enter your CMS Login Password")
        if(cms_id == login_id and login_pwd == cms_pwd):
            print("You made it!!")
            while(1):
                ch = input('''Operations you can do in my CMS-
          1- Add Customer
          2- Modify Customer
          3- Search Customer
          4- Delete Customer
          5- Display All
          6- Exit
          Enter your choice-->
          ''')
                if(ch.isnumeric()):
                    if(ch == '1'): #Add Cust
                        global name,age
                        
                        name = getName()
                        age = getAge()
                        generated_id = genID(name,age)
                        addCust(generated_id,name,age)
                        
                        
                        
                    elif(ch=='2'): #ModifyCust
                        md = 0
                        while(1):
                            ch2 = input('''Enter the way of modification-
                                            1- By ID
                                            2- By Age
                                            3- By Name
                                            ''')
                            if(ch2.isnumeric()):
                                
                                if(ch2=='1'):
                                    md +=1
                                    id = input("Enter the id")
                                    if(id in listid):
                                        ch21 = input('''Enter the entity you want to modify
                                         1- ID
                                         2- Age
                                         3- Name''')
                                        if(ch21 == '1'):    
                                            index = search_index_by_id(id)
                                            name = listname[index]
                                            age = listage[index]
                                            id = genID(name,age)
                                            modifyCust_id(id)
                                        
                                        elif(ch21 == '2'):
                                            age = getAge()
                                            index = search_index_by_id(id)
                                            
                                            modifyCust_age(age)
                                        elif(ch21 == '3'):
                                            name = input("Enter the updated Name")
                                            index = search_index_by_id(id)
                                            modifyCust_name(name)
                                        else:
                                            print("Kripya Number Jaach le")
                                    else:
                                        print(f"Enter the valid id;No Customer with id {id} found in our database")
                            
                            
                                elif(ch2 == '2'):
                                    md +=1
                                    age = int(input("Enter the age"))
                                    if(age in listage):
                                        index = search_index_by_age(age)
                                        ch22 = input('''Enter the entity you want to modify
                                             1- ID
                                             2- Age
                                             3- Name''')
                                        if(ch22 == '1'):
                                            id = genID(name,age)
                                            modifyCust_id(id)
                                        elif(ch22 == '2'):
                                            age = getAge()
                                            modifyCust_age(age)
                                        elif(ch22 == '3'):
                                            name = input("Enter the updated name")
                                            modifyCust_name(name)
                                        else:
                                            print("Wrong Choice")
                                    else:
                                        
                                        print(f"Person with age {age} not found")
                            
                                elif(ch2=='3'):
                                    md +=1
                                    name = input("Enter the name")
                                    if(name in listname):
                                        index = search_index_by_name(name)
                                        ch23 = input('''Enter the entity you want to modify
                                             1- ID 
                                             2- Name
                                             3- Age''')
                                        if(ch23 == '1'):
                                            name = listname[index]
                                            age = listage[index]
                                            id = genID(name,age)
                                            modifyCust_id(id)
                                        elif(ch23 == '2'):
                                            name = input("Enter the correct name")
                                            modifyCust_name(name)
                                        elif(ch23 == '3'):
                                            age = getAge()
                                            modifyCust_age(age)
                                        else:
                                            print("Wrong Choice")
                                    else:
                                        print(f"Customer with name - {name} not found in database")
                            if(md==1):
                                break
                                
                        
                        
                        
                        
                        
                    elif(ch == '3'):    #Search Customer
                        sc = 0
                        while(1):
                            
                            ch3 = input('''Enter your choice for search-
                                    1- By ID
                                    2- By Age
                                    3- By Name
                                    ''')
                            if(ch3.isnumeric()):
                                if(ch3 == '1'):
                                    while(1):
                                        id = input("Enter the ID")
                                        if(id in listid):
                                            index = search_index_by_id(id)
                                            print("Customer details are --> Cust Name-",listname[index],"Cust Id",listid[index],"Cust Age",listage[index])
                                            sc +=1
                                            break
                                        
                                        else:
                                            print("Enter valid id")
                                
                                elif(ch3 == '2'):
                                    while(1):
                                        age  = input("Enter the age")
                                        age = int(age)
                                        if(age in listage):
                                            index = search_index_by_age(age)
                                            print("Customer details are --> Cust Name-",listname[index],"Cust Id",listid[index],"Cust Age",listage[index])
                                            sc += 1
                                            break
                                        else:
                                            print("Enter correct age")
                                elif(ch3 == '3'):
                                    while(1):
                                        name = input("Enter the name")                               
                                        if (name in listname):
                                            index = search_index_by_name(name)
                                            print("Customer details are --> Cust Name-",listname[index],"Cust Id",listid[index],"Cust Age",listage[index])
                                            sc += 1
                                            break
                                        else:
                                            print(f"Peron with name {name} not found!!")
                                else:
                                    print("Wrong Choice")
                            else:
                                print("Enter choice in numbers only")
                            if(sc >= 1):
                                break
                    elif(ch == '4'):   #Delete Customer
                        fl = 0
                        while(1):
                            
                            ch4 =  input('''Enter your way of deleting
                                             1- By id 
                                             2- By Age
                                             3- By Name''')
                            if(ch4.isnumeric()):
                                if(ch4 == '1'):
                                    id = input("Enter the id")
                                    if (id in listid):
                                        index=search_index_by_id(id)
                                        delCust(index)
                                        print("Customer Deleted Succesfully")
                                        fl += 1
                                        break
                                    else:
                                        print(f"Customer with id {id} not found" )
                                elif(ch4 == '2'):
                                    age = int(input("Enter the age"))
                                    if (age in listage):
                                        index=search_index_by_age(age)
                                        delCust(index)
                                        print("Customer Deleted Succesfully")
                                        fl += 1
                                        break
                                    else:
                                        print(f"Customer with age {age} not found")
                                elif(ch4 == '3'):
                                    while(1):
                                        name = input("Enter the name")
                                        if(name in listname):
                                            index=search_index_by_name(name)
                                            delCust(index)
                                            print("Customer Deleted Succesfully")
                                            fl += 1
                                            break
                                        else:
                                            print("Name not fount,Please re-enter")
                                                
                                            
                                else:
                                        print("Wrong Choice")
                                
                            else:
                                print("Enter the choice in numbers only")
                            if(fl >= 1):
                                break
                            
                            
                    elif(ch == '5'):   #display all
                        print("Cust Name \t\t Cust Age \t\t Cust ID ")
                        for i in range(len(listid)):
                            disCust(i)
                    elif(ch == '6'): #Exit
                        
                        print("Thank you for using my project")
                        quit_program +=1
                        #quit()   
                        break 
                else:
                    print("Enter the choice in numbers only")
        elif(cms_id == '' or cms_pwd == ''):
            print("You opted to exit by pressing enter key")
            break
        else:
            print("Wrong ID or Password")
            flag = flag + 1
    else:
        print('''You exceeded the max limit-
          Try again later''')
        break
    if(quit_program >=1):
        break
