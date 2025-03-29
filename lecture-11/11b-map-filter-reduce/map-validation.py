sports = [
    "Baseball",
    "Basketball",
    "Cross Country",
    "Golf",
    "Softball",
    "Tennis",
    "Track & Field",
    "Volleyball",
]


# NORMALIZE both valid values (using the map pattern) and user input prior to
# validating.


def get_sport_map1():
    lower_sports = []
    for sport in sports:
        lower_sports.append(sport.lower())
    while True:
        user_val = input("Favorite AU Sport: ")
        if user_val.lower() in lower_sports:
            return user_val
        else:
            print("AU DOESN'T HAVE THAT SPORT. TRY AGAIN.")


# print("What is your favorite Augusta University varsity sport?")
# sport = get_sport_map1()
# print(f"Ah, you like {sport}. Me too!")

# More advanced ideas for normalizing values


def get_sport_map2():
    valid_sports = []
    # MAP
    for sport in sports:
        # lower case
        vsport = sport.lower()
        # remove spaces
        vsport = vsport.replace(" ", "")
        # remove "and" and "&"
        vsport = vsport.replace("&", "")
        vsport = vsport.replace("and", "")
        # remove dashes
        vsport = vsport.replace("-", "")
        valid_sports.append(vsport)
    print(valid_sports)
    while True:
        user_val = input("Favorite AU Sport: ")
        check_val = user_val.lower()
        # remove spaces
        check_val = check_val.replace(" ", "")
        # remove "and" and "&"
        check_val = check_val.replace("&", "")
        check_val = check_val.replace("and", "")
        # remove dashes
        check_val = check_val.replace("-", "")
        print(check_val)
        if check_val in valid_sports:
            return user_val
        else:
            print("AU DOESN'T HAVE THAT SPORT. TRY AGAIN.")


# print("What is your favorite Augusta University varsity sport?")
# sport = get_sport_map2()
# print(f"Ah, you like {sport}. Me too!")


def clean(val):
    # lower case
    val = val.lower()
    # remove spaces
    val = val.replace(" ", "")
    # remove "and" and "&"
    val = val.replace("&", "")
    val = val.replace("and", "")
    # remove dashes
    val = val.replace("-", "")
    return val


def get_sport_map3():
    valid_sports = []
    # MAP
    for sport in sports:
        valid_sports.append(clean(sport))
    print(valid_sports)
    while True:
        user_val = input("Favorite AU Sport: ")
        check_val = clean(user_val)
        print(check_val)
        if check_val in valid_sports:
            return user_val
        else:
            print("AU DOESN'T HAVE THAT SPORT. TRY AGAIN.")


print("What is your favorite Augusta University varsity sport?")
sport = get_sport_map2()
print(f"Ah, you like {sport}. Me too!")
