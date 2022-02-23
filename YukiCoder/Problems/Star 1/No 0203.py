C = input() + input()
c = 0
mc = 0
for i in C:
    if i == "o":
        c += 1
        mc = max(mc,c)
    else:
        c = 0
print(mc)