sports = [
    "baseball",
    "basketball",
    "cross country",
    "golf",
    "softball",
    "tennis",
    "track & field",
    "volleyball",
]

all_sports = ", ".join(sports)
print(all_sports)

# BASIC STRING ACCUMULATOR PATTERN

all_sports = ""
for sport in sports:
    all_sports = all_sports + sport + ", "
print(all_sports)

# Replicate .join() by slicing the list

all_sports = ""
for sport in sports[0:-1]:
    all_sports = all_sports + sport + ", "
all_sports = all_sports + sports[-1]
print(all_sports)


# Can also use += for strings

all_sports = ""
for sport in sports[0:-1]:
    all_sports += sport + ", "
all_sports += sports[-1]
print(all_sports)

# VARIATIONS (FILTER AND/OR MAP)

# FILTER
all_sports = ""
for sport in sports:
    if " " not in sport:
        all_sports = all_sports + sport + ", "
print(all_sports)


# MAP
all_sports = ""
for sport in sports:
    sport = sport.title()
    sport = sport.replace("&", "and")
    all_sports += sport + ", "


print(all_sports)

# Replicate .join() by slicing the resulting string
all_sports = all_sports[0:-2]
print(all_sports)
