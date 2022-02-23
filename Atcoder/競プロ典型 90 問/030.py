N,K = [int(i) for i in input().split()]
if K == 1:
    print(N-1)
    exit()
nums = [0]*(N+1)
count = 0
for i in range(2, N+1):
    if nums[i] >= K:
        count += 1
    if nums[i] != 0:
        continue
    for j in range(i*2, N+1, i):
        nums[j] += 1
print(count)