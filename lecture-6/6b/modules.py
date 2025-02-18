# os        sys     typing  threading   subprocess
# io        socket  hashlib codecs
# math      random  re      datetime    time
# unittest  logging json    uuid

import math

math.cos(15)

pow(3,2)

# Use alias to avoid name "collisions" so you don't
# "clobber" built-in functions
from math import sin, pow as pow2

pow2(3,2)

# WARNING!!!! DO NOT USE FUNCTION NAMES FOR VARIABLE NAMES
min = min(3,2)
print(min)
new_min = min(5,4)

import random

random.randint(1,100)

from random import randint
print(randint(1,6))
