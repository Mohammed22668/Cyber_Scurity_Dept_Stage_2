import random
# def greet(name1):
#     print(f"Hello {name1}")



# #name = input("Enter name: ")
    
# greet("ali") 
# greet("ahmed")    

# greet("mustafa")    

###################################
# def square(num):
    
#     return num*num  


# def is_even(num):
#     if num %2==0 :
#         return True
#     else :
#         return False
    
# age = int(input("Enter naumber: "))   
# num1 = square(age)   
# result = is_even(age)


# print(f"Square {age} = {num1}")

# if result :
#     print("Even")
# else :
#     print("Odd")    

######################################
list1 = [1,2,4,6,8,10,16,21,23,45,65,76,2]

def list_length(list2):
    count=0
    for i in list2:
        count +=1
    
    print(f"Length List = {count}")    
########################

# def is_duplicated(list2,x=10):
#     count = 0
#     for i in list2:
#         if i == x :
#             count +=1
    
#     return count        
        
# num1 = 20
# list_length(list1)    
# result_count = is_duplicated(list1,num1)
# print(f"{num1} found {result_count} times in list 1")

#############################################



# Capital 1 , small 1 , Symbol 1 , capital2 ,small 2 , symbol 2

def generate_pass() : 
    list_capital = ["A", "B" , "C", "D", "E", "F"]
    list_small = ["a","b","c" , "d", "e" , "f"]
    list_numbers = [1,2,3,4,5,6,7,8,9,0]
    list_symbols = ["!","@","#","$","&"]
    password = ""
    for i in range(1,5):
        capital_letter = random.choice(list_capital)
        small_letter = random.choice(list_small)
        symbol_letter = random.choice(list_symbols)
        number = random.choice(list_numbers)
        password += f"{capital_letter}{small_letter}{symbol_letter}{number}"
    
    print(f"Password = {password}")
    

generate_pass()
    
    
###########################################
# Write function to check input password is strong or accepted or weak 
# password strong should contain "Capital small symbol numbers" 
# If password is weak => Genrate a new strong password    
    
    