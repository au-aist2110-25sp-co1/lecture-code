# Text following a hashtag are comments.
# Comments are IGNORED by the Python interpreter.
# Comments can be at the beginning of a line or following actual code.

# Literal values
# -------

# NUMBERS

# int (Integer -- counting number w/ no decimals)
# 3
# 1,000,000 (NOPE...no commas)

# float (Floating point numbers -- numbers with decimals)
# 17.62

# In interactive (REPL) mode, typing these in will result in the value being
# echoed back to the screen.

3               # 3
type(3)         # <class 'int'>
17.62           # 17.62
type(17.62)     # <class 'int'>

# Above, type() is a "built-in function". It inspects a value and tells you the
# data type of that value.

# Need to use print() inside of scripts to display output. print is another of
# the core "built-in functions". It simply echoes a value to the screen.

print(3)
print(type(3))      # functions can be nested.
print(17.62)
print(type(17.62))

# TEXT

# str (String -- any text, including numbers)
# "Paul Revere"
# 'Ben Franklin'
# `George Washington` (NOPE backtick is not a viable option)

"Paul Revere"
print("Paul Revere")
print(type("Paul Revere"))  # <class 'str'>
print(type('Ben Franklin')) # <class 'str'>
print(type('3'))            # <class 'str'>
