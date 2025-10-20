# from .lacture_basic import  BankAccount


class BankAccount:
    def __init__(self,account_name,balance,account_expire,phone_number):
        self.account_name = account_name
        self.balance = balance
        self.account_expire = account_expire
        self.phone_number = phone_number
        
    def get_balance(self):
        return self.balance
    
    def deposit(self,amount):
        self.balance += amount
        
    def withdraw(self,amount):
        if amount < self.balance :
            self.balance -= amount   
        else : 
            print(f"Cannot do this operations")         
    
    
    def get_expired(self):
        return self.account_expire            

# class ClassName:
#     def _init_(self, parameters):
#         # هذا هو الكونستركتر (دالة التهيئة)
#         self.attribute1 = value1
#         self.attribute2 = value2

#     def method_name(self):
#         # دالة داخل الكلاس
#         print("This is a method")
# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def print_info(self):
#         print(f" Student Name: {self.name}, Age is: {self.age}")

# student1 = Student("Ali", 20)
# student1.name = "Salah"
# student1.print_info()

# student2 = Student("Ahmed",33)
# student2.print_info()

######################################

         
        
        
# car1 = Car("Nissan","White",2024,1500,50000,150)


# car2 = Car("Marcides","Black",2025,3000,100000,200)     


# car1.get_color()   
# car1.set_price(30000)
# car1.set_speed(250)
# # car1.car_info()
# car2.get_color()
# car2.set_speed(300)
# car2.car_info()

#######################################

account1 = BankAccount("Ahmed",540000,"10-10-2026","0770000000")

account1.deposit(60000)
print(f"Your balance is ",account1.get_balance())

account1.withdraw(150000)
print(f"Your balance is ",account1.get_balance())
