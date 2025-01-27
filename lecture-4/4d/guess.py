# You're thinking of a number...it's 42
# Ask the user to guess the number between 1 and 100
# Tell them if they guessed too high, too low, or if they got it right.

# Alphabetical comparisons (strings)
# "3000"
# "4"
# "41"
# "42"
# "5"

# Numerical comparisons (ints, floats, etc.)
# 4
# 5
# 41
# 42
# 3000

mynum = 42

usernum = int( input("Enter a number from 1 to 100: ") )

if usernum < 1 or usernum > 100:
    print("!!! INVALID NUMBER !!!")
elif usernum > mynum:
    print("Too high!!")
elif usernum < mynum:
    print("Too low!!")
# elif usernum == mynum:
else:
    print("YOU GUESSED IT!!!")
