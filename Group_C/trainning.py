
import random
# Generate Random Password 

char = input("Enter Words with , between each word:")
number = input("Enter numbers  with , between each number:")
symbols = input("Enter Symbols with , between each symbol:")

list_chars = char.split(",")
list_numbers = number.split(",")
list_symbols = symbols.split(",")
# char symbols number
length_password = int(input("Enter number of passwords: "))
my_password_list = []
password = ""
for i in range(1,length_password + 1):
    char_random = random.choice(list_chars)
    number_random = random.choice(list_numbers)
    symbol_random = random.choice(list_symbols)
    password1 = f"{symbol_random}{char_random}{number_random}\n"
    password2 = f"{char_random}{symbol_random}{number_random}\n"
    password3 = f"{number_random}{char_random}{symbol_random}\n"
    with open('mylist.txt','a') as f :
        f.writelines(password1)
        f.writelines(password2)
        f.writelines(password3)

