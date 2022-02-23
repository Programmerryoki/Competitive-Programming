N = int(input())
users = set()
ans = []
for case in range(1, N+1):
    name = input()
    if not name in users:
        ans.append(case)
        users.add(name)
print("\n".join(map(str, ans)))