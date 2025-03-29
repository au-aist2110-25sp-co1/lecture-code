# Out of loop variables
#  - accumulator
#  - tracker

attendees = ""
attendee_count = 0

while True:
    name = input("Enter attendee: ")
    if name != "":
        # attendees = attendees + name + "\n"
        attendees += name + " "
        attendee_count += 1
    else:
        break


print("MY COOL PARTY")
print(f"{attendee_count} people are coming")
print("THEY ARE:")
print(attendees)
