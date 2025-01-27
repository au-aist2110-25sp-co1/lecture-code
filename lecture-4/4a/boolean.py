# Boolean   type is `bool``
#   True    (yes)
#   False   (no)

print(type(True))   # bool

# Comparison operators
#  does x = 5? (these don't work)
#  does 5 = x? (`=` used for variable ASSIGNMENT)
# 
# ==    equal
# !=    not equal
# >     greater than
# <=    less than or equal to
# <     less than
# >=    greater than or equal to

x = 4
ans = x > 5

print(ans)      # False

x = 6
ans = x > 5
print(ans)      # True

print(x > 5)    # True

# COMPOUND CONDITIONS with and / or

print( 7 > 5 and 3 < 5 )    # True and True >>>> True
print( 7 > 5 and 8 < 3 )    # True and False >>> False
print( True and False )     # False (really the same as above)
print( False and True )     # False
print( False and False )    # False
print( True or True )       # True
print( True or False )      # True
print( False or True )      # True
print( False or False )     # False

###############################################################################
# TRUTH TABLES
###############################################################################

###############################################################################
# AND
#  BOTH sides must be True for the compound condition to be True.
###############################################################################

# |  AND  | TRUE  | FALSE |
# |-------|-------|-------|
# | TRUE  | True  | False |
# | FALSE | False | False |

###############################################################################
# OR
#  EITHER (or BOTH) must be True for the compound condition to be True.
###############################################################################

# |  OR   | TRUE  | FALSE |
# |-------|-------|-------|
# | TRUE  | True  | True  |
# | FALSE | True  | False |

###############################################################################
# not (NEGATION)
###############################################################################
x = 5
print(x == 5)
print(x != 5)
print(not x == 5)


###############################################################################
# PARENTHETICAL PRECEDENCE
#  Use parentheses to group together expressions to compose complicated
#  compound expressions.
###############################################################################

gender = "male"
risk = "high"
last_check = 6

have_exam = gender == "male" and ( (risk == "low" and last_check > 10) or (risk == "high" and last_check > 5) )

does_not_need_exam = not have_exam

# convert bool to str to concatenate
print("Needs Exam: " + str(have_exam))  
print("Doesn't need exam: " + str(does_not_need_exam))
