stacks = [
    list("GFVHPS"),
    list("GJFBVDZM"),
    list("GMLJN"),
    list("NGZVDWP"),
    list("VRCB"),
    list("VRSMPWLZ"),
    list("THP"),
    list("QRSNCHZV"),
    list("FLGPVQJ")
]

while True:
    try:
        line = input()
    except:
        break
    _,cmd,_,s,_,e = line.split()
    stacks[int(e)-1].extend(stacks[int(s)-1][-int(cmd):])
    stacks[int(s)-1] = stacks[int(s)-1][:-int(cmd)]
print("".join(i[-1] for i in stacks))

# stacks = [
#     list("GFVHPS"),
#     list("GJFBVDZM"),
#     list("GMLJN"),
#     list("NGZVDWP"),
#     list("VRCB"),
#     list("VRSMPWLZ"),
#     list("THP"),
#     list("QRSNCHZV"),
#     list("FLGPVQJ")
# ]
#
# while True:
#     try:
#         line = input()
#     except:
#         break
#     _,cmd,_,s,_,e = line.split()
#     for i in range(int(cmd)):
#         stacks[int(e)-1].append(stacks[int(s)-1].pop())
# print("".join(i[-1] for i in stacks))