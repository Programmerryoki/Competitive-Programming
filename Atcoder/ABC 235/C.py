N,Q = [int(i) for i in input().split()]
nums = {}
A = [int(i) for i in input().split()]
for i in range(N):
    if A[i] not in nums:
        nums[A[i]] = []
    nums[A[i]].append(i+1)
for _ in range(Q):
    x,k = [int(i) for i in input().split()]
    if x in nums and len(nums[x]) > k-1:
        print(nums[x][k-1])
    else:
        print(-1)