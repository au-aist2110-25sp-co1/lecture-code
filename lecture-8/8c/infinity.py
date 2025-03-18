feeling_blue = True
know_where_to_go = False

# while feeling_blue or not know_where_to_go:
#     print("Puttin' on the Ritz")

#     resp = input("How do you feel? ")
#     if resp == "good":
#         feeling_blue = False
#     else:
#         continue  # looping keyword

#     resp = input("Do you know where to go? ")
#     if resp == "yes":
#         know_where_to_go = True
#     else:
#         continue  # looping keyword

# Intentional INFINITE LOOPS

while True:
    print("Puttin' on the Ritz")

    resp = input("How do you feel? ")
    if resp == "good":
        break

    resp = input("Do you know where to go? ")
    if resp == "yes":
        break

print("All Done! Super goodDuper!")
