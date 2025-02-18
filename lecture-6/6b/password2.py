from passfuncs import check_password, change_password

oldpass = input("Enter old password: ")

# if check_password(oldpass) != True:
if not check_password(oldpass):
    print("Password is invalid")
    exit()

newpass1 = input("Enter new password; ")

if len(newpass1) < 8:
    print("Password is too short")
    exit()

newpass2 = input("Verify new password; ")

if newpass1 != newpass2:
    print("Passwords do not match")
    exit()

change_password(oldpass, newpass1)

pass_check = input("Now check it: ")

print(check_password(pass_check))
