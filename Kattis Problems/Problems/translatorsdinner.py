N,M = [int(i) for i in input().split()]

if M&1:
    print("impossible")
    exit()

language = [0]*N
trans = {j:[int(i) for i in input().split()] for j in range(M)}
lanTotran = {i:set() for i in range(N)}
lanTolan = {i:set() for i in range(N)}
for n,key in enumerate(trans):
    i,j = trans[key]
    language[i] += 1
    lanTotran[i].add(n)
    language[j] += 1
    lanTotran[j].add(n)
    lanTolan[i].add(j)
    lanTolan[j].add(i)
freq = [[language[i], i] for i in range(N)]
freq.sort()

print("frequency",language, freq)
print("t",trans)
print("l2t",lanTotran)
print("l2l",lanTolan)

pair = []
for i in range(N):
    f,lan = freq[i]
    while f > 1:
        fr = [[]]