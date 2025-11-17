# class Car:
#     def __init__(self,brand,color,model,engine,price,speed):
#         self.brand = brand
#         self.color = color
#         self.model = model
#         self.engine = engine
#         self.price = price
#         self.speed = speed
        
#     def get_color(self):
#         print(f"Car {self.brand} has color {self.color}")
        
#     def get_speed(self):
#         print(f"Speed is {self.speed}")
        
#     def set_price(self,new_price):
#         self.price += new_price
        
#     def set_speed(self,new_speed):
#         self.speed = new_speed    
        
#     def car_info(self):
#         print(f"Brand: {self.brand}") 
#         print(f"Color: {self.color}")
#         print(f"Model: {self.model}")
#         print(f"Engine: {self.engine}")    
#         print(f"Price: {self.price}")
#         print(f"Speed: {self.speed}")  

# a = 10 
# b =20 
# # c = a 
# # a = b 
# # b = c 

# a,b = b , a 


# def str1(a):
#     return a[::-1]

import random
###################################################
mylist = [1,2,3,4,5,6,7,8]
mylist2 = ["a","b","c","d"]
with open("mylist.txt","a") as file:
    for i in mylist:
        file.write(f"{str(i)} {random.choice(mylist2)} \n")
        