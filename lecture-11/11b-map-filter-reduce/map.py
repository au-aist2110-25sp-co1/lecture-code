naughty_words_str = "Potty Poop Poo-Poo Doo-Doo Pee-Pee Wee-Wee Woo-Woo"
naughty_words = naughty_words_str.split()

print(naughty_words)

lower_naughty = []
for word in naughty_words:
    new_word = word.lower()
    lower_naughty.append(new_word)

print(lower_naughty)

user_val = input("Enter a word: ").lower()
if user_val in lower_naughty:
    print("Eat soap you naughty child!")
else:
    print("You are so nice!")
