

# class Student:
#     def __init__(self,name,age):
#         self.name = name 
#         self.age = age
#         print("Your Class Created...")
        
#     def generate_email(self):
#         print(f"{self.name}@gmail.com")    
        
#     def __del__(self):
#         print("Class Is Closed...")    
        
        
# std1 = Student("Ali",34)
# std1.generate_email()        


############################################
# W = Write , r = Read  , a = Append 

# class FileHandler:
#     def __init__(self,fileName):
#         self.file = open(fileName,"a")
#         print(f"File is Created...")
    
#     def write_data(self,data):
#         self.file.write(data)
        
#     # def read_file(self):
#     #     print(f"File => \n{self.file.read()}")
            
    
#     def __del__(self):
#         self.file.close()    



# file1 = FileHandler("Cyber_A.txt")
# file1.write_data("This is Cyber Security Class A\n")
# file1.write_data("Second Class A\n")

                
                
####################################################    

# class A     10 models
# class B     3 models 

class Animals:
    def sound(self,x):
        print(f"Your Animals has sound {x}") 
        
class Dog(Animals):
    def bark(self):
        print(f"Dog is Bark now ...")        
        
        
doc1 = Dog()
doc1.bark()  
doc1.sound("X1")    


an1 = Animals()
an1.bark()