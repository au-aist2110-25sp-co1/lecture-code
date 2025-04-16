duck_colors = {"huey": "red", "dewey": "blue", "louie": "green"}

# print(duck_colors.keys())
# print(duck_colors.values())
# print(duck_colors.items())

for duck in duck_colors:
    color = duck_colors[duck]
    print(f"{duck} is {color}")

for color in duck_colors.values():
    print(color)

for item in duck_colors.items():
    print(f"{item}")


for item in duck_colors.items():
    duck = item[0]
    color = item[1]
    print(f"{duck} is {color}")

for duck, color in duck_colors.items():
    print(f"{duck} is {color}")
