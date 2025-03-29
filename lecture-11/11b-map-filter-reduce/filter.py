sentence = "Now is the time for all good men to come to the aid of their country."
words = sentence.split()

# filter to count the "big" words only

big_words = 0
for word in words:
    if len(word) > 3:
        big_words += 1


print(f"There are {big_words} big words in '{sentence}")
