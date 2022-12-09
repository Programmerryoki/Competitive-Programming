h1 = "ABC"
h2 = "XYZ"
sh = [1,2,3]
ts = 0
while True:
    try:
        o, y = input().split()
    except:
        break
    op = h1.index(o)
    if y == 'X':
        ts += sh[(op-1)%len(h1)]
    elif y == 'Y':
        ts += 3 + sh[op]
    else:
        ts += 6 + sh[(op+1)%len(h1)]
print(ts)

# h1 = "ABC"
# h2 = "XYZ"
# sh = [1,2,3]
# ts = 0
# while True:
#     try:
#         o, y = input().split()
#     except:
#         break
#     op = h1.index(o); you = h2.index(y)
#     if op == you:
#         ts += 3 + sh[you]
#     elif you - op in [1,-2]:
#         ts += 6 + sh[you]
#     else:
#         ts += sh[you]
# print(ts)