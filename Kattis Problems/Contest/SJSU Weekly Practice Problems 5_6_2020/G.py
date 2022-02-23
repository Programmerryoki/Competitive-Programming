from functools import reduce
from random import randint

# board = [input() for i in range(9)]

nums = [randint(1,100) for i in range(1,10)]
p = [nums[0]]
for i in range(1,len(nums)):
    p.append(p[-1]^nums[i])
print(nums)
print(p)
for i in range(0,len(nums)-1):
    for j in range(i+1, len(nums)):
        print(i,j)
        print(reduce(lambda x,y: x^y, nums[i:j]), end="")
        print("",p[i]^p[j])