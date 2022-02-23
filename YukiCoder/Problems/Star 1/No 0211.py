K = int(input())
pos = {}
for i in [2,3,5,7,11,13]:
    for j in [4,6,8,9,10,12]:
        try:
            pos[i*j] += 1
        except:
            pos[i*j] = 1
print(pos[K]/36 if K in pos else 0)