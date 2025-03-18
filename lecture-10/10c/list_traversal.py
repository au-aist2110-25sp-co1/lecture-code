months = [
    "jan",
    "feb",
    "mar",
    "apr",
    "may",
    "jun",
    "jul",
    "aug",
    "sep",
    "oct",
    "nov",
    "dec",
]

# Counter Controlled
# index = 0
# while index < len(months):
#     mon = months[index]
#     print(mon)
#     index += 1

# for / in
# for mon in months:
#     print(mon)

# for in range()

# for index in range(10):
for index in range(len(months)):
    mon = months[index]
    print(f"{index+1}:\t{mon}")
