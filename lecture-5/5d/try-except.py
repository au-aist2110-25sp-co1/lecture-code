# Exception handling

#   You can use if to ACTIVELY PREVENT potential errors.
#   But sometimes you errors "just happen".
#   You can use exception handling to PASSIVELY RESPOND to errors.

# ACTIVE PREVENTION
# if / else

num1 = 5
num2 = 2
# num2 = "two"

# if num2 != 0 and type(num2) != str:
if num2 != 0:
    ans = num1 / num2
    print(f"if: {num1} / {num2} = {ans}")
else:
    print("if: can't divide by zero")


# PASSIVE HANDLING
# try / except

# num1 = 5
# num2 = 0
# ans = num1 / num2
# print(f"i blowed up before I gots here: {num1} / {num2} = {ans}")

## try blocks attempt to run code sequentially WITHOUT branching
## but will immediately branch off to the except block in the case
## of an error.

num1 = 7
num2 = 2

try:
    answer = num1 / num2
    print(f"try: {num1} / {num2} = {answer}")
except:
    print("try: an error occurred")

## This next line DEPENDS ON answer which is in the try block.
## So if an exception occurs in teh answer = num1 / num2 line,
## this will also raise an (unhandled) error.

# print(f"try: {num1} / {num2} = {answer}")
