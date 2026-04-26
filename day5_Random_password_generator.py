import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
           'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("welcome to the pypaswword generator")
num_letters = int(input("how many letters do you want in your password?|\n"))
num_symbols = int(input("how many symbols do you want in your password?|\n"))
num_numbers = int(input("how many numbers do you want in your password?|\n"))
# Easy level 
password = ""
for char in range(0, num_letters):
    password +=  random.choice(letters)
    
for char in range(0, num_symbols):
    password +=  random.choice(symbols)

for char in range(0, num_numbers):
    password +=  random.choice(numbers)

print(f"Your generated password is: {password}")
# Hard level
password_list = []
for char in range(0, num_letters):
    password_list.append(random.choice(letters))

for char in range(0, num_symbols):
    password_list.append(random.choice(symbols))

for char in range(0, num_numbers):
    password_list.append(random.choice(numbers))
random.shuffle(password_list)
# we can use for loop to convert the list to string
password = ""   
for char in password_list:
    password += char        
print(f"Your generated password is: {password}")
