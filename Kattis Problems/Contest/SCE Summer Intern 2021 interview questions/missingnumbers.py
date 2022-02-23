n = int(input())
nums = set([int(input()) for i in range(n)])
ans = []
for i in range(1,max(nums)+1):
    if i not in nums:
        ans.append(i)
print("\n".join(map(str, ans)) if ans else "good job")