sentence = "Now is the time for all good men to come to the aid of their country."
words = sentence.split()

# filter to count the "big" words only

big_words = []
for word in words:
    if len(word) > 3:
        big_words.append(word)

print(big_words)
