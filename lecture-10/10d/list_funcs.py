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

# len()
print(len(oregon_temps))

# max()
# min()
print(max(oregon_temps))
print(min(oregon_temps))
print(max(months))

# sum()
print(sum(oregon_temps))

avg = sum(maine_temps) / len(maine_temps)
print(avg)

# sorted()
# reversed()

# months.sort()
m2 = sorted(months)
print(m2)
print(months)

print("".join(sorted("mississippi")))
