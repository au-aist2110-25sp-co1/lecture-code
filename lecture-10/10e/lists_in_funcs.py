# RABBIT HOLE STRAIGHT TO WONDERLAND

x = 12
y = "abc"
l = ["the", "quick", "brown", "fox"]
m = []
m.append(1)
m.append(2)

# Value Types vs. Reference Types

# stack             heap
# x: 12             #729: ['the','quick','brown','fox']
# y: 'abc'          #826: [1,2]
# l: <729>          #777: ['the','quick','brown','fox']
# m: <826>
# a: 10
# g: <729>
# h: <777>


a = x
print(a == x)
a = a - 2
print(a == x)

g = l
print(g == l)
g[0] = "HE"
print(g)
print(l)
print(g == l)

h = l.copy()
print(h == l)
h[1] = "KIK"
print(h)
print(l)
print(h == l)


# Passing By Value vs Passing By Reference


def change_val(num):
    num = num + 5
    print(num)


num = 5
print(f"before: {num}")
change_val(num)
print(f"after: {num}")


def change_ref(lst):
    lst = [1, 2, 3]
    print(lst)


lst = [7, 8]
print(f"before: {lst}")
change_ref(lst)
print(f"after: {lst}")


def mutate_ref(lst):
    lst.append(9)
    # print(lst)


lst = [7, 8]
print(f"before: {lst}")
mutate_ref(lst)
print(f"after: {lst}")
