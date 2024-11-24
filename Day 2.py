

print("Welcome to the My Tip Calculator!")



bill = float(input("What is your  total bill ? $"))
tip = int(input("What percentage tip would you give to the waiter? 10 , 15 ,20 $"))
people = int(input("How many people to split the bill?"))
bill_with_percent = tip / 100
total_tip_amount = bill_with_percent * bill
Total_bill = total_tip_amount + bill
print(Total_bill)





