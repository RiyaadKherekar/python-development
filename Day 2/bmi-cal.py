# user input
height = input("enter your height in m: ")
weight = input ("enter your weight in kg: ")

# using the exponent operator 
bmi = int(weight) / float(height) ** 2
# or using multiplocation and PEMDAS
bmi_as_int = int(bmi)
print(bmi_as_int)