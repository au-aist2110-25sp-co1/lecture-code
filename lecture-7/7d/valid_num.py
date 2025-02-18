def get_number():
    response = input("Enter a number: ")

    try:
        num = int(response)
        return num
    except:
        return None

num1 = get_number()
# num1 = get_number("Enter num1: ")
# if num1 is None:
#     print("INVALID INPUT")
#     exit()
num2 = get_number()

if num1 is not None and num2 is not None:
    sum = num1 + num2
    print(f"The sum is {sum}")
else:
    print("INVALID INPUT")
