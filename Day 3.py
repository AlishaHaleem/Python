print("Welcome to the Python Pizza Deliveries!")
size = input("What size of pizza do you want? S, M OR L")
Pepperoni = input("Do you want pepperoni? Y or N")
cheese = input("Do you want extra cheese? Y or N")

# Billing
bill = 0
if size == "S":
    bill += 20
elif size == "M":
    bill += 35
elif size == "L":
    bill += 60
else:
    print("You typed the wrong data.")


# Pepperoni
if Pepperoni == "Y":
    if size == "S":
        bill += 4
    else:
        bill += 8

# Extra Cheese
if cheese == "Y":
    bill += 3

print(f"Your final bill is: ${bill}.")



