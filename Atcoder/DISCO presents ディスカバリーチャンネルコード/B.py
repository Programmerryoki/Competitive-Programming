N = int(input())
length = [int(i) for i in input().split()]
pos = []
s1 = sum(length)
s2 = 0

for a in range(len(length)):
    pos.append(max(s1,s2) - min(s1,s2))
    s1 -= length[a]
    s2 += length[a]
    # print("pos " + str(a)+":",sum(length[:a]), sum(length[a:]))
# print(pos)

print(min(pos))