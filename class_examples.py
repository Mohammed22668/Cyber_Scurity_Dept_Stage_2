# # class ClassName:
# #     def _init_(self, parameters):
# #         # هذا هو الكونستركتر (دالة التهيئة)
# #         self.attribute1 = value1
# #         self.attribute2 = value2

# #     def method_name(self):
# #         # دالة داخل الكلاس
# #         print("This is a method")

# #####################################
# class Hello:
#     def say_hello(self):
#         print("مرحبا بكم في عالم البرمجة الكيانية!")

# obj = Hello()
# obj.say_hello()


# ##############################
# class Student:
#     def _init_(self, name, age):
#         self.name = name
#         self.age = age

#     def print_info(self):
#         print(f"اسم الطالب: {self.name}, عمره: {self.age}")

# student1 = Student("Ali", 20)
# student1.print_info()



# ###################################
# class Car:
#     def _init_(self, brand, model):
#         self.brand = brand
#         self.model = model

#     def start(self):
#         print(f"السيارة {self.brand} {self.model} بدأت التشغيل!")

# mycar = Car("Toyota", "Camry")
# mycar.start()


# ############################
# class BankAccount:
#     def _init_(self, owner, balance):
#         self.owner = owner
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance += amount
#         print(f"تم إيداع {amount}، الرصيد الجديد = {self.balance}")

# account1 = BankAccount("Sara", 500)
# account1.deposit(200)


##########################################################################################################
# =========================
# Week 8: Access Modifiers in Python
# =========================

# -------------------------
# Example 1: Public Members
# -------------------------
# class PersonPublic:
#     def __init__(self, name, age):
#         self.name = name  # public
#         self.age = age    # public

# p1 = PersonPublic("Ali", 25)
# # print("Example 1 - Public Members:")
# print(p1.name)  # Ali
# print(p1.age)   # 25
# print("-" * 40)

# ----------------------------
# Example 2: Protected Members
# ----------------------------
class PersonProtected:
    def __init__(self, name, age):
        self._name = name   # protected
        self._age = age     # protected

# class EmployeeProtected(PersonProtected):
#     def show_info(self):
#         print(f"Employee Name: {self._name}, Age: {self._age}")

# e1 = EmployeeProtected("Sara", 30)
# print("Example 2 - Protected Members:")
# e1.show_info()
# print("-" * 40)

# # --------------------------
# # Example 3: Private Members
# # --------------------------
# class PersonPrivate:
#     def __init__(self, name, age):
#         self.__name = name   # private
#         self.__age = age     # private

#     def display(self):
#         print(f"Name: {self.__name}, Age: {self.__age}")

# p2 = PersonPrivate("Omar", 28)
# print("Example 3 - Private Members:")
# p2.display()
# # The following line would cause an error
# print(p2.__name)
# print("-" * 40)

# # ---------------------------------------
# # Example 4: Access Private via Getters/Setters
# # ---------------------------------------
# class PersonGetterSetter:
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age

#     # Getter
#     def get_name(self):
#         return self.__name

#     # Setter
#     def set_name(self, new_name):
#         self.__name = new_name

# p3 = PersonGetterSetter("Khalid", 35)
# print("Example 4 - Getter and Setter for Private:")

# print(p3.get_name())  # Khalid
# p3.set_name("Ahmed")
# print(p3.get_name())  # Ahmed
# print("-" * 40)

# # ---------------------------------------
# # Example 5: Combined Public, Protected, Private
# # ---------------------------------------
# class PersonCombined:
#     def __init__(self, name, age):
#         self.name = name       # public
#         self._age = age        # protected
#         self.__salary = 5000   # private

#     def show_info(self):
#         print(f"Name: {self.name}, Age: {self._age}, Salary: {self.__salary}")

# class EmployeeCombined(PersonCombined):
#     def show_employee(self):
#         print(f"Name: {self.name}, Age: {self._age}")  # can access protected
#         # print(self.__salary)  # error! cannot access private

# e2 = EmployeeCombined("Ali", 40)
# print("Example 5 - Combined Access Modifiers:")
# e2.show_info()      # Name: Ali, Age: 40, Salary: 5000
# e2.show_employee()  # Name: Ali, Age: 40
# print(e2.name)      # Ali
# # The following lines would cause errors or are not recommended
# print(e2._age)     
# print(e2.__salary) 
# ###################################


class Staff:
    def __init__(self,name,age,email,salary):
        self.name = name
        self._age = age
        self.email = email
        self.__salary = salary
        
    def show_info(self): 
        print(f'Name : {self.name} - Age : {self._age} - Email : {self.email} - Salary : {self.__salary}')  
    
    def get_salary(self):
        print(f'Salary : {self.__salary}')     
    
    def set_salary(self,new_salary):
        self.__salary = new_salary  
        
    def increment_salary(self,increment):
        self.__salary += increment 
        
    def dcrement_salary(self,value):
        if value > self.__salary :
            print("Salary is not enough!")
        else :
            self.__salary -= value
        
            
        
          
        


staff1 = Staff("Ahmed", 39 , "Ahmed@gmail.com" , 500000)
# staff1.show_info()
# print(staff1.__salary)
staff1.set_salary(200000)
staff1.increment_salary(50000)
staff1.dcrement_salary(300000)
staff1.get_salary()



