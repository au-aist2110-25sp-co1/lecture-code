# STATEMENT: executable line of Python code
# EXPRESSION: code that can be evaluated (i.e., code that can become a value)

age = 29
name = "Paul"

# Expressions can contain mathematical operations.
# Mathematical operations involce the use of mathematical operators.
#    + (addition)
#    - (subtraction)
#    * (multiplication)
#    / (division) FORWARD slash
#    % (modulus / remainder)

age = 29 + 5
print(age)          # 34
print(type(age))

new_age = age + 10
print(new_age)      # 44
print(type(new_age))

age = age + 10
print(age)          # 44
print(type(age))

age = age + 3.5
print(age)          # 47.5
print(type(age))

age = age + 3.5
print(age)          # 51.0
print(type(age))

age = int(age)
print(age)          # 51
print(type(age))

# Python ODDNESS: Division ALWAYS evaluates as a float

age = 50
age = age / 2
print(age)          # 25.0
print(type(age))

age = int(age)
print(age)          # 25
print(type(age))

chocolate_count = 50
recipient_count = 15

chocolates_per_recipient = int(chocolate_count / recipient_count)
leftover_chocolates = chocolate_count % recipient_count     # remainder

print(chocolates_per_recipient)
print(leftover_chocolates)



weight = "145.7"
print(float(weight))

# weight = weight - 5   # uh oh, weight is still a string so this fails
# print(weight)

weight = float(weight)
weight = weight - 5
print(weight)

first_name = "Paul"
last_name = "Revere"

# CONCATENATION: merge two (or more) string values together

print(first_name)
print(last_name)

print(first_name + last_name)   # + between strings CONCATENATES them

print(first_name + " " + last_name)
print(last_name + ", " + first_name)

# Paul Revere is 25 years old

# print(first_name + " " + last_name + " is " + age + " years old")
# # Can't concatenate int or float with str
print(first_name + " " + last_name + " is " + str(age) + " years old")

output = first_name + " " + last_name + " is " + str(age) + " years old"
print(output)

output = output + " ... BOOM!!!!"
print(output)

output = "Did you know that " + output
print(output)
