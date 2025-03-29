# compound boolean expressions
#   e.g., input a value that is one of the following:
#       "baseball"
#       "basketball"
#       "cross country"
#       "golf"
#       "softball"
#       "tennis"
#       "track & field"
#       "volleyball"
def get_sport():
    while True:
        user_val = input("Favorite AU Sport: ")
        if (
            user_val == "baseball"
            or user_val == "basketball"
            or user_val == "cross country"
            or user_val == "golf"
            or user_val == "softball"
            or user_val == "tennis"
            or user_val == "track & field"
            or user_val == "volleyball"
        ):
            return user_val
        else:
            print("AU DOESN'T HAVE THAT SPORT. TRY AGAIN.")


# print("What is your favorite Augusta University varsity sport?")
# sport = get_sport()
# print(f"Ah, you like {sport}. Me too!")


def get_sport_in():
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
    while True:
        user_val = input("Favorite AU Sport: ")
        if user_val in sports:
            return user_val
        else:
            print("AU DOESN'T HAVE THAT SPORT. TRY AGAIN.")


print("What is your favorite Augusta University varsity sport?")
sport = get_sport_in()
print(f"Ah, you like {sport}. Me too!")
