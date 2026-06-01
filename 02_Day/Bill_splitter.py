print("Welcome to the Tip Calculator!")

total_bill = input("What was the total bill?\n")

tip = input("How much tip would you like to give? 10, 12, or 15 %?\n")

people_to_split = input("How many people will split the bill?\n")

total_bill_with_tip = float(total_bill) + ((float(tip)/100) * float(total_bill))

bill_split = total_bill_with_tip / int(people_to_split)

final_bill = round(bill_split, 2) # this is float

print(f"Each person should pay: $ {round(final_bill):.2f}") #this is string