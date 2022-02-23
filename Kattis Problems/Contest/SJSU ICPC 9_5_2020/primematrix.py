N,B = [int(i) for i in input().split()]
ps = (1 + N)*(N)//2
n = 0
while True:
    for i in range(2,ps):
        if (ps+n)%i == 0:
            break
    else:
        break
    n += 1
nums = [i for i in range(1,N+1)]
for j in range(n):
    nums[(len(nums) - j - 1)%len(nums)] += 1
print("\n".join(" ".join(map(str, nums[i:] + nums[:i])) for i in range(N)) if max(nums) <= B else "impossible")