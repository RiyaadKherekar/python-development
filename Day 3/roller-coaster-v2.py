# Nested if statements and elif statements

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        print("Please pay R5.")
    elif age <= 18:
      print("Please pay R7.")
    elif age < 30:
      print("Please pay R12.")
    else:
      print("Please pay R12.")
else:
    print("Sorry, you have to grow taller before you can ride.")