# "truthiness"

# if EXPRESSION:
#  usually EXPRESSION is boolean.


name = None         # no value assigned

# if name is None:
# None is Falsey
# Not None is Truthy
if name:
    print("name is " + name)
else:
    print("name is unassigned")

name = "Paul"
# A non-empty string is Truthy
# if name != "":
if name:
    print("name is " + name)
else:
    print("name is unassigned")

name = ""      # This is NOT None
# An empty string is Falsey
# if name == "":
if name:
    print("name is " + name)
else:
    print("name is unassigned")


age = 20
# Not 0 is Truthy
if age:
    print("age is " + str(age))
else:
    print("age must be 0")

age = 0
# 0 is Falsey
if age:
    print("age is " + str(age))
else:
    print("age must be 0")


# "short-circuits"

# When two boolean expressions are strung together with an and
# the left is evaluated first and will immediately stop evaluationg
# if it is False (or Falsey)

num1 = 7
num2 = 0
if num2 > 0 and num1 / num2 > 3:
    print("good ratio!")
else:
    print("bad ratio")
