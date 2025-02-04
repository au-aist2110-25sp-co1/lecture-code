###########################################################
# Basic string choice validation

## Option 1
print("Do you like Chocolate, Vanilla, or Strawberry?")
choice = input("Enter c, v, or s: ")
if choice != "c" and choice != "v" and choice != "s":
    print("INVALID CHOICE")
    exit()

## Option 2
print("Do you like Chocolate, Vanilla, or Strawberry?")
choice = input("Do you like Chocolate, Vanilla, or Strawberry? Enter c, v, or s: ")
if not (choice == "c" or choice == "v" or choice == "s"):
    print("INVALID CHOICE")
    exit()

# BE CAREFUL -- DO NOT DO THIS
# if not (choice == "c" or "v" or "s"):


###########################################################
# Basic "is a number" validation

# Option 1
year_str = input("What year is it? ")
try:
    year = int(year_str)
except:
    print("INVALID INPUT")
    exit()

# Option 2
try:
    year = int(input("What year is it? "))
except:
    print("INVALID INPUT")
    exit()


###########################################################
# Basic range check (year from 2020 to 2099)

# Option 1
if year < 2020 or year >= 2100:
    print("INVALID YEAR")
    exit()

# Option 2
if not (year >= 2020 and year < 2100):
    print("INVALID YEAR")
    exit()

# Option 3
# if not (2020 <= year and year < 2100):
if not (2020 <= year < 2100):
    print("INVALID YEAR")
    exit()
