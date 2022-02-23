S = input()
c = 0
b = 0
for i in S:
    if i == "A":
        c += b
    else:
        b += 1
print(c)