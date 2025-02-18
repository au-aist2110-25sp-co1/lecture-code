from random import randint

num = randint(1,10)

print("I'm thinking of a number between 1 and 10.")
try:
    guess = int(input("What is it? "))
except:
    print("Nice try, wise guy! That's not even a number!")
    exit()

if guess < num:
    print(f"Nope. Too low. I was thinking of {num}")
elif guess > num:
    print(f"Nope. Too high. I was thinking of {num}")
else:
    print(f"YES!!!! I was thinking of {num}, too. Great minds think alike!")


