nums = [5, 12, 17, 8, 4, 10]

# min = 9999999999999
# max = -9999999999999
smallest_word = nums[0]
biggest_word = nums[0]

for num in nums:
    if num < smallest_word:
        smallest_word = num
    if num > biggest_word:
        biggest_word = num

print(f"min val: {smallest_word}")
print(f"max val: {biggest_word}")

smallest_word = min(nums)
biggest_word = max(nums)

print(f"min val: {smallest_word}")
print(f"max val: {biggest_word}")




vals = ["5", "12", "17", "8", "4", "10"]

# min_val = min(vals)
# max_val = max(vals)
smallest_word = int(vals[0])
biggest_word = int(vals[0])

for val in vals:
    num = int(val)
    if num < smallest_word:
        smallest_word = num
    if num > biggest_word:
        biggest_word = num

smallest_word = vals[0]
biggest_word = vals[0]

for val in vals:
    num = int(val)
    if num < int(smallest_word):
        smallest_word = num
    if num > int(biggest_word):
        biggest_word = num


print(f"min val: {smallest_word}")
print(f"max val: {biggest_word}")



sentence = "four score and seven years ago our fathers brought forth upon this continent a new nation"
words = sentence.split()

smallest_word = words[0]
biggest_word = words[0]

for word in words:
    if len(word) < len(smallest_word):
        smallest_word = word
    if len(word) > len(biggest_word):
        biggest_word = word


print(smallest_word)
print(biggest_word)