# exercise based on f strings and math operations

age = input("What is your current age?")

# todo maths, str needs to be converted to int
age_as_int = int(age)

#calc number of years left
years_remaining = 90 - age_as_int
#calc days reminaing
days_remaining = years_remaining * 365
#calc weeks remaining
weeks_remaining = years_remaining * 52
#calc months remaining
months_remaining = years_remaining * 12

# make use of f strings
message = f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months remaining"
print(message)