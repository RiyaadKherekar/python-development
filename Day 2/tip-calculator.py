#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

# Collect data from user
print("Welcome to your tip calculator")
bill = float(input("What was the bill? R"))
# print(bill)
tip = int(input("What tip percentage would you like to give? 5, 10, 15, 20? "))
# print(tip)
people = int(input("How many people needs to split the bill? "))

# Calculate bill with tip / people

# bill_with_tip = tip / 100 * bill + bill
# print(bill_with_tip)
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people 
final_amount = round(bill_per_person, 2)
final_amount = "{:.2f}".format(bill_per_person)

print(f"Each person should pay R{final_amount} ")