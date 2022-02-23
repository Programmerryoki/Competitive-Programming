n = int(input())
nums = [int(input()) for i in range(n)]
snums = set(nums)
m = max(nums)
ans = []
for i in range(1,m+1):
    if not i in snums:
        ans.append(i)
print("\n".join(map(str, ans)) if len(ans) else "good job")