# BRANCHING
# if <condition>:
#     do something

feeling_blue = True
know_where_to_go = False

# if feeling_blue and not know_where_to_go:
#     print("Puttin' on the Ritz")
# else:
#     print("Super Duper!")

# LOOPING ?

while feeling_blue and not know_where_to_go:
    print("Puttin' on the Ritz")

    resp = input("How do you feel? ")
    if resp == "good":
        feeling_blue = False

# The else block is "neat" but also not a standard construct for loops in most
# other languages
#
# else:
#     print("Super Duper!")
