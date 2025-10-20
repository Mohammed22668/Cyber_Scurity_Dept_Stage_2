
# class Hello:
#     def __init__(self,name,age,phone):
#         self.name = name
#         self.age = age
#         self.phone = phone
    
#     def print_info(self):
#         print(f"Welcome {self.name} your age is {self.age}")
        
        
#     def get_phone(self):
#         print(f"Phone Number = {self.phone}")    
        
#     def change_phone(self,new_phone):
#         self.phone = new_phone     
        


# name1 = Hello("Ali",25,"077777777")
# name1.print_info() 
# name1.get_phone()          
# name1.change_phone("07712345678")

# name2 = Hello("Ahmed", 35, "0770000000")
# name2.name += " Salman"

# name2.print_info() 

#########################################

# class Student:
#     def __init__(self,name,student_number,stage,group,list_dgree):
#         self.name = name 
#         self.stage = stage
#         self.group = group
#         self.list_dgree= list_dgree
#         self.student_number = student_number
        
#     def print_info(self):
#         print(f"Student Name : {self.name}")
#         print(f"Student Stage : {self.stage}")    
#         print(f"Student Group : {self.group}")
#         print(f"Student Number : {self.student_number}")  
    
    
#     def student_email(self):
#         print(f"Email : {self.student_number}@collage.com")   
        
#     def set_degree(self,degree):
#         self.list_dgree.append(degree)  
        
#     def print_degree(self):
#         print(f"List degree {self.list_dgree}")       
         
    
# std1 = Student("Ahmed", 2025123001,2,"A",[])

# std1.print_info()        
# std1.student_email()

# std1.set_degree(90)
# std1.set_degree(100)
# std1.print_degree()



############################################
class BankAccount :
    def __init__(self,fName,lName,account_number , balance,phone):
        self.fName = fName
        self.lName= lName
        self.account_number = account_number
        self.balance = balance
        self.phone = phone
        
    
    def get_balance(self):
        print (f"your balance is {self.balance}")
        
        
    def deposit (self,amount):
        self.balance +=amount 
        
    def withdrow(self,amount):
        if self.balance >= amount :
            self.balance -= amount
        else :
            print("your balance is not enugh")
            
    def account_info(self):
        print(f"your account name is : {self.fName} {self.lName}")
        print(f"phone is : {self.phone}")
        print(f"your balance is: {self.balance}") 
        print(f"your account number: {self.account_number}")           
        
        


account1 = BankAccount("Ahmed","Fouad","342343424",1000,"07734242424") 
account1.deposit(500)
account1.withdrow(1200)
account1.account_number = "000000"
account1.account_info()       
