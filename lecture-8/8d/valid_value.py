# color = input("What is your favorite color? ")
# if not (color == "red" or color == "blue" or color == "green"):
#     print("INVALID COLOR")
#     exit()

# while True:
#     color = input("What is your favorite color? ")
#     if not (color == "red" or color == "blue" or color == "green"):
#         print("INVALID COLOR")
#         continue
#     else:
#         break


while True:
    color = input("What is your favorite color? ")
    if color == "red" or color == "blue" or color == "green":
        break
    print("INVALID COLOR")

print(f"I love {color}, too!!!")
