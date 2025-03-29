# compound boolean expressions
#   e.g., input a value that is NOT one of the following:
#       "baseball"
#       "basketball"
#       "cross country"
#       "golf"
#       "softball"
#       "tennis"
#       "track & field"
#       "volleyball"
def get_other_sport():
    while True:
        user_val = input("New AU Sport: ")
        if (
            user_val != "baseball"
            and user_val != "basketball"
            and user_val != "cross country"
            and user_val != "golf"
            and user_val != "softball"
            and user_val != "tennis"
            and user_val != "track & field"
            and user_val != "volleyball"
        ):
            return user_val
        else:
            print("AU ALREADY HAS THAT SPORT. TRY AGAIN.")


# print("What is sport you want Augusta University to add?")
# sport = get_other_sport()
# print(f"Ah, you like {sport}. Me too!")


def get_other_sport_in():
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
        user_val = input("New AU Sport: ").lower()
        # if not user_val in sports:
        if user_val not in sports:
            return user_val
        else:
            print("AU ALREADY HAS THAT SPORT. TRY AGAIN.")


print("What is sport you want Augusta University to add?")
sport = get_other_sport_in()
print(f"Ah, you like {sport}. Me too!")
