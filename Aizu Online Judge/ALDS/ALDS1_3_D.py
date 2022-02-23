S = input()
land = []
h = 0
j = 0
for i,s in enumerate(S):
    if s == "\\":
        h -= 1
    elif s == "/":
        h += 1
    if h == 0:
        land.append([j, i])
        h = 0
        j = i+1
    elif h > 0:
        j = i
    