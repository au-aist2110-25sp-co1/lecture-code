num1 = 6
num2 = 3
ans = num1 / num2

print("num1 / num2 = ans")
print("1: " + str(num1) + " / " + str(num2) + " = " + str(ans))

# String interpolation

print(f"2: {num1} / {num2} = {ans}")

print(f"3: {num1} / {num2} = {num1 / num2}")

out = f"4: {num1} / {num2} = {num1 / num2}"

print(out)


# f"{num:.0f}"   ZERO DECIMAL PLACES
print(f"5: {num1} / {num2} = {ans:.0f}")

# f"{num:.2f}"   TWO DECIMAL PLACES
print(f"6: {num1} / {num2} = {ans:.2f}")
print(f"7: {num1} / {num2} = ${ans:.2f}")


num1 = 8
num2 = 3
ans = num1 / num2

# f"{num:.2f}"   ROUNDS TWO DECIMAL PLACES
print(f"7: {num1} / {num2} = ${ans:.2f}")


print(f"{123456789:,}")
print(f"{123_456_789:,}")
print(f"{123_456_789:,.2f}")

print(ans)

print(f"{ans:.4f}")

num1 = 9
num2 = 3
ans = num1 / num2

print(f"{ans:.4f}")


round_ans = round(ans, 4)

print(round_ans)


num1 = 4
num2 = 3
ans = num1 / num2
round_ans = round(ans, 4)

print(round_ans)
print(ans)
