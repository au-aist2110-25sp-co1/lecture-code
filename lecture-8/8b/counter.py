# Sentinel-Controlled Loops

# while < "sentinel" is True >:
#     do stuff
#     sentinel condition (may) change either in code or externally

# Counter-Controlled Loops

lcount = 0

while lcount < 10:
    # lcount = lcount + 1
    lcount += 1
    print(f"Hello {lcount}")
