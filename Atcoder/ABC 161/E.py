import sys
sys.setrecursionlimit(2*10**5)

N,K,C = [int(i) for i in input().split()]
S = input()

count = [0]*len(S)
total = 0
def work(p, wd):
    global total
    if len(wd) == K:
        for a in wd:
            count[a] += 1
        total += 1
        return

    j = p + C + 1
    # print("\t"*(len(wd)), j, p, wd)
    for a in range(j, len(S)):
        if S[a] == "o":
            work(a, wd + [a])

work(-C-1, [])
# print(count, total)
for i,a in enumerate(count, 1):
    if a == total:
        print(i)