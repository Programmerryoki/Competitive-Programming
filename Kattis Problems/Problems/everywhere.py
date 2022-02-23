n = int(input())
for a in range(n):
    p = int(input())
    place = []
    for b in range(p):
        pn = input()
        if pn not in place:
            place.append(pn)
    print(len(place))