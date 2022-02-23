def a(l):
    return [l[1],l[0],l[2]]


def b(l):
    return [l[0], l[2], l[1]]


def c(l):
    return [l[2], l[1], l[0]]


trik = input()
l = [1, 0, 0]
for i in trik:
    if i=="A":
        l = a(l)
    elif i=="B":
        l = b(l)
    elif i=="C":
        l = c(l)
print(l.index(1)+1)