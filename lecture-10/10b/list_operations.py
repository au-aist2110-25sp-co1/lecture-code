# Native Python list operators

trimurti = ["Brahma", "Vishnu", "Shiva"]
tridevi = ["Sarasvati", "Lakshmi", "Parvati"]

# ONE MORE METHOD
#
# .copy()       Create a list with duplicate elements

t2 = trimurti.copy()  # a full copy of trimurti


# + / +=        ADDITIVE CONCATENATION

trimurti + tridevi  # a COPY of the two merged lists
trimurti += tridevi  # trimurti is now MUTATED and permanently contains tridevi, too

# * / *=        MULTIPLICATIVE CONCATENATION

"-" * 80  # --------------- (but 80 of them)
tridevi * 3  # a new list with all of the tridevi in it 3 times
tridevi *= 2  # permanently mutates tridevi to contain all three deities twice

# in        FIND EXACT MATCH

"Vishnu" in trimurti  # True
"vishnu" in trimurti  # False
"is" in trimurti  # False

# == / != / is
# PLEASE WAIT...DIGGING RABBIT HOLE...
