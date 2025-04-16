# Why not just multiple variables??

# Why this:
duck_colors = {"huey": "red", "dewey": "blue", "louie": "green"}

# And not just this:
huey = "red"
dewey = "blue"
louie = "green"


king = """
The most important things are the hardest to say. They are the things you get
ashamed of, because words diminish them — words shrink things that seemed
limitless when they were in your head to no more than living size when they're
brought out. But it's more than that, isn't it? The most important things lie
too close to wherever your secret heart is buried, like landmarks to a treasure
your enemies would love to steal away. And you may make revelations that cost
you dearly only to have people look at you in a funny way, not understanding
what you've said at all, or why you thought it was so important that you almost
cried while you were saying it. That's the worst, I think. When the secret stays
locked within not for want of a teller but for want of an understanding ear.
"""

word_counts = dict()
for word in king.split():
    word = word.lower()
    if word not in word_counts:
        word_counts[word] = 1
    else:
        word_counts[word] += 1

# print(f"There are {len(word_counts)} unique words")
# print(word_counts)


# Deal with lowercase and punctuation

import re

# from string import punctuation

# punc_to_none = str.maketrans("", "", punctuation)

# a_list = [] or list()
word_counts = {}  # same as dict()
for word in king.split():
    # word = word.translate(punc_to_none).lower()
    word = re.sub(r"[^\w']", "", word.lower())
    word = word.strip()
    if len(word) == 0:
        continue
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

# print(f"There are {len(word_counts)} unique words")
# print(word_counts)


# sorting by *** KEYS ***

alphabetical_words = list(word_counts.keys())
alphabetical_words.sort()

# Get first 10:
counter = 0
for word in alphabetical_words:
    count = word_counts[word]
    print(f"{count:>2} : {word}")
    counter += 1
    if counter >= 10:
        break


print()
print()

# sorting by *** VALUES ***
# (kinda goofy, so just as FYI and for your copy/paste pleasure)

sorted_words = sorted(word_counts, key=word_counts.get, reverse=True)

# Get first 10:
counter = 0
for word in sorted_words:
    count = word_counts[word]
    print(f"{count:>2} : {word}")
    counter += 1
    if counter >= 10:
        break
