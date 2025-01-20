# INPUT
# PROCESS
# OUTPUT

value_1 = input()
print(value_1)
print(type(value_1))

# input() ALWAYS returns a str

# input() takes an argument that is a prompt for the user.

value_2 = input("Enter a cool value: ")
print(value_2)
print(type(value_2))

age = input("Enter your age: ")
age_int = int(age)
print(age_int)
print(type(age_int))

price = input("Enter price of tea in China: ")
price_with_decimals = float(price)
print(price_with_decimals)
print(type(price_with_decimals))
