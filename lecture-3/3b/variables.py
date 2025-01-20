# Variables
# NAMED pockets of memory that store values that can change over time.

# + Variable names should be meaningful
# + Variable names can contain only letters, numbers, and _'s
# + Variable names can't start with a number
# + Variable names are case sensitive

# age
# Age
# aGE

# Variables must be ASSIGNED values.


# ASSIGNMENT uses the ASSIGNMENT OPERATOR.
#  (operator is simply a symbol that has meaning)
#  Assignment operator is =
#   (get's the value of)

# A line of valid Python code is called a STATEMENT

age = 13

# 13 = age   NOPE variable name is ALWAYS TO THE LEFT of the value

# Variables are either ASSIGNED TO or REFERENCED.
# Referencing is getting the value of the variable.

print(13)
print(age)
print(type(age))

# Code is executed sequentially. Values change over time, but only after the
# (re)assignment line has been executed.

age = 15
print(age)
print(type(age))

# Variables must be ASSIGNED before they can be REFERENCED.

# print(name)
# name = "Paul Revere"   NOPE name needs to be set (assigned) first

name = "Paul Revere"
print(name)
print(type(name))

name = 1775
print(name)
print(type(name))

# Python is DYNAMICALLY TYPED.
# As opposed to STATICALLY TYPE, like C#, C++, C, Java, Rust.

weight: float = 0.0
weight = 172.3
print(weight)
print(type(weight))

weight = "Skinny"
print(weight)
print(type(weight))


# location = "unknown"
location = None          # aka Null

# var location;         DECLARING in JavaScript
# String location;      DECLARING in C# or Java

# Variables must be ASSIGNED before they can be REFERENCED.
# Partly false. ACTUALLY it must be DECLARED before it can be referenced.

print(location)
print(type(location))

