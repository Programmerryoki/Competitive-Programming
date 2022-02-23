from math import gcd

def gcdl(lst):
    n = lst[0]
    for i in lst:
        n = gcd(n,i)
    return n

n = int(input())
nums = [int(i) for i in input().split()]
vs = set(nums)
for i in range(n):
    for j in range(i+1,n+1):
        # print(nums[i:j])
        vs.add(gcdl(nums[i:j]))
print(len(vs))