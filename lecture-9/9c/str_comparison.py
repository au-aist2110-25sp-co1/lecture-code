# Exactly equal
s1 = "World Series"
s2 = "world series"

print(s1 == s2)

# Case Insensitive comparison

print(s1.upper() == s2.upper())
print(s1.lower() == s2.lower())
print(s1.casefold() == s2.casefold())

# input sanitization

password = "pass123"
user_input = input("enter password: ")
# user_input = user_input.strip()
# user_input = user_input.lower()
# user_input = input("enter password: ").strip().lower()
if (user_input.strip().lower() == password):
    print("come in")
else:
    print('go away')



# "Contains"

val = "The quick brown fox"

print("fox" in val)
print("quick" in val)
print("the" in val.lower())
