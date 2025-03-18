# A string is a SEQUENCE
# A list is a SEQUENCE

# So what's the difference??

# DECLARATION

name = "Jamal"
name_list = ["J", "a", "m", "a", "l"]
empty_list = []

# ELEMENT TYPES

oregon_temps = [45.1, 48.2, 52.8, 58.9, 65.3, 72.4, 78.2, 77.1, 71.2, 60.3, 50.8, 45.5]
maine_temps = [29.8, 32.6, 41.2, 52.0, 63.2, 72.1, 77.6, 76.4, 67.5, 55.0, 45.2, 33.8]

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

# MUTABLE vs IMMUTABLE (a rabbit hole)

name = "Paul"  # NOT changing "Jamal" to "Paul"...creating a new
# string and changing the thing that name is referencing

name = "Jamal"
name[4]  # 'l'
name[4] = "r"  # ERROR ERROR ERROR!!!!!

name_list[4]  # ALSO 'l'
name_list[4] = "r"  # SURE, NO PROB!!
name_list  # ['J', 'a', 'm', 'a', 'r']

# IN SUMMARY

# a list is a GENERIC, MUTABLE SEQUENCE
# s string is a SPECIALIZED, IMMUTABLE SEQUENCE
