

# class Student:
#     def __init__(self,name,stage):
#         self.name = name 
#         self.stage = stage
#         print(f"welcome {self.name} Your class has been created")
        
#     def generate_email(self):
#         print(f"{self.name}@gmail.com")
    
#     def __del__(self):
#         print(f"Your Memory has been cleaned...")        
        
        
# std1 = Student("Ali",44) 
# std1.generate_email()       

##########################################
class FileHandler:
    def __init__(self,fileName):
        self.file = open(fileName,"a")
        
    def write_data(self,data):
        self.file.write(data)
        
    def __del__(self):
        self.file.close()    
        
        
f1 = FileHandler("Cyber_Group_B.txt")   
f1.write_data("\nWlecome Cyber Class\n")     
        