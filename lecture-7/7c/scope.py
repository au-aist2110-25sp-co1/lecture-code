# Types of "variables" and variable "scope"

# num1 & num2 are parameters (pretty much like variables with function scope)
def prod(num1, num2):
    # BAD!!! DO NOT CHANGE module-level variables in functions
    # global random_value  # declaring that I want to change the value of this varble
    
    # val is a variable with function scope
    val = num1 * num2
    val = round(val, 2)

    # NOT GOOD!!! Though less of a cardinal sin, you should not even access the
    # value of module-level variables inside of functions. If a function needs
    # access to the value of a module-level varialbe, it should define a
    # parameter for it and it should be passed in.
    new_value = random_value + 5
    print(new_value)
    
    # BAD!!! DO NOT CHANGE module-level variables in functions
    # random_value = random_value + 10

    return val

# variable with module scope, accessible in lower-levels of the module
random_value = 5
# result1 is a variable with module scope
result1 = prod(1.1, 2.2222)
result2 = prod(2.2, 3.333333)
result3 = prod(3.3, 4.4444)

print(result1)
print(result2)
print(result3)
print(random_value)

# DO NOT USE THE GLOBAL KEYWORD Functions are "black boxes". Unless there is
# some entirely unavoidable reason to break the rule, you should NOT change
# module-scoped variables in functions.

# Confusing, but these are NAMED the same as the function-scope parameters and
# variables, but are completely different. The fact that they are named the same
# is coincidental. And maybe shoudl be considered a bad practice since it is
# confusing ... but it is quite a common occurrence.
num1 = 5.555
num2 = 6.666667
val = prod(num1, num2)
print(val)
