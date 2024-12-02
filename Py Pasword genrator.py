import random
# TODO : Hard Level
letter = ['a','b','c','d' ,'e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
number = ['0','1', '2','3 ','4','5','6','7','8','9']
symbol = ['!','@','#','$','%','^','&','*','(',')','_','+','=','-','?','>','>','|']

print("Welcome to hte Python Password Generator!")

anr_letters = int(input("How many letters would you want in your password? \n"))
anr_numbers = int(input("How many numbers would you want in your password? \n"))
anr_symbols = int(input("How many symbols you want in your password? \n"))

password_list = []
for char in range(0 , anr_letters):
    password_list.append(random.choice(letter))
for char in range(0, anr_numbers):
    password_list.append(random.choice(number))
for char in range(0, anr_symbols):
    password_list.append(random.choice(symbol))

print(password_list)
random.shuffle(password_list)
print(password_list)
password = ""
for char in password_list:
    password+= char
print(f"Your password is :{password_list}")