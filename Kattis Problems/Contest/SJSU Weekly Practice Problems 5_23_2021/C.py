W,P = map(int, input().split())
L = [0]+[int(i) for i in input().split()]+[W]
L.sort()
pos = set()
for i in range(len(L)-1):
    for j in range(i+1,len(L)):
        pos.add(L[j] - L[i])
print(" ".join(map(str, sorted(pos))))