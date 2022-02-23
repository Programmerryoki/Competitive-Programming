mc = input()
nop = 0
j = 0
i = 1
while i < len(mc):
    if mc[i].isupper():
        # print(mc, i, mc[i], (4 - i%4)%4)
        nop += (4 - i%4)%4
        mc = mc[i:]
        i = 1
    else:
        i += 1
print(nop)