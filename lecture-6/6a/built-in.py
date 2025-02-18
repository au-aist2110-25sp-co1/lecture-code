# print()	input()
# abs()     max()       min()       pow()       round()
# dir()     eval()      exec()      hash()      help()
# bool()    float()     int()       str()       type()
# chr()     ord()       len()

val = -7

abs_val = abs(val)
print(abs_val)

abs(10)   # 10
abs(-271.63) # 271.63

max(7, 3, 4, 55)  # 7

# Get a value that is at least a number or larger
newval = int(input("enter a num above 10: "))
actualval = max(newval, 10) 
print(f"You entered {actualval}")


pow(3,2)  # 3 ^ 2 = 9
