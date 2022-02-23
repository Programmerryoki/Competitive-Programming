from math import ceil

n = int(input())
ppl = [[int(i) for i in input().split()]+[j] for j in range(n)]
if n == 1:
    print(ppl[0][-1]+100)
    exit()
ans = [i[3] for i in ppl]
ppl.sort(key = lambda x: (-x[0], x[1], x[2]))
rank = 0
points = [100,75,60,50,45,40,36,32,29,26,24,22,20,18,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1]
i = 1; j = 0
while j < n and rank < 30:
    if i < n and ppl[j][:3] == ppl[i][:3]:
        i += 1
    else:
        if i - j == 1:
            ans[ppl[j][-1]] += points[rank]
            rank += 1
            j = i
        else:
            point = ceil(sum(points[rank:rank+i-j]) / (i-j))
            rank += i-j
            for t in range(j,i):
                ans[ppl[t][-1]] += point
            j = i
print(*ans,sep="\n")