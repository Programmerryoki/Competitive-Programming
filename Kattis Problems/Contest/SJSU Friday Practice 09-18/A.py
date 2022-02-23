from itertools import permutations
box = [int(i) for i in input().split()]
h1,h2 = box[-2:]
box = box[:-2]
for pat in permutations([i for i in range(6)]):
    spat = [box[i] for i in pat]
    t1 = sum(spat[:3])
    t2 = sum(spat[3:])
    if t1 == h1 and t2 == h2:
        print(" ".join(map(str, sorted(spat[:3], reverse=True))) + " " + " ".join(map(str, sorted(spat[3:], reverse=True))))
        exit()