N = int(input())
A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]

nums = [{A[i]^B[j] for i in range(N)} for j in range(N)]
s = nums[0]
for i in nums[1:]:
    s &= i
print(len(s))
if len(s):
    print("\n".join(str(i) for i in sorted(s)))