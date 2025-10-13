# Functions 

# def greet(name):
#     print(f"Hello {name}!")
    
# name1 = input("Enter name: ")    
# greet(name1)    

#########################
# def is_even(num1):
#     if num1 %2==0 :
#         return True
#     else : 
#         return False
    

# num = int(input("Enter number: "))    
# result = is_even(num)

# print(f"Result : {result}")

####################################
# list1 = [1,2,3,4,5,6,"A","B","C", ["O",1,10], True , False]


# def count_list(list2):
#     count = 0
#     for i in list2:
#         count += 1
#     return count


# result = count_list(list1)  

# print(f"Length of list = {result}")  

###########################################
# list1 = [1,2,3,4,5,6,"A","B","C", ["O",1,10], True , False,3,4,5]
# def is_duplicated(list1,x=5):
#     count = 0
#     for i in list1:
#         if i == x :
#             count +=1 
#     return count , x


# #num = int(input("Enter number: "))
# result_count , num2 = is_duplicated(list1,10)  

# print(f" {num2} is found in list {result_count} times ")      

##########################################################
# list1 = [1,2,3,4,5,6,"A","B","C", ["O",1,10], True , False,3,4,5]

# def find_value(list1,y):
#     if y in list1:
#         list1.remove(y)
#         list1.append(y)
#     else : 
#         list1.append(y)
#     return list1

# x = input("Enter value: ")
# list2 = find_value(list1,x)
# print(f"List ==> {list2}")        

##############################################
import random

def generate_pass(length=8):
    capital_letter = ["A","B","C","D","E","F"]
    small_letter = ["a","b","c","d","e","f"]
    symbol_letter = ["@","!","#","$","&","%"]
    numbers = [1,2,3,4,5,6,7,8,9,0]
    password = ""
    for i in range(1,length+1):
        random_capital = random.choice(capital_letter)
        random_small = random.choice(small_letter)
        random_symbol = random.choice(symbol_letter)
        random_number = random.choice(numbers)
        password += f"{random_capital}{random_small}{random_symbol}{random_number}"
        
    return password    
    
leng = int(input("Entet length of password: "))    
passord1 = generate_pass(leng) 
print(f"Password = {passord1}")   

###################################################


# Quiz 2 : Group B
# Create a function to check the password has been stolen before from API 


#############################################

# عملي 

