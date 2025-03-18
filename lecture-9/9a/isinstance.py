
s = "Paul"
t = str(10)

x = True
# if x is True:

if type(s) is str:
    print("YEP, I'm a string")
else:
    print("NOPE")

# preferred
if isinstance(s, str):
    print("YEP, I'm a string")
else:
    print("NOPE")
