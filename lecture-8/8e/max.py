# max_val = 0  # primed value is critical
max_val = -1e1000  # arbitrarily low value

while True:
    try:
        num = int(input("ENTER NUM: "))
        if num > max_val:
            max_val = num
    except:
        break

print("THE BIGGEST IS", max_val)
