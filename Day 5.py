#  TODO : Easy Level
import random

letters = ['a','b','c','d' ,'e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['0','1', '2','3 ','4','5','6','7','8','9']
symbols = ['!','@','#','$','%','^','&','*','(',')','_','+','=','-','?','>','>','|']

print("Welcome to hte Python Password Generator!")

nr_letters = int(input("How many letters would you want in your password? \n"))
nr_numbers = int(input("How many numbers would you want in your password? \n"))
nr_symbols = int(input("How many symbols you want in your password? \n"))


password = ""

for char in range(0 , nr_letters):
    password += random.choice(letters)
for char in range(0, nr_numbers):
    password += random.choice(numbers)
for char in range(0, nr_symbols):
    password += random.choice(symbols)


print(password)


