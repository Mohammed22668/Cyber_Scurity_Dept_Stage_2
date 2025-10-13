
# Functions 

# def greet(name,age):
    
#     print(f"Hello {name} age = {age}")
    


# greet("Ahmed" , 34)   
# greet("Ali" , 60)   
# greet("mustafa" , 45)   
# greet("salam" , 20)   

############################


# def sum_numbers(num1,num2):
#     # print(f"Result = {num1+num2}")
    
#     return num1+num2
    
    

# result = sum_numbers(10,24)   


# print(f"Result = {result}")

#################################

# def even_num(num):
#     if num %2==0:
#         return True ,num
#     else :
#         return False , num
    

# num1 = int(input("Enter Number: "))  

# result , num2 = even_num(num1)

# print(f"Result {result}  ==== num2 {num2}")


#########################################

list_values = [1,2,4,5,7,9,0,15,2,4,5,6,7,8,9,5,34,"A", "B"]

def count_list(list2):
    count = 0
    for i in list2:
        count +=1
    return count    


# result_count = count_list(list1)

# print(f"Length list1 = {result_count}")

##########################
# Check any value is duplicated 

def is_duplicated(list2,x=10):
    count =0 
    for i in list2 :
        if i == x :
            count +=1
    
    print(f"Value {x} found {count} times")        
    
    
y=10    
is_duplicated(list_values,y)    


######################################


# Create a function called grade_calculator that takes a list of exam scores
# and returns average score and letter grade 
# (A:90-100 , B:80-89 , C:70-79 , D:60-69 , F:Below 60)

###########
# عملي

def calculate_area(length,width):
    area = length * width
    return area


length = int(input("Enter length: "))
width = int(input("Enter Width: "))
room_area = calculate_area(length,width)


print(f"Room area = {room_area} ")