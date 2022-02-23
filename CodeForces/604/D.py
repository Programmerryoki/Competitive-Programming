# a,b,c,d = [int(i) for i in input().split()]
nums = [int(i) for i in input().split()]
n = sum(nums)
ans = []

def recur(l,nums):
    global ans
    # print(l, nums)
    if sum(nums) == 0:
        ans = l
        return

    pos = []
    num = l[-1]
    # print(num)
    if num > 0 and nums[num-1] > 0:
        # print("p1", num)
        nums[num-1] -= 1
        l.append(num - 1)
        # print(l,nums)
        recur(l,nums)
    num = l[-1]
    if num < 3 and nums[num+1] > 0:
        # print("p2", num)
        nums[num+1] -= 1
        l.append(num + 1)
        # print(l, nums)
        recur(l,nums)

if sum(nums) > 0:
    if nums[0] > 0:
        nums[0] -= 1
        recur([0], nums)
    if len(ans) == 0 and nums[1] > 0:
        # print("a")
        nums[1] -= 1
        recur([1],nums)
    if len(ans) == 0 and nums[2] > 0:
        nums[2] -= 1
        recur([2],nums)
    if len(ans) == 0 and nums[3] > 0:
        nums[3] -= 1
        recur([3],nums)

    # print(ans, nums)
    if len(ans) == n and sum(nums) == 0:
        print("YES")
        print(" ".join(map(str, ans)))
    else:
        print("NO")
else:
    print("NO")