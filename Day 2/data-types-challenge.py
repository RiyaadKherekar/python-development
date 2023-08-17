# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

# print(type(two_digit_number))
# returns output as a <class 'str'>
# print("hello"[0])
first_digit = two_digit_number[0]
second_digit = two_digit_number[1]

print(first_digit)
print(second_digit)

result = int(first_digit) + int(second_digit)
print(result)
# print the type
print(type(result))