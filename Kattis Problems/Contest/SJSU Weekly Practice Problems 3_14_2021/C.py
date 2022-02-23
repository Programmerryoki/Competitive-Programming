from itertools import permutations
from bisect import bisect_right

num = input()
nums = set()
for i in permutations(num):
    n = "".join(i)
    if len(n) == len(str(int(n))):
        nums.add(int(n))
nums = list(nums)
nums.sort()
index = bisect_right(nums, int(num))
if index == len(nums):
    print(0)
else:
    print(nums[index])