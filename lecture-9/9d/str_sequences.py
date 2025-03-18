s = "the quick brown fox"

print(s)
print(s[0], s[1], s[2])

print(len(s))

# count = 0
# while count < len(s):
#     c = s[count]
#     print(c)
#     count += 1

for c in s:
    print(c)

try:
    print(s[20])
except:
    print("BOOM")
    
