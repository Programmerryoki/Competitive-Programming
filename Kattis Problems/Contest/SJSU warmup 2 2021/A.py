from collections import deque

Moves = input()
ans = []
prev2 = deque()
counter = {"R":"S","B":"K","L":"H"}
special = set("SKH")
for m in Moves:
    prev2.append(counter[m])
    if set(prev2) == special:
        ans.append("C")
        prev2.clear()
    if len(prev2) > 2:
        ans.append(prev2.popleft())
while prev2:
    ans.append(prev2.popleft())
print("".join(ans))