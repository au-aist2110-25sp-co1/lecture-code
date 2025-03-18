# MUTATION METHODS
#
# .append()     Add element at end
# .insert()     Add element after index
# .extend()     Add many elements
# .clear()      Remove all elements
# .remove()     Remove one element
# .pop()        Remove element at position

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

months.append("bob")
months.remove("bob")
len(months)  # 12
months.extend(["bob", "sue"])
len(months)  # 14
months.count("bob")  # 1
months.pop(13)  # sue
months.pop(12)  # bob
len(months)  # 12
months.pop(12)  # IndexError
months.remove("jerky")  # ValueError

# REORDER METHODS (okay these are mutations also)
# (oh yeah, sequences are ORDERED)
#
# .sort()       Arrange in order
# .reverse()    Reverse the order


# INSPECTION METHODS
# (these are also in strings...so not mutations)
#
# .index()      Find index of a value
# .count()      Find number of elements equal to value
