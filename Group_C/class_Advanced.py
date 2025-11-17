

# class Student:
#     def __init__(self,name,age):
#         self.name = name 
#         self.age = age
#         print(f"Student class Created with Value {self.name} - {self.age}")
        
#     def print_age(self):
#         print(f"Age = {self.age}")    
        
        
#     def __del__(self):
#         print("This class is deleted...")    
        

# std1 = Student("Ali",23)
# print(f" Age = {std1.age}")        

###################################################
# class FileHandler:
#     def __init__(self,fileName):
#         self.file = open(fileName,"a")
#         print(f"Your File  is created")
        
#     def write_data(self,text):
#         self.file.write(text)
        
#     def __del__(self):
#         self.file.close()
#         print(f"Your file closed..")        
        


# file1 = FileHandler("MyData.txt")
# file1.write_data("\nMy name : salam\n")
# file1.write_data("Age = 50")


################################################

class Animals:
    def speak(self):
        print(f"Animal Speak")
         
class Dog(Animals):  
    def bark(self):
        print("Dog bark...") 
        
d = Dog()
d.speak()
d.bark()


                     
        