total = 0

while True:
    try:
        num = int(input("ENTER NUM: "))
        total += num
        # print(f"Subtotal: {total}")
    except:
        break

print("THE TOTAL IS", total)
