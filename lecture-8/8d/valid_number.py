# try:
#     val_str = input("Enter a number: ")
#     val = int(val_str)
# except:
#     print("INVALID NUMBER")
#     exit()

while True:
    try:
        val = int(input("Enter a number: "))
    except:
        print("INVALID NUMBER")
        continue
    break

square = val * val
print(f"{val} squared is {square}")
