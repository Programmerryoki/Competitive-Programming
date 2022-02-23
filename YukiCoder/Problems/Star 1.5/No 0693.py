N = int(input())
A = [int(i) for i in input().split()]
count = [0]*(N)
for a in A:
    count[a-1] += 1
# print(count)
tc = 0
k = -1
for i,n in enumerate(count):
    if n > 1:
        for _ in range(n-1):
            j = count.index(0, k+1)
            count[j] += 1
            tc += abs(j - i)
            # print(j, i)
            k = j
print(tc)