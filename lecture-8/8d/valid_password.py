SECRET_PASSWORD = "pass123"


def check_pass(user, attempts):
    cnt = 0
    while cnt < attempts:
        cnt += 1
        passwd = input(f"Enter password for {user}: ")
        if passwd == SECRET_PASSWORD:
            return True
    return False


user_name = input("Enter username: ")
valid = check_pass(user_name, 3)
if valid == True:
    print(f"Welcome {user_name}!!")
elif valid == False:
    print("Login Failed")
else:
    print("WHAAAAAATTTTT????")
