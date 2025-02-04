# Ask for two numbers
# Should be between -100 and 100 (inclusive)
# divide and show answer rounded to at most 3 decimals


try:
    num1 = int(input("Enter a number: "))
except:
    print("INVALID INPUT")
    exit()

if not (-100 <= num1 <= 100):
    print("INVALID RANGE")
    exit()

try:
    num2 = int(input("Enter a second number: "))
except:
    print("INVALID INPUT")
    exit()

if not (-100 <= num2 <= 100):
    print("INVALID RANGE")
    exit()

try:
    ans = num1 / num2
    round_ans = round(ans, 3)
    print(round_ans)
except:
    print("an expected error occurred")
