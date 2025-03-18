months = [
    "jan",
    "feb",
    "mar",
    "apr",
    "may",
    "jun",
    "jul",
    "aug",
    "sep",
    "oct",
    "nov",
    "dec",
]
name = "Jamal"
name_list = ["J", "a", "m", "a", "l"]
sent = "The quick brown fox jumps over the lazy dog"
para = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor
incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis
nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu
fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in
culpa qui officia deserunt mollit anim id est laborum.
"""

# Turning Strings INTO Lists

# list constructor
list(name)
name_list
list(sent)

# str.split()

"a,b,c".split(",")
print(sent)
# words = sent.split(' ')
words = sent.split()
print(words)

lines = para.strip().splitlines()
print(lines)

# Turning Lists INTO Strings
# str.join()

new_name = "".join(name_list)
print(new_name)

mstr = ", ".join(months)
print(months)
print(mstr)

mlstr = "\n".join(months)
print(mlstr)
