# Beer-thirty is Friday afternoon at 5:30 PM.
# Ask the user for the day of the week.
# Ask the user for the time.
# Ask the user for AM or PM.
# If it's beer thirty, then celebrate.
# Otherwise if it's Friday AFTER beer thirty, then you panic.
# Otherwise, you wish it it was beer thirty.

day = input("Enter day of week: ")
time = input("Enter the time: ")
ampm = input("Enter AM or PM: ")

if day == "Friday" and time == "5:30" and ampm == "PM":
    print("Woot! It's beer-thirty. Let's grab a cold one!!")
elif day == "Friday" and time > "5:30" and ampm == "PM":
    # Yeah this ALMOST works, but after 9:59 time is NOT > "5:30"
    print("Oh no!!! I missed beer-tirty!!!! :( :( :(")
else:
    print("Darn. It's not beer-thirty yet!! Get here already!")
