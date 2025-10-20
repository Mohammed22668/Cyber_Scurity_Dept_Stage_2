from .trainning import Car

# class Hello:
#     def __init__(self,name,age,phone):
#         self.name = name
#         self.age = age
#         self.phone = phone
        
#     def print_info(self):
#         print(f"Welcome {self.name}")
#         print(f"Age = {self.age}") 
#         print(f"Phone = {self.phone}")
        


# name1 = Hello("Firas" , 27 , "077xxxxxxxx")
# name1.name += " Ahmed"
# name1.print_info()


# name2 = Hello("Ali", 34,"07724234424")
# name2.age += 5
# name2.print_info()

###################################

class Student:
    def __init__(self,fName,lName,stage,std_number,group,list_degree):
        self.fName = fName
        self.lName = lName
        self.stage = stage
        self.group = group
        self.list_degree = list_degree
        self.fullName = fName+" "+lName
        self.std_number = std_number
        
        
    def student_info(self):
        print(f"Studen Name : {self.fullName}")
        print(f"Student Stage : {self.stage}")
        print(f"Student group : {self.group}")
        print(f"Student Number : {self.std_number}")
        print(f"Student Degree : {self.list_degree}")
        
    def student_email(self):
        print(f"Student Email : {self.std_number}@collage.com")  
        
    def add_degree(self,degree):
        self.list_degree.append(degree)  
        
    def avirage(self):
        sum = 0
        avg = 0
        if len(self.list_degree) >0 :
            for i in self.list_degree:
                sum += i
            avg = sum/len(self.list_degree)  
            return avg  
        else :
            print("Student dont have any degree")       
        


# std1 = Student("Alaa","Sami",2,"20250024001","B",[])   
# # std1.add_degree(90)
# # std1.add_degree(85)
# std1.student_info()   
# std1.student_email()   
# print("Avg =: ",std1.avirage())
            
#######################################


class BankAccount():
    def __init__(self,fName,lName,balance,expire_date,phone,account_number):
        self.fName = fName
        self.lName = lName
        self.balance = balance
        self.expire_date = expire_date
        self.phone= phone
        self.account_number = account_number
        
    def get_balance(self):
        return self.balance
    
    def deposit(self,amount):
        self.balance += amount
        return self.balance
    
    def withrow(self,amount):
        if self.balance > amount :  
            self.balance -= amount   
            return self.balance 
        else : 
            print("Cannot do it ")
        
    def get_info(self):
        print(f"Account Name : {self.fName} {self.lName}")  
        print(f"Account Number : {self.account_number}")  
        


# account1 = BankAccount("Ahmed","Ali",250000,"12-12-2030","07712345678","12323213545")
# account1.deposit(150000)
# account1.withrow(600000)
# print("Balance : ",account1.get_balance())        
         