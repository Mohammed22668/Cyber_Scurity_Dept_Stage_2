# class ClassName:
#     def _init_(self, parameters):
#         # هذا هو الكونستركتر (دالة التهيئة)
#         self.attribute1 = value1
#         self.attribute2 = value2

#     def method_name(self):
#         # دالة داخل الكلاس
#         print("This is a method")

#####################################
class Hello:
    def say_hello(self):
        print("مرحبا بكم في عالم البرمجة الكيانية!")

obj = Hello()
obj.say_hello()


##############################
class Student:
    def _init_(self, name, age):
        self.name = name
        self.age = age

    def print_info(self):
        print(f"اسم الطالب: {self.name}, عمره: {self.age}")

student1 = Student("Ali", 20)
student1.print_info()



###################################
class Car:
    def _init_(self, brand, model):
        self.brand = brand
        self.model = model

    def start(self):
        print(f"السيارة {self.brand} {self.model} بدأت التشغيل!")

mycar = Car("Toyota", "Camry")
mycar.start()


############################
class BankAccount:
    def _init_(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"تم إيداع {amount}، الرصيد الجديد = {self.balance}")

account1 = BankAccount("Sara", 500)
account1.deposit(200)


