nums = [int(i) for i in input().split()]
if len(nums) == 3:
    if nums.count(5) == 2 and nums.count(7) == 1:
        print("YES")
    else:
        print("NO")