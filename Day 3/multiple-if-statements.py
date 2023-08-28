# example of if/elif/else
# if condition1:
#     do A
# elif condition2:
#     do B
# else:
#     dp C

# multiple if
# if condition1:
#     do A
# if condition 2:
#     do B
# if condition3:
#     do C


print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

bill = 0

# Checking age and payment
if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age?"))
    if age < 12:
        bill = 5
        print("Child tickets are R5. ")
    elif age <= 18:
        bill = 7
        print("Youth tickets are R7. ")
    else:
        bill = 12
        print("Adult tickets are R12. ")
        
    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        # Add R3 to their bill
        bill += 3
    
    print(f"Your final bill is {bill}")
    
else:
    print("Sorry, you have to grow taller before you can ride.")