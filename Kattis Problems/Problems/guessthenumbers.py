nums = [int(i) for i in input().split()]
n = nums[0]
m = nums[-1]
nums = nums[1:-1]
s = input()

values = {}

def search(val, nums):
    