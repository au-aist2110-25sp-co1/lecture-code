def login():
    uid = input("Enter your user id: ")
    pwd = input("Enter your password: ")

    # OR use an early return strategy
    if uid == "b.shark" and pwd == "doo-doo":
        return uid
    if uid == "m.shark" and pwd == "i-heart-baby":
        return uid
    return None

user_id = login()

# if user_id is not None:
#     print(f"Welcome {user_id}!")
# else:
#     print("ACCESS DENIED!!")

if user_id is None:
    print("ACCESS DENIED!!")
    exit()

print(f"Welcome {user_id}!")

print()
