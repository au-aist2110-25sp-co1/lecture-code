print('Welcome to "21 and Over Gets you Drunk"')

age = int(input("How old are you? Be honest!!: "))

###############################################################################
# TWO MUTUALLY EXCLUSIVE BRANCHES
###############################################################################

###############################################################################
# OPTION 1 (separate if's)
# 
# You can do two "opposite" if statements, but it is inefficient and
# error-prone.
###############################################################################

# if age >= 21:
#     print("I see you are over 21")
#     print("okay, come on in")

# if not age >= 21:
#     print("You gotta go!!")


###############################################################################
# OPTION 2 (if / else)
# 
# if / else is a much easier / better choice when there are just two branches.
###############################################################################

# if age >= 21:
#     print("I see you are over 21")
#     print("okay, come on in")
# else:               # OTHERWISE
#     print("You gotta go!!")

###############################################################################
# MORE THAN TWO MUTUALLY EXCLUSIVE BRANCHES
###############################################################################

###############################################################################
# OPTION 1 (separate if's)
# 
# No real logical problem with multiple if statments, but be careful as this is
# quite error prone and very difficult to manage.
###############################################################################

# if age >= 21:
#     print("I see you are over 21")
#     print("okay, come on in and get drunk")
# if age >= 18 and age < 21:
#     print("I see you are over 18")
#     print("okay, come on in and party, but no drinkin'")
# if not age >= 18:
#     print("You gotta go!!")


###############################################################################
# NOT AND OPTION (if + if / elif)
# 
# Be VERY careful with code like this. You have two separate if statements. The
# else will run even if the first if condition is True.
###############################################################################

# if age >= 21:
#     print("I see you are over 21")
#     print("okay, come on in and get drunk")
# if age >= 18 and age < 21:
#     print("I see you are over 18")
#     print("okay, come on in and party, but no drinkin'")
# else:
#     print("You gotta go!!")

###############################################################################
# OPTION 2 (if / elif / else)
# 
# This is the way.
###############################################################################

if age >= 21:
    print("I see you are over 21")
    print("okay, come on in and get drunk")
elif age >= 18:                # ELSE IF
    print("I see you are over 18")
    print("okay, come on in and party, but no drinkin'")
else:
    print("You gotta go!!")


print("Have a nice day!!")
