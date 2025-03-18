
# TYPE HINTS: Just say what type you SHOULD expect the variable to be.
i: int = None

user_input = input("what is your name: ")
print(type(i))
i = str(user_input)
print(type(i))
i = 12
print(type(i))

def is_leap_year(year: int) -> bool:
    ...
