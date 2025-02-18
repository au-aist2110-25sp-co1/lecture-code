# What is None

name = None

# if name:
if name is not None:
    print(name)

name = "Paul"

# if name:
if name is not None:
    print(name)


def are_valid_credentials(uid, pwd):
    # if uid == "b.shark" and pwd == "doo-doo":
    #     return True
    # elif uid == "m.shark" and pwd == "i-heart-baby":
    #     return True
    # else:
    #     return False

    # OR use an early return strategy
    if uid == "b.shark" and pwd == "doo-doo":
        return True
    if uid == "m.shark" and pwd == "i-heart-baby":
        return True
    return False


uid_input = input("Enter your user id: ")
pwd_input = input("Enter your password: ")

success = are_valid_credentials(uid_input, pwd_input)

print(success)

# if uid == "b.shark" and pwd == "doo-doo":
#     print("Login successful")
# elif uid == "m.shark" and pwd == "i-heart-baby":
#     print("Login successful")
# else:
#     print("Login denied")
