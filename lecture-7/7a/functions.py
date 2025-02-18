from random import randint, random

# if/elif/else breaks out of linear code flow conditionally

# val = randint(1,10)
# if val <= 5:
#     print("I'm little... :(")
# else:
#     print("I'm big!! :)")




# But functions are UNCONDITIONAL branching

pass      # I DO NOTHING!!!

# def jump():
#     print("!!! JUMP !!!")
#     return

# print("...walk...")
# print("...walk...")
# jump()
# print("...walk...")
# jump()
# jump()
# print("...walk...")


# Execute and return
#   return (nothing)
#   return something
#   implied return


def print_random_int_1_20():
    num = randint(1,20)
    print(f"Your number is {num}")
    # return is implied because code falls off of the end of the block

# print_random_int_1_20()
# print_random_int_1_20()
# print_random_int_1_20()


def get_random_float_0_100():
    num = random()      # between 0 and 1
    num = num * 100     # between 0 and 100
    num = round(num, 4) # round to 4 decimal places
    return num

# num1 = get_random_float_0_100()
# num2 = get_random_float_0_100()
# num3 = get_random_float_0_100()
# prod = num1 * num2 * num3
# print(prod)

# functions are SO much better with parameters!!!
def get_random_float(upper_bound):
    num = random()          # between 0 and 1
    num = num * upper_bound # between 0 and upper_bount
    num = round(num, 4)     # round to 4 decimal places
    return num

print(get_random_float(50))
print(get_random_float(50000))
